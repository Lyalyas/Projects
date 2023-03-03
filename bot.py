import telebot
import config
import random

from telebot import types
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup as b# Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой



URL = 'https://finance.rambler.ru/currencies/?ysclid=lemvjwn3gr793899689'


headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

current_converted_price = 0
difference = 5 # Разница после которой будет отправлено сообщение на почту

full_page = requests.get(URL, headers=headers)
r= full_page
soup = b(r.text, 'lxml')

USD = soup.find_all(
	"a", {"class": "finance-currency-table__tr"})
for usd in USD:
	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Евро":
		EURO = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())
	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Доллар США":
		USD1 = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())

	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Турецкая лира":
		LIRA = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())
		
# 		usd1 = ((usd.find(
# 			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text)
# print(usd1)

print(EURO, USD1, LIRA)





bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	# sti = open('/Users/ilyaszmorka/Desktop/telebot/sticker1.webp', 'rb')
	# bot.send_message(message.chat.id, "Выбирай любую валюту")

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item3 = types.KeyboardButton("🇺🇸 Курс Доллара")
	item4 = types.KeyboardButton("🇪🇺 Курс Евро")
	item5 = types.KeyboardButton("🇹🇷 Курс Турецкой лиры")
	

	markup.add(item3, item4,item5)
	bot.send_message(message.chat.id, text="Выбирай любую валюту", reply_markup=markup)


USD = soup.find_all(
	"a", {"class": "finance-currency-table__tr"})
for usd in USD:
	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Евро":
		EURO = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())
	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Доллар США":
		USD1 = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())

	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Турецкая лира":
		LIRA = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())
		
# 		usd1 = ((usd.find(
# 			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text)
# print(usd1)




@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == "🇺🇸 Курс Доллара":
			bot.send_message(message.chat.id, USD1)
		if message.text == "🇪🇺 Курс Евро":
			bot.send_message(message.chat.id, EURO)
		if message.text == "🇹🇷 Курс Турецкой лиры":
			bot.send_message(message.chat.id, LIRA)

				




# RUN
bot.polling()