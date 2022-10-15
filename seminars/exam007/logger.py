from datetime import datetime as dt

def result_loger(data):
    time = dt.now().strftime('%H:%M')
    with open('output.txt', 'a') as file:
        file.write(f'{time}: expression: {data}\n')
