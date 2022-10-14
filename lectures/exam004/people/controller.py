# звено связывающие файлы

import model
import view

def button_click():
    view.view_data("Информация о пользователях.")
    size = view.get_value("Информацию о скольки пользователях вы хотите увидеть? Введите число: ")
    for i in range(size):
        sex = model.sex()
        full_name = model.name(sex)
        view.view_data(f"{sex}, {full_name}")

