from pygame import image, mixer, quit, Surface
from pygame.mixer import music, Sound
from os import path, getcwd
from sys import exit


def abrir_txt(filename: str) -> list:
    filepath = path.join(getcwd(), 'data', 'palabras', filename)  # cra un string con la ruta al archivo
    if path.exists(filepath):  # verifica que la ruta exista.
        with open(filepath, 'rt', encoding='utf-8') as file:
            lineas = [line.rstrip('\n') for line in file.readlines()]
        return lineas


def cargar_imagen(filename: str) -> Surface:
    filepath = path.join(getcwd(), 'data', 'imagenes', filename)  # cra un string con la ruta al archivo
    if path.exists(filepath):  # verifica que la ruta exista.
        imagen = image.load(filepath).convert_alpha()
        return imagen


def cargar_musica(filename: str) -> None:
    mixer.init()
    filepath = path.join(getcwd(), 'data', 'audio', 'musica', filename)  # cra un string con la ruta al archivo
    if path.exists(filepath):  # verifica que la ruta exista.
        music.load(filepath)  # carga la canción
        music.set_volume(1)  # subí el volumen de la musica porque yo apenas lo escucho.
    music.play(-1)  # comienza a reproducir la canción, con un loop infinito.


def cargar_sonidos(filename: str) -> Sound:
    filepath = path.join(getcwd(), 'data', 'audio', 'sounds', filename)  # cra un string con la ruta al archivo
    if path.exists(filepath):  # verifica que la ruta exista.
        sonido = Sound(filepath)  # inicializa el sonido
        sonido.set_volume(0.3)  # Bajamos el volumen del sonido porque el audio original es muy fuerte)
        return sonido  # devolvmeos el sonido


def salir() -> None:
    # unifica las funciones de para salir del programa.
    quit()
    exit()


def detener_musica() -> None:
    music.stop()


__all__ = [
    'salir',
    'cargar_sonidos',
    'cargar_imagen',
    'cargar_musica',
    'abrir_txt',
    'detener_musica'
]
