import logger


def delete_row(search, list_data):
    for i in range(len(list_data)):
        if search in list_data[i]:
            print(f"Удалена запись {list_data[i]}")
            logger.result_loger(f'Удаление {list_data[i]}')
            del list_data[i]
            return delete_row(search, list_data)
    return list_data

def delete_row_empty(list_data):
    if "" in list_data:
        list_data.remove("")
        return delete_row_empty(list_data)
    if '\n' in list_data:
        list_data.remove('\n')
        return delete_row_empty(list_data)
    return list_data
