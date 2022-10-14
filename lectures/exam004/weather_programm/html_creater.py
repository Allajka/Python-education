# Модуль 4: HTML-генератор
from user_interface import temperature_view as t_view
from user_interface import wind_speed_view as speed_view
from user_interface import pressure_view as pres_view


# Пишем сами, но чаще всего для этого используют готовые библиотеки
# с какого устройства будем получать данные, для наглядности если с одного данные будут отрицательные и наоборот
def create(device=1):
    style = 'style="font-size:30px;"'  # явно описываем шрифт
    html = '<html>\n  <head></head>\n  <body>\n'  # заготовка для html представления
    html += '    <p {}>Temperature: {} c</p>\n' \
        .format(style, t_view(device))  # строка, которая форматируется, значения из user_interface
    html += '    <p {}>Wind_speed: {} m/s</p>\n' \
        .format(style, speed_view(device))
    html += '    <p {}>Pressure: {} mmHg</p>\n' \
        .format(style, pres_view(device))
    html += '  </body>\n</html>'

    with open('index.html', 'w') as page:  # создаем файл и просто его сохраняем
        page.write(html)

    return html


def new_create(data, device=1):
    t, p, w = data
    style = 'style="font-size:30px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>Temperature: {} c</p>\n' \
        .format(style, t)
    html += '    <p {}>Wind_speed: {} m/s</p>\n' \
        .format(style, w)
    html += '    <p {}>Pressure: {} mmHg</p>\n' \
        .format(style, p)
    html += '  </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data
