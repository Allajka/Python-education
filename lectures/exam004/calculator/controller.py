# звено связывающие файлы
# здесь мы создадим кнопку, которую пользователь сможет нажимать
import model
import view

def button_click():
    view.view_data("Программа сложения двух чисел.")
    model.init(view.get_value(), view.get_value())
    view.view_data("Сумма: ", model.amount("+"))
