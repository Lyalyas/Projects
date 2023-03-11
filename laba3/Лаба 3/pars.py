from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup as b
import json
import csv
import random
from time import sleep
import time
import datetime
from openpyxl.chart import PieChart, Reference, Series, BarChart

fn = 'data.xlsx'
wb=load_workbook(fn)
ws = wb['Data']

URL = "https://www.myfxbook.com/forex-broker-quotes/xm-group/2824"
URL1 = 'https://www.myfxbook.com/ru/forex-broker-quotes/fxpro/5168'
URL2 = 'https://www.myfxbook.com/ru/forex-broker-quotes/ic-markets/2320'
#
headers = {
	"Accept": "*/*",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
}
for i in range(5):
	
	
	print("iteration ", i)
	r = requests.get(URL, headers=headers) #@ Создаем переменную, в которой будем хранить результат get- запроса к странице.
	r1 = requests.get(URL1, headers=headers)
	r2 = requests.get(URL2, headers=headers)

	soup = b(r.text, 'lxml')
	soup1= b(r1.text, 'lxml')
	soup2= b(r2.text, 'lxml')

# data = []
# table = soup.find('table', attrs={'class':'spreads-table table text-center no-custom-css'})
# table_body = table.find('tbody')
# rows = table_body.find_all('tr')
# for row in rows:
# 	c=row.find_all('td')
# 	print(c)
# 	# b=c.find_all(
# 	# 	"a", {"class": "no-hover noCursorPointer"})
# 	# print(b)
	dt_now = datetime.datetime.now()
	XMP_group=float(soup.find("td", {"id": "2824_1Ask"}).text)
	FX_pro = float(soup1.find("td", {"id": "5168_1Ask"}).text)
	one_C = float(soup2.find("td", {"id": "2320_1Ask"}).text)
	sr_num = (float(XMP_group) + float(FX_pro)+ float(one_C)) / 3
	ws.append({'B':XMP_group, 'C':FX_pro, 'D':one_C, 'E':sr_num, 'F':dt_now})


	print(XMP_group, FX_pro, one_C)

	time.sleep(4)
values = Reference(worksheet=ws,
                 min_row=1,
                 max_row=100,
                 min_col=2,
                 max_col=4)
# создаем объект столбчатой диаграммы
chart = BarChart()
# добавляем в диаграмму выбранный диапазон значений
chart.add_data(values, titles_from_data=True)
# привязываем диаграмму к ячейке `E15`
ws.add_chart(chart, "F11")
# определяем размеры диаграммы в сантиметрах
chart.width = 20
chart.height = 5
# сохраняем и смотрим что получилось
wb.save(fn)
wb.save(fn)
wb.close()
