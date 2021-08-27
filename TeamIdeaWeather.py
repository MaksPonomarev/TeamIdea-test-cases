import requests
from datetime import datetime, timedelta

def min_temp_diff():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=56.55&lon=59.57&exclude=minutely,hourly&appid=*"
    response = requests.get(url)
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
    return "Минимальная разница между 'ощущаемой' и фактической температурами ночью равна %s градусов Цельсия. Дата: %s" %(min_temp, date)
        


def max_length_of_sun():
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=56.55&lon=59.57&exclude=minutely,hourly&appid=*"
    response = requests.get(url)
    max_diff = 0
    date = ""
    first_check = False
    days = 0
    for line in response.json()['daily']:
        diff = line['sunset'] - line['sunrise']
        if max_diff < diff or first_check == False:
            max_diff = diff
            date = line['dt']
            first_check = True
    max_diff = datetime.fromtimestamp(max_diff).strftime('%H:%M:%S')
    date = datetime.fromtimestamp(date).strftime('%Y-%m-%d')
    return "Максимальная продолжительность светового дня за ближайшие 5 дней равна %s. Дата: %s"  %(max_diff, date)

print(min_temp_diff())
print(max_length_of_sun())