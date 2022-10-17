# звено связывающие файлы

import UI
import user_answer


def button_click():
    UI.print_data("\nВы можете выполнить следующие действия со списком: ")
    answer = UI.input_check_choice(
        "1. Вывод всего телефонного справочника.\n2. Добавление нового номера\n3. Поиск информации\n4. Удаление информации\n5. Сохранить спровочник\n6. Выход\n Введите цифру: ",
        6)
    if answer == 1:
        user_answer.show_all()
        button_click()
    elif answer == 2:
        user_answer.add_new()
        button_click()
    elif answer == 3:
        user_answer.search()
        button_click()
    elif answer == 4:
        user_answer.deletion()
        button_click()
    elif answer == 5:
        user_answer.export_to()
        button_click()
    elif answer == 6:
        print()
