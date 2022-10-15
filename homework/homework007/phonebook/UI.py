# Юзер-интерфейс, то что будет видеть пользователь, его взаимодействие с программой

def print_data(data):
    print(data)


def input_data(data):
    input(f"{data}")


def input_phonebook():
    phone = check_phone()
    surname = input("surname: ")
    name = input("name: ")
    patronymic = input("patronymic: ")
    return f"phone: +7 {phone} surname: {surname} name: {name} patronymic: {patronymic}"

def check_phone():
    flag = False
    while flag == False:
        phone = input("phone: +7 ")
        if phone.isdigit():
            flag = True
            return phone
        else:
            print("Некорректный ввод, повторите попытку.")

def input_check_choice(text):
    flag = False
    while flag == False:
        user_answer = input(text)
        try:
            int(user_answer)
            if 0 < int(user_answer) < 3:
                return int(user_answer)
            else:
                flag == False
        except ValueError:
            flag == False
