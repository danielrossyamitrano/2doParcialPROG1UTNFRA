from pygame import image, mixer
from pygame.mixer import music
from os import path, getcwd

def abrir_txt(filepath):
    with open(filepath, 'rt', encoding='utf-8') as file:
        lineas = [line.rstrip('\n') for line in file.readlines()]
    return lineas

def cargar_imagen(filename):
    filepath = path.join(getcwd(), 'data', 'imagenes',filename)
    if path.exists(filepath):
        imagen = image.load(filepath).convert_alpha()
        return imagen

def cargar_musica(filename):
    mixer.init()
    filepath = path.join(getcwd(), 'data', 'musica', filename)
    if path.exists(filepath):
        music.load(filepath)
    music.play(-1)