# звено связывающие файлы

import reading_data
import print_all_data
import UI
import add_data
import logger



def button_click():
    UI.print_data("Вы можете выполнить следующие действия со списком: ")
    answer = UI.input_check_choice("1. Вывод всего телефонного справочника.\n2. Добавление нового номера\n Введите цифру: ")
    if answer == 1:
        list_data = reading_data.get_info("uses.csv")  # читаем
        print_all_data.print_all(list_data)  # печатаем все
        UI.print_data(f"\nТелефонный справочник состоит из {len(list_data)} записей")
    elif answer == 2:
        user_data = UI.input_phonebook()
        add_data.append_data("uses.csv", user_data)
        logger.result_loger(user_data)
        UI.print_data("\nДанные успешно добавлены в телефонный справочник.")