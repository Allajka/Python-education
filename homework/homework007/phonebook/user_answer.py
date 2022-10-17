import reading_data
import print_all_data
import add_data
import logger
import search_data
import deletion_data
import UI


def show_all():
    list_data = reading_data.get_info('uses.csv')
    print_all_data.print_all(list_data)
    UI.print_data(f"\nТелефонный справочник состоит из {len(list_data)} записей")
    logger.result_loger(f'Запрос на вывод информации')


def add_new():
    user_data = UI.input_phonebook()
    add_data.append_data("uses.csv", user_data)
    logger.result_loger(f'Новая запись {user_data}')
    UI.print_data("\nДанные успешно добавлены в телефонный справочник.")


def search():
    list_data = reading_data.get_info('uses.csv')
    UI.print_data("\nВам необходимо найти:")
    answer = UI.input_check_choice("1. Номер телефона\n2. Фамилию, Имя, Отчество\n Введите цифру: ", 2)
    if answer == 1:
        phone = UI.check_phone_search()
        search_data.search_phone(list_data, phone)
        logger.result_loger(f'Запрос на поиск {phone}')
    elif answer == 2:
        surname = UI.check_full_name("surname: ")
        search_data.search_surname(list_data, surname)
        logger.result_loger(f'Запрос на поиск {surname}')


def deletion():
    list_data = reading_data.get_info('uses.csv')
    UI.print_data("\nВы можете удалить запись по номеру телефона.")
    phone = UI.check_phone()
    list_data = deletion_data.delete_row(phone, list_data)
    list_data = deletion_data.delete_row_empty(list_data)
    add_data.overwriting('uses.csv', list_data)


def export_to():
    UI.print_data("\nВыберите формат:")
    answer = UI.input_check_choice("1. txt\n2. csv \n3. XML \n", 3)
    if answer == 1:
        add_contact_by_txt()
    elif answer == 2:
        add_contact_by_csv()
    elif answer == 3:
        add_contact_by_XML()


def add_contact_by_txt():
    list_data = reading_data.get_info('uses.csv')
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for i in list_data:
            file.write(f'{i},')
            file.write('\n')

def add_contact_by_csv():
    list_data = reading_data.get_info('uses.csv')
    with open('phonebook.csv', 'a', encoding='utf-8') as file:
        for i in list_data:
            file.write(f'{i},')
            file.write('\n')

def add_contact_by_csv():
    list_data = reading_data.get_info('uses.csv')
    with open('phonebook.csv', 'a', encoding='utf-8') as file:
        for i in list_data:
            file.write(f'{i},')
            file.write('\n')

def add_contact_by_XML():
    list_data = reading_data.get_info('uses.csv')
    with open('phonebook.XML', 'a', encoding='utf-8') as file:
        for i in list_data:
            file.write(f'{i},')
            file.write('\n')
