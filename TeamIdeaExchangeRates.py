import requests
from bs4 import BeautifulSoup

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
valutes = soup.find_all('name')
nominal = soup.find_all('nominal')
values = soup.find_all('value')

rates = {}

for i in valutes:
    if "Венгерских форинтов" in i or "Норвежских крон" in i:
        rates[i.text] = float(values[valutes.index(i)].text.replace(",", "."))/float(nominal[valutes.index(i)].text)

print("Стоиомсть 1 норвежской кроны в венгерских форинтах составляет %s" %(rates["Норвежских крон"] / rates["Венгерских форинтов"]))