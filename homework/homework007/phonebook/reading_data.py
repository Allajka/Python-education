def get_info(name_file):
    with open(name_file, 'r') as file:
        info = file.read().split(",")
    return info
