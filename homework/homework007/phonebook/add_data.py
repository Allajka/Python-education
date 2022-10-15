

def append_data(name_file, data):
    with open(name_file, 'a') as file:
        file.write(f"{data},")


