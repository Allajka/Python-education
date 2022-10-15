# Модуль 2: логирование
from datetime import datetime as dt


def temperature_logger(data):  # температура
    time = dt.now().strftime('%H:%M')  # маска для вывода
    with open('log.csv', 'a')  as file: # открытие для добавления данных
        file.write('{};temperature;{}\n'
                   .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M')  # маска для вывода
    with open('log.csv', 'a')  as file: # открытие для добавления данных
        file.write('{};pressure;{}\n'
                   .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M')  # маска для вывода
    with open('log.csv', 'a')  as file: # открытие для добавления данных
        file.write('{};wind_speed;{}\n'.format(time, data))