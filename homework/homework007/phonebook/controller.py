# звено связывающие файлы

import UI
import user_answer


def button_click():
    UI.print_data("Вы можете выполнить следующие действия со списком: ")
    answer = UI.input_check_choice(
        "1. Вывод всего телефонного справочника.\n2. Добавление нового номера\n3. Поиск информации\n4. Удаление информации\n Введите цифру: ",
        4)
    if answer == 1:
        user_answer.show_all()
    elif answer == 2:
        user_answer.add_new()
    elif answer == 3:
        user_answer.search()
    elif answer == 4:
        user_answer.deletion()
