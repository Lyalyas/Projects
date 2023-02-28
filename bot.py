import telebot
import config
import random

from telebot import types
import requests # Модуль для обработки URL
from bs4 import BeautifulSoup as b# Модуль для работы с HTML
import time # Модуль для остановки программы
import smtplib # Модуль для работы с почтой

# # Основной класс
# class Currency:
# 	# Ссылка на нужную страницу
# 	URL = 'https://www.rbc.ru'
# 	# Заголовки для передачи вместе с URL
# 	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

# 	current_converted_price = 0
# 	difference = 5 # Разница после которой будет отправлено сообщение на почту

# 	def __init__(self):
# 		# Установка курса валюты при создании объекта
# 		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

# 	# Метод для получения курса валюты
# 	def get_currency_price(self):
# 		# Парсим всю страницу
# 		full_page = requests.get(self.URL, headers=self.headers)

# 		# Разбираем через BeautifulSoup
# 		soup = BeautifulSoup(full_page.content, 'html.parser')

# 		# Получаем нужное для нас значение и возвращаем его
# 		# convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
# 		return full_page.status_code

# urrency.get_currency_price()
# print(Currency.get_currency_price())

# Основной класс

	# Ссылка на нужную страницу
URL = 'https://finance.rambler.ru/currencies/?ysclid=lemvjwn3gr793899689'
	# Заголовки для передачи вместе с URL

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

current_converted_price = 0
difference = 5 # Разница после которой будет отправлено сообщение на почту

full_page = requests.get(URL, headers=headers)
r= full_page
soup = b(r.text, 'lxml')
# USD = soup.find_all(
# 	'div', class_ ="finance-currency-table__body"


# 	)

# USD = soup.find(title = "Евро")
# print(USD[2])
# for uds in USD:
# 	print(uds.text)
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












# bot = telebot.TeleBot(config.TOKEN)

# @bot.message_handler(commands=['start'])
# def welcome(message):
# 	# sti = open('/Users/ilyaszmorka/Desktop/telebot/sticker1.webp', 'rb')
# 	bot.send_message(message.chat.id, 'Привет')

# 	# keyboard
# 	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 	item1 = types.KeyboardButton("💵 Курс Доллара")
# 	item2 = types.KeyboardButton("💶 Курс Евро")
# 	item3 = types.KeyboardButton("💶 Курс Турецкой лиры")

# 	markup.add(item1, item2,item3)

# 	bot.send_message(message.chat.id, "настя привет солнце, {0.first_name}!\nЯ - <b>{1.first_name}</b>, друг или подружка Ильяса, там сложно в общем.".format(message.from_user, bot.get_me()),
# 		parse_mode='html', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def lalala(message):
# 	if message.chat.type == 'private':
# 		if message.text == '🎲 Рандомное число':
# 			bot.send_message(message.chat.id, str(random.randint(0,100)))
# 		elif message.text == '😊 Как дела?':

# 			markup = types.InlineKeyboardMarkup(row_width=2)
# 			item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
# 			item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

# 			markup.add(item1, item2)

# 			bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
# 		else:
# 			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
# 	try:
# 		if call.message:
# 			if call.data == 'good':
# 				bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
# 			elif call.data == 'bad':
# 				bot.send_message(call.message.chat.id, 'Бывает 😢')

# 			# remove inline buttons
# 			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
# 				reply_markup=None)

# 			# show alert
# 			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
# 				text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

# 	except Exception as e:
# 		print(repr(e))

# # RUN
# bot.polling(none_stop=True)





# import telebot
# import config
# import random

# from telebot import types
# import requests # Модуль для обработки URL
# from bs4 import BeautifulSoup as b# Модуль для работы с HTML
# import time # Модуль для остановки программы
# import smtplib # Модуль для работы с почтой

# # # Основной класс
# # class Currency:
# # 	# Ссылка на нужную страницу
# # 	URL = 'https://www.rbc.ru'
# # 	# Заголовки для передачи вместе с URL
# # 	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

# # 	current_converted_price = 0
# # 	difference = 5 # Разница после которой будет отправлено сообщение на почту

# # 	def __init__(self):
# # 		# Установка курса валюты при создании объекта
# # 		self.current_converted_price = float(self.get_currency_price().replace(",", "."))

# # 	# Метод для получения курса валюты
# # 	def get_currency_price(self):
# # 		# Парсим всю страницу
# # 		full_page = requests.get(self.URL, headers=self.headers)

# # 		# Разбираем через BeautifulSoup
# # 		soup = BeautifulSoup(full_page.content, 'html.parser')

# # 		# Получаем нужное для нас значение и возвращаем его
# # 		# convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
# # 		return full_page.status_code

# # urrency.get_currency_price()
# # print(Currency.get_currency_price())

# # Основной класс

# 	# Ссылка на нужную страницу
# URL = 'https://finance.rambler.ru/currencies/?ysclid=lemvjwn3gr793899689'
# 	# Заголовки для передачи вместе с URL

# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# current_converted_price = 0
# difference = 5 # Разница после которой будет отправлено сообщение на почту

# full_page = requests.get(URL, headers=headers)
# r= full_page
# soup = b(r.text, 'lxml')
# # USD = soup.find_all(
# # 	'div', class_ ="finance-currency-table__body"


# # 	)

# USD = soup.find(title = "Евро")
# print(USD[2])
# for uds in USD:
# 	print(uds.text)
# USD = soup.find_all(
# 	"a", {"class": "finance-currency-table__tr"})
# for usd in USD:
# 	if ((usd.find(
# 		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Евро":
# 		EURO = ((usd.find(
# 			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())
# 	if ((usd.find(
# 		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Доллар США":
# 		USD1 = ((usd.find(
# 			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())

# 	if ((usd.find(
# 		"div", {"class": "finance-currency-table__cell finance-currency-table__cell--currency"})).text.strip()) == "Турецкая лира":
# 		LIRA = ((usd.find(
# 			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text.strip())
		
# # 		usd1 = ((usd.find(
# # 			"div", {"class": "finance-currency-table__cell finance-currency-table__cell--value"})).text)
# # print(usd1)

# print(EURO, USD1, LIRA)












bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	# sti = open('/Users/ilyaszmorka/Desktop/telebot/sticker1.webp', 'rb')
	bot.send_message(message.chat.id, "Выбирай любую валюту")

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("🇺🇸 Курс Доллара")
	item2 = types.KeyboardButton("🇪🇺 Курс Евро")
	item3 = types.KeyboardButton("🇹🇷 Курс Турецкой лиры")

	markup.add(item1, item2,item3)


@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == "🇺🇸 Курс Доллара":
			bot.send_message(message.chat.id, USD1)
		if message.text == "🇪🇺 Курс Евро":
			bot.send_message(message.chat.id, EURO)
		if message.text == "🇹🇷 Курс Турецкой лиры":
			bot.send_message(message.chat.id, LIRA)

				
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')



# RUN
bot.polling()