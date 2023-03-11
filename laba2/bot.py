import telebot
import config
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from telebot import types
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup as b# Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой
import json



bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	# sti = open('/Users/ilyaszmorka/Desktop/telebot/sticker1.webp', 'rb')
	# bot.send_message(message.chat.id, "Выбирай любую валюту")

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item3 = types.KeyboardButton("Ввести значения")
	item4 = types.KeyboardButton("Ввести ограничения и кратность")

	

	markup.add(item3, item4)
	bot.send_message(message.chat.id, text="Вводи значения функции", reply_markup=markup)





numbers = ''

a=[0,0]


@bot.message_handler(content_types=['text'])
def lalala(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Построить график")
	item2 = types.KeyboardButton("Ввести ограничения")
	item3 = types.KeyboardButton("Построить диаграмму")
	markup.add(item1, item2,item3)
	markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
	markup2.add(item3)
	if message.chat.type == 'private':
		if "[" in message.text:
			t=message.text[1:-1]
			print(t)
			k=t.split(',')
			print(k)
			minx = int(k[0])
			maxx = int(k[1])
			krat = int(k[2])
			n = list(range(1,11))
			filename = 'numbers.json'
			with open(filename) as f:
			    numbers = json.load(f)
			y = list(map(int, numbers))
			print(max(y), min(y))
			if minx > max(y) or maxx < min(y):
				bot.send_message(message.chat.id, text="ОШИБКА. Указанные границы выходят за область значений функции", reply_markup=markup)
			else:
				y1=y.copy()
				t=0
				
				for i in range(len(y)):
					if y[i]%krat !=0 or y[i]<minx or y[i]>maxx:
						y1.pop(i-t)
						n.pop(i-t)
						t+=1



				# y = np.array(y)

				
				barb=plt.bar(n, y1)	
				for i in range(len(y1)-1):
					if y1[i]/y1[i+1] <0.8 or y1[i]/y1[i+1]>1.2:
						barb[i+1].set_color('r')

				# plt.xlim([2, 5])
				plt.scatter (n, y1 )

	#add horizontal line at mean value of y
				plt.axhline (y=np.nanmean (y1 ), color='red', linestyle='--', linewidth= 3 , label='Avg')
				plt.savefig('saved_figure.png')
				with open("saved_figure.png", "rb") as file:
					data = file.read()
				bot.send_photo(message.from_user.id, photo=data)
				plt.gcf().clear()


				plt.plot(n, y1)	
				

				# plt.xlim([2, 5])
				plt.scatter (n, y1 )

	#add horizontal line at mean value of y
				plt.axhline (y=np.nanmean (y1 ), color='red', linestyle='--', linewidth= 3 , label='Avg')
				plt.savefig('saved_figure.png')
				with open("saved_figure.png", "rb") as file:
					data = file.read()
				bot.send_photo(message.from_user.id, photo=data)
				plt.gcf().clear()
				bot.send_message(message.chat.id, text="Среднее значение составляет "+str(np.nanmean (y1)), reply_markup=markup)








		elif ',' in message.text:
			numbers = message.text.split(",")
			filename = 'numbers.json'
			with open(filename, 'w') as f:
   				json.dump(numbers, f)
			
			bot.send_message(message.chat.id, text="Что будем делать с функцией?", reply_markup=markup)





		elif message.text == "Построить график":
			n = np.arange(1, 11, 1)
			filename = 'numbers.json'
			with open(filename) as f:
			    numbers = json.load(f)
			y = list(map(int, numbers))
			# y = np.array(y)

			
			plt.plot(n, y)	
			# plt.xlim([2, 5])
			plt.savefig('saved_figure.png')
			with open("saved_figure.png", "rb") as file:
			    data = file.read()
			bot.send_photo(message.from_user.id, photo=data)
			plt.gcf().clear()



		elif message.text == "Построить диаграмму":
			n = np.arange(1, 11, 1)
			filename = 'numbers.json'
			with open(filename) as f:
			    numbers = json.load(f)
			y = list(map(int, numbers))
			# y = np.array(y)

			
			plt.bar(n, y)	
			# plt.xlim([2, 5])
			plt.savefig('saved_figure.png')
			with open("saved_figure.png", "rb") as file:
			    data = file.read()
			bot.send_photo(message.from_user.id, photo=data)
			plt.gcf().clear()	

		elif message.text == 'Ввести ограничения':
			bot.send_message(message.chat.id, text="Введите ограничения формата [первая граница,вторая граница, кратность]")



		




				




# RUN
bot.polling()
