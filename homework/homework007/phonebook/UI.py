# Юзер-интерфейс, то что будет видеть пользователь, его взаимодействие с программой

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
        phone = input("phone: +7 ").replace(' ', '')
        if phone.isdigit() and len(phone) == 10:
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
