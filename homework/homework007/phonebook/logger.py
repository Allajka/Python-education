from datetime import datetime as dt

def result_loger(data):
    time = dt.now().strftime('%H:%M')
    with open("logbook.txt", 'a', encoding='utf-8') as file:
        file.write(f'{time}: new entry: {data}\n')