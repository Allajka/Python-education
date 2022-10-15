import controller
import UI

flag = False
while flag == False:
    try:
        controller.button_click()
    except:
        flag = True
        UI.print_data("Введены неверные значения")
