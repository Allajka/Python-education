import print_all_data

def search_phone(data, search_data):
    search_data = search_data.replace(' ', '')
    counter = 0
    for row in data:
        temp = row.replace(' ', '')
        if search_data in temp:
            print(row)
            counter += 1
    if counter == 0:
        print("Номер телефона отсутствует в справочнике.")


def search_surname(data, search_data):
    search_data.title()
    for i in data:
        if search_data in i:
            print(i)
