def abrir_txt(filepath):
    with open(filepath, 'rt', encoding='utf-8') as file:
        lineas = [line.rstrip('\n') for line in file.readlines()]
    return lineas