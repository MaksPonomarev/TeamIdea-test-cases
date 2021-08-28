import requests
from datetime import datetime

class Weather:

    def __init__(self, token):
        self.token = token
        self.URL = "https://api.openweathermap.org/data/2.5/onecall?lat=56.55&lon=59.57&exclude=minutely,hourly&appid=%s" %token

    def get_min_temp_diff(self):
        response = requests.get(self.URL)
        min_temp = 0
        date = ""
        first_date_check = False
        for line in response.json()['daily']:
            temp = line['temp']['night']
            feels_like = line['feels_like']['night']
            diff = abs(temp - feels_like)
            if min_temp > diff or first_date_check == False:
                min_temp = diff
                date = line['dt']
                first_date_check == True
        date = datetime.fromtimestamp(date).strftime('%d.%m.%Y')
        return "Минимальная разница между 'ощущаемой' и фактической температурами ночью равна %s градусов Цельсия. Дата: %s." %(min_temp, date)
            


    def get_max_length_of_sun(self):
        response = requests.get(self.URL)
        max_diff = 0
        date = ""
        first_check = False
        days = 0
        for line in response.json()['daily']:
            days += 1
            if days > 5:
                break
            diff = line['sunset'] - line['sunrise']
            if max_diff < diff or first_check == False:
                max_diff = diff
                date = line['dt']
                first_check = True
        max_diff = datetime.fromtimestamp(max_diff).strftime('%H:%M:%S')
        date = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
        return "Максимальная продолжительность светового дня за ближайшие 5 дней равна %s. Дата: %s."  %(max_diff, date)

token = input("Введите ваш токе OpenWeatherMap: ")
weather = Weather(token)

print("1. День, с минимальной разницей ощущаемой и фактической температуры ночью (с указанием разницы в градусах Цельсия).")
print("2. Максимальная продолжительность светового дня (считать, как разницу между временем заката и рассвета) за ближайшие 5 дней (включая текущий), с указанием даты.")
if (input("Введите номер запроса: ") == "1"):
    print(weather.get_min_temp_diff())
else:
    print(weather.get_max_length_of_sun())
