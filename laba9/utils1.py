import matplotlib.pyplot as plt
import telebot
import config
import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sqlite3
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

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
    item3 = types.KeyboardButton("График по автомобилям")
    item4 = types.KeyboardButton("График по водителям")

    

    markup.add(item3, item4)
    bot.send_message(message.chat.id, text="Выбери необходимый график", reply_markup=markup)





numbers = ''

a=[0,0]


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
            if message.text == "График по автомобилям":
                #/Users/ilyaszmorka/project_test/project1/db.sqlite3'
                db = sqlite3.connect('C:/Users/Ильяс/Desktop/laba9/project_test/project1/db.sqlite3')
                sql = db.cursor()
                n=['a','b','']
                fuel_sql=[]
                cars=[]
                for value in sql.execute("SELECT * FROM app_car"):
                    fuel_sql.append(value[5])
                for value in sql.execute("SELECT * FROM app_car"):
                    cars.append(value[1])
                print(cars)
                barb=plt.bar(cars, fuel_sql) 

                fig,ax=plt.subplots()
                barb=plt.bar(cars, fuel_sql) 
                plt.scatter (cars, fuel_sql )
                ax.set_xlabel('Автобомили')
                ax.set_ylabel('Общий расход топлива')
                #add horizontal line at mean value of y
                plt.axhline (y=np.nanmean (fuel_sql ), color='red', linestyle='--', linewidth= 3 , label='Avg')
                plt.savefig('saved_figure.png')


                with open("saved_figure.png", "rb") as file:
                    data = file.read()
                bot.send_photo(message.from_user.id, photo=data)
                bot.send_message(message.chat.id, text="Среднее значение расхода топлива составляет "+str(round(np.nanmean (fuel_sql),4)) + " литров")
                plt.gcf().clear()

            if  message.text == "График по водителям":
                db = sqlite3.connect('C:/Users/Ильяс/Desktop/laba9/project_test/project1/db.sqlite3')
                sql = db.cursor()
                run=[]
                drivers=[]
                for value in sql.execute("SELECT * FROM app_drivers"):
                    run.append(value[4])
                for value in sql.execute("SELECT * FROM app_drivers"):
                    drivers.append(value[1])
                plt.figure(figsize=(1,5))
                barb=plt.bar(drivers, run) 

                fig,ax=plt.subplots()
                barb=plt.bar(drivers, run) 
                plt.scatter (drivers, run)
                ax.set_xlabel('Водители')
                ax.set_ylabel('Общий пробег')

                #add horizontal line at mean value of y
                plt.axhline (y=np.nanmean (run), color='red', linestyle='--', linewidth= 3 , label='Avg')
                plt.savefig('saved_figure1.png')

                plt.gcf().clear() 

                with open("saved_figure1.png", "rb") as file:
                    data = file.read()
                bot.send_photo(message.from_user.id, photo=data)
                bot.send_message(message.chat.id, text="Среднее значение пробега составляет "+str(round(np.nanmean (run),4)) + " киломметров")
                plt.gcf().clear()

                




                




# RUN
bot.polling()







