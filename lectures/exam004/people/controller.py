# звено связывающие файлы

import model
import view

def button_click():
    view.view_data("Информация о пользователях.")
    size = view.get_value("Информацию о скольки пользователях вы хотите увидеть? Введите число: ")
    for i in range(size):
        sex = model.sex()
        surname, name, patronymic = model.surname(sex), model.name(sex), model.patronymic(sex)
        phone = model.phone()
        view.view_data(f" пол: {sex}; ФИО: {surname} {name} {patronymic}; номер телефона: {phone}")

        with open('uses.csv', 'a') as file:
            file.write('phone: {} '.format(phone))
            file.write('surname: {} '.format(surname))
            file.write('name: {} '.format(name))
            file.write('patronymic: {},'.format(patronymic))


        print("_______________________________________________________")

