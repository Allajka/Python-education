# Модуль 3: UI
import data_provider as prov
import logger as log


def temperature_view(sensor):  # представление информации о температуре
    data = prov.get_temperature(sensor)  # получение информации о температуре
    log.temperature_logger(data)  # запись данных в файл
    return data


def pressure_view(sensor):  # представление информации о температуре
    data = prov.get_pressure(sensor)  # получение информации о давления
    log.pressure_logger(data)  # запись данных в файл
    return data


def wind_speed_view(sensor):  # представление информации о температуре
    data = prov.get_wind_speed(sensor)  # получение информации о скорости
    log.wind_speed_logger(data)  # запись данных в файл
    return data
