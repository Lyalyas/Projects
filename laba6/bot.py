'''@  Импортируем api pyTelegramBot, установленный заранее через терминал,
данные из файла config.py, в котором указали токен бота, 
модуль time, чтобы вызывать время во время запросов''' 
import telebot
import config
import random
import time

from telebot import types #@ Модуль, в котором определены все типы данных(текст, аудио и т.д).
import requests #@  Модуль для обработки URL
from bs4 import BeautifulSoup as b#@  Модуль для работы с HTML
import time #@  Модуль для остановки программы
import smtplib #@  Модуль для работы с почтой



URL = 'https://finance.rambler.ru/currencies/?ysclid=lemvjwn3gr793899689' #@ Переменная, которая хранит ссылку на сайт

#@  Переменная хранит заголовок Юзер-агента, с помощью нее будем  сообщать серверу, что запрос идет от браузера. 
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}  




r = requests.get(URL, headers=headers) #@ Создаем переменную, в которой будем хранить результат get- запроса к странице.
soup = b(r.text, 'lxml') #@ Создается объект BeautifulSoup. Данные передаются конструктору. Вторая опция уточняет объект парсинга.

'''@ Создаем переменную, в которой будем хранить возвращаемое методом find_all значение.
Метод .find_all() модуля BeautifulSoup4 просматривает и извлекает ВСЕХ потомков тега, которые соответствуют переданным фильтрующим аргументам,
в нашем случае блок каждой отдельной валюты находится в теге a со значением "finance-currency-table__tr" '''
USD = soup.find_all(
	"a", {"class": "finance-currency-table__tr"})

'''@ Перебираем извлеченный список потомков тега, просматривая значение тега div со значением 
"finance-currency-table__cell finance-currency-table__cell--currency", в которых хранятся наименования валют, 
сверяем с наименованиями самых актуальных  валют "Евро", "Доллар США", "Лира" ''' 
for usd in USD:
	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Евро":
		
'''@ В случае соответствия названий создаем соответсвующие переменнные (EURO, USD1, LIRA), и присваиваем им значение, найденное в теге div с классом 
"finance-currency-table__cell finance-currency-table__cell--value", который хранит значение курса соответствующей валюты ''' 
		EURO = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())

'''@ Проделываем ту же операцию с курсами Доллара США и Турецкой Лиры''' 
	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Доллар США":
		USD1 = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())

	if ((usd.find(
		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Турецкая лира":
		LIRA = ((usd.find(
			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())
		




'''@ Создаем в проекте бота путем создания переменной bot, которому присваем экземпляр класса TeleBot()- ему передаем полученный токен.
Этими действиям мы устанавливаем то, что мы будем описывать функционал именно для того бота, токен которого у нас имеется. ''' 

bot = telebot.TeleBot(config.TOKEN)



@bot.message_handler(commands=['start']) #@ Ожидаем от пользователя команду /start - старт работы бота

def welcome(message):
	'''@ Данная функция будет обрабатывать последующие команды пользователя после старта работы бота, 
	принимает на вход message- сообщение пользователя ''' 
	
	#@ Создаем  клавиатуру ReplyKeyboardMarkup — это шаблоны сообщений, предлагает варианты ответа пользователю
	
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  #@ Создаем переменную, которой присваем тип ReplyKeyboardMarkup. 
															  #@ resize_keyboard=True позволяет клавиатуре подгонится по высоте до возможного минимума.
	item3 = types.KeyboardButton("🇺🇸 Курс Доллара") #@ Создаем переменную, которая будет хранить кнопку "🇺🇸 Курс Доллара"
	item4 = types.KeyboardButton("🇪🇺 Курс Евро")	#@ Создаем переменную, которая будет хранить кнопку "🇪🇺 Курс Евро"
	item5 = types.KeyboardButton("🇹🇷 Курс Турецкой лиры")	#@ Создаем переменную, которая будет хранить кнопку "🇹🇷 Курс Турецкой лиры"

	'''@ ДОБАВЛЕНО ЗМОРКА И.Ю. 04/03/2023 10:00
	   Причина: Расширение функционала - возможность получить курс любой валюты''' 

	item6 = types.KeyboardButton("Выбрать другую валюту")	#@ Создаем переменную, которая будет хранить кнопку "Выбрать другую валюту"
	

	markup.add(item3, item4,item5, item6) #@ Добавляем созданные кнопки
	'''@  bot.send_message  - позволяет отправить сообщение пользователю, принимает аргументы message.chat.id, - id чата, и само сообщение
	message.from_user.first_name возвращает имя пользователя'''@ 
	bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name + "!" +' Этот бот был создан для выполнения задач лабораторной работы #@ 4')
	bot.send_message(message.chat.id, text="Выбирай любую валюту", reply_markup=markup)


@bot.message_handler(content_types=['text'])  #@ Метод ожидает от пользователя сообщение типа text


def lalala(message):
	'''@ Следующая функция будет будет обрабатывать ответ пользователя - принимать на вход сообщение, и в соотвествии с его содержимым, 
	выполнять определенные функции. В случае если пользователь нажал на кнопки "🇺🇸 Курс Доллара" или "🇪🇺 Курс Евро" или "🇹🇷 Курс Турецкой лиры"
	ему будут отправлены значения соответствующих курсов, которые мы храним в переменных USD1, EURO, LIRA соответственно''' 

	if message.chat.type == 'private':
		tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #@ Конвертация даты в читабельный вид
		if message.text == "🇺🇸 Курс Доллара":
			tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #@ Конвертация даты в читабельный вид
			bot.send_message(message.chat.id, "На "+tconv(message.date)+"⏰ курс составляет "+USD1+ " ₽")
		if message.text == "🇪🇺 Курс Евро":
			tconv = lambda x: time.strftime("%H:%M:%S %d.%m.%Y", time.localtime(x)) #@ Конвертация даты в читабельный вид
			bot.send_message(message.chat.id, "На "+tconv(message.date)+"⏰ курс составляет "+EURO+ " ₽")

		if message.text == "🇹🇷 Курс Турецкой лиры":
			
			bot.send_message(message.chat.id, "На "+tconv(message.date)+"⏰ курс составляет "+LIRA+ " ₽")
		if message.text == ("Выбрать другую валюту"):
			bot.send_message(message.chat.id, 'Напишите курс (пример:  Белорусский рубль)')
		
		'''@ ДОБАВЛЕНО ЗМОРКА И.Ю. 04/03/2023 10:30
	   Причина: Расширение функционала - возможность получить курс любой валюты''' 

		val = message.chat #@ принимаем значение отправленного пользователем сообщения		
		for usd in USD:
			'''@ В данном цикле будем перебирать все курсы валют, как мы делали ранее с Евро, Долларом США, и турецкой Лирой,
			находить среди названий валют - значение, которое было введено пользователем. В случае соответсвия, создаем переменную val1,
			хранящую значение валюты соответствующей валюты''' 
			if ((usd.find(
				"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == message.text:
				val1 = ((usd.find(
					"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())
				#@ Отправляем пользователю значение курса требоваемой валюты
				bot.send_message(message.chat.id, "На "+tconv(message.date)+"⏰ курс составляет "+val1+ " ₽") 




				


#@  RUN
bot.polling() #@ Функция, после вызова которой, TeleBot начинает опрашивать серверы Telegram на предмет новых сообщений.

