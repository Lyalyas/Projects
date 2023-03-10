import requests
from bs4 import BeautifulSoup as b
import json
import csv
import random
from time import sleep
import time

URL = "https://www.myfxbook.com/forex-broker-quotes/xm-group/2824"
URL1 = 'https://www.myfxbook.com/ru/forex-broker-quotes/fxpro/5168'
URL2 = 'https://www.myfxbook.com/ru/forex-broker-quotes/ic-markets/2320'
#
headers = {
	"Accept": "*/*",
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"
}
for i in range(100):
	
	time.sleep(30)
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

	XMP_group=soup.find("td", {"id": "2824_1Ask"}).text
	FX_pro = soup1.find("td", {"id": "5168_1Ask"}).text
	FOREX = soup2.find("td", {"id": "2320_1Ask"}).text
	print(XMP_group, FX_pro, FOREX)



