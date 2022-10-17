def search_phone(data, search_data):
    search_data = search_data.replace(' ', '')
    counter = 0
    for row in data:
        temp = row.replace(' ', '')
        if search_data in temp:
            print(f"Запись найдена: {row}")
            counter += 1
    if counter == 0:
        print("Номер телефона отсутствует в справочнике.")


def search_surname(data, search_data):
    search_data.title()
    counter = 0
    for i in data:
        if search_data in i:
            print(f"Запись найдена: {i}")
            counter += 1
    if counter == 0:
        print("Информация отсутствует")
