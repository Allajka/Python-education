# Модуль 1: сбор информации с датчиков
from random import randint

def get_temperature(sensor):  # температура
    return randint(-20,0) if sensor else randint(0, 20)


def get_pressure(sensor):  # давление
    return randint(720,750) if sensor else randint(750, 770)


def get_wind_speed(sensor):  # скорость
    return randint(0, 30) if sensor == 1 else randint(30, 50)

def data_collection(sensor = 1):  # будет собирать данные со всех датчиков и отдавать их одной порцией
    return (get_temperature(sensor), get_pressure(sensor), get_wind_speed(sensor))