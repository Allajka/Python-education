# звено связывающие файлы

import model
import view

def button_click():
    view.view_data("Информация о пользователях.")
    size = view.get_value("Информацию о скольки пользователях вы хотите увидеть? Введите число: ")
    for i in range(size):
        sex = model.sex()
        surname, name, patronymic = model.surname(sex), model.name(sex), model.patronymic(sex)
        birth, phone = model.date_birth(), model.phone()
        view.view_data(f"id: {i+1}; пол: {sex}; ФИО: {surname} {name} {patronymic};\n дата рождения: {birth}; номер телефона: {phone}")
        print("_______________________________________________________")

