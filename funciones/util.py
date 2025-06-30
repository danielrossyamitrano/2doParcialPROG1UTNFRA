from pygame import image
from os import path

def abrir_txt(filepath):
    with open(filepath, 'rt', encoding='utf-8') as file:
        lineas = [line.rstrip('\n') for line in file.readlines()]
    return lineas

def cargar_imagen(ruta):
    if path.exists(ruta):
        imagen = image.load(ruta).convert_alpha()
        return imagen