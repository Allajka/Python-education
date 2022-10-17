# Юзер-интерфейс, то что будет видеть пользователь, его взаимодействие с программой
import reading_data
import print_all_data
import add_data
import logger
import search

def print_data(data):
    print(data)


def input_data(data):
    input(f"{data}")


def input_phonebook():
    phone = check_phone()
    surname = check_full_name("surname: ")
    name = check_full_name("name: ")
    patronymic = check_full_name("patronymic: ")
    return f"phone: +7 {phone} surname: {surname} name: {name} patronymic: {patronymic}"


def check_full_name(text):
    flag = False
    while flag == False:
        data = input(f"{text} ")
        if data.isalpha():
            flag = True
            return data.title()
        else:
            print("Некорректный ввод, повторите попытку.")


def check_phone():
    flag = False
    while flag == False:
        phone = input("phone: +7 ")
        temp = phone.replace(' ', '')
        if temp.isdigit() and len(temp) == 10:
            flag = True
            return phone
        else:
            print("Некорректный ввод, повторите попытку.")


def input_check_choice(text, control_numbers):
    flag = False
    while flag == False:
        user_answer = input(text)
        try:
            int(user_answer)
            if 0 < int(user_answer) <= control_numbers:
                return int(user_answer)
            else:
                print("Некорректный ввод, повторите попытку.")
                flag == False
        except ValueError:
            flag == False


def answer(number):
    if number == 1:
        list_data = reading_data.get_info('uses.csv')
        print_all_data.print_all(list_data)
        print_data(f"\nТелефонный справочник состоит из {len(list_data)} записей")
        logger.result_loger(f'Запрос на вывод информации')
    elif number == 2:
        user_data = input_phonebook()
        add_data.append_data("uses.csv", user_data)
        logger.result_loger(f'Новая запись {user_data}')
        print_data("\nДанные успешно добавлены в телефонный справочник.")
    elif number == 3:
        list_data = reading_data.get_info('uses.csv')
        print_data("\nВам необходимо найти:")
        answer = input_check_choice("1. Номер телефона\n2. Фамилию, Имя, Отчество\n Введите цифру: ", 2)
        if answer == 1:
            phone = check_phone()
            search.search_phone(list_data, phone)
            logger.result_loger(f'Запрос на поиск {phone}')
        elif answer == 2:
            surname = check_full_name("surname: ")
            search.search_surname(list_data, surname)
            logger.result_loger(f'Запрос на поиск {surname}')