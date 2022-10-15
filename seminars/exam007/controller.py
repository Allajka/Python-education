import UI
import logger
import database
from operations import new_sum, new_diff, multiplication, division
from database import x, y, init


def button_click():
    a = UI.input_data("Введите a: ")
    sign = UI.input_data("Введите знак операции: ")
    b = UI.input_data("Введите b: ")
    database.init(a, b)
    match sign:
        case "+":
            result = new_sum(database.x, database.y)
        case "-":
            result = new_diff(database.x, database.y)
        case "*":
            result = multiplication(database.x, database.y)
        case "/":
            result = division(database.x, database.y)
    UI.print_data(result)
    logger.result_loger(f"{database.x} {sign} {database.y} = {result}")


