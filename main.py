# === PROYECTO FINAL - JUEGO DEL AHORCADO EN PYGAME ===
# Instrucciones:
# - Usar funciones, listas, diccionarios y archivos.
# - No usar clases ni programación orientada a objetos.
# - El juego debe leer palabras desde un archivo de texto externo (palabras.txt).
# - Mostrar la palabra oculta en pantalla, los intentos y las letras ingresadas.
# - Dibujar el muñeco del ahorcado a medida que se cometen errores (cabeza, cuerpo, brazos, piernas).
# - Mostrar mensaje final al ganar o perder.
# - Organizar el código con funciones bien nombradas.
# - El código debe estar comentado línea por línea.
# - Solo las partes del cuerpo deben contar como errores, no el soporte del ahorcado.

from pygame import SRCALPHA, init as pg_init, display, font, Surface, event, quit as pg_quit, time, image
from pygame.locals import *
from random import choice
from sys import exit
from funciones import abrir_txt as cargar_palabras
from os import path, getcwd

pg_init()

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------
ANCHO, ALTO = 800, 600
VENTANA = display.set_mode((ANCHO, ALTO))
#completar con nombre del equipo
display.set_caption("Ahorcado 💀 by EL DREAM TEAM ⭐")
icono = image.load("") # Agregar imagen para el icono del juego
display.set_icon(icono)

FPS = time.Clock()

# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# ----------------- FUENTE -----------------
FUENTE = font.SysFont(None, 48)


#-------------------Modelo de funciones, se deberan realizar en un archivo aparte
# Las funciones del personaje deben ser creadas y completadas por el equipo en un archivo aparte
# -------------------

# ----------------- CARGAR PALABRAS DESDE ARCHIVO -----------------
# def cargar_palabras():
#     # Leer las palabras desde un archivo de texto y devolver una lista
#     # Asegurate de tener un archivo llamado palabras.txt con una palabra por línea
#     pass

#IMPLEMENTADO: función funciones/util.abrir_txt()
#AUTOR: Daniel Rossy Amitrano


# ----------------- ELEGIR PALABRA AL AZAR -----------------
def elegir_palabra(lista_palabras):
    # Elegir una palabra aleatoria de la lista y convertirla a mayúsculas
    chosen = choice(lista_palabras)
    return chosen.upper()


# ----------------- DIBUJAR ESTRUCTURA DEL AHORCADO -----------------
# Joaco: No se que tanto utilizemos esta funcion, si pensabamos dibujar la estructura como parte del fondo
def dibujar_estructura():
    # Dibuja la base, palo y cuerda del ahorcado (no cuenta como error)
    pass


# ----------------- DIBUJAR PARTES DEL CUERPO -----------------

# Joaco: Decidamos si vamos a hacer que se acerque cada vez mas a la olla o lo que sea (baje la cuerda)
# o le agregamos partes del cuerpo como cualquier ahorcado
def dibujar_cuerpo(errores):
    cuerpo_personaje = Surface((200, 200), SRCALPHA)  # Crear superficie para el cuerpo del personaje
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    return cuerpo_personaje


# ----------------- DIBUJAR JUEGO EN PANTALLA -----------------
def dibujar_juego(palabra, letras_adivinadas, errores):
    # Llenar fondo, mostrar palabra oculta, letras ingresadas y dibujar estructura y cuerpo
    pass


# ----------------- VERIFICAR LETRA -----------------
#Desglocé la función en dos porque me parecía que tenía dos return values diferentes. (dani)
# Joaco: Me parecio mejor que tambien se muestre la lista de letras ya utilizadas,
# sobretodo las erradas, arme otra lista para eso


# def verificar_letra(letra: str, letras_adivinadas: list):
#     # Agregar la letra a letras_adivinadas si no estaba
#     if letra not in letras_adivinadas:
#         letras_adivinadas.append(letra)
#     return letras_adivinadas

def verificar_letra(letra: str, palabra: str, letras_adivinadas: list, letras_incorrectas: list):
    # Verifica que la letra no fue utilizada antes
    if letra in letras_adivinadas or letra in letras_incorrectas:
        print(f"La letra '{letra}' ya fue utilizada. Intente con otra.")
        return letras_adivinadas, letras_incorrectas

    # Si la letra esta en la palabra la agregamos a letras_adivinadas
    if letra in palabra:
        print(f"La Letra '{letra}' se encuentra en la palabra.")
        # AGREGAR SONIDO DE CELEBRACION
        letras_adivinadas.append(letra)
    else:
        # Si la letra no está en la palabra, la agregamos a letras_incorrectas
        print(f"La letra '{letra}' no se encuentra en la palabra.")
        #AGREGAR SONIDO DE ERROR
        letras_incorrectas.append(letra)

    return letras_adivinadas, letras_incorrectas


def agregar_letra(letra: str, palabra: str):
    # Retornar True si la letra está en la palabra, False si no
    return letra in palabra


# ----------------- SONIDO -----------------
# pygame.mixer.init()  # Inicializa el motor de sonido
# sonido_error = pygame.mixer.Sound("error.wav")  # Asegurate de tener este archivo sonido_acierto = pygame.mixer.Sound("")  # Mati hace magia y agrega el sonido de acierto

# ----------------- BUCLE PRINCIPAL -----------------
def jugar():
    # 1. Cargar palabras desde archivo y elegir una al azar
    palabras = cargar_palabras(path.join(getcwd(), 'data', 'palabras_programacion.txt'))
    elegida = choice(palabras)
    espacios = len(elegida)
    # 2. Inicializar estructuras necesarias: letras_adivinadas, errores, reloj, banderas
    adivinadas = []
    incorrectas = []
    errores = 0

    for pair in ('í', 'i'), ('ó', 'o'), ('á', 'a'), ('ú', 'u'), ('é', 'e'):
        # reemplaza las vocales con tílde porque en Pygame esos son dos teclas y requeriría un parser.
        actual_word = elegida.replace(*pair)

    # esto es porque al adivinar una letra se ocuan todos los epsacios que tienen la misma letra. Ademas, case sensitive
    actual_word = actual_word.replace('rr', 'r').replace('cc', 'c').replace('ll', 'l').lower()
    corriendo = True

    while corriendo:
        FPS.tick(60)  # 4.g- Controlar FPS
        # 3. Crear un bucle while que termine al cerrar el juego o al ganar/perder
        for e in event.get([KEYDOWN, QUIT]):  #4.a- Capturar eventos (teclas)
            if (e.type == KEYDOWN and e.key == K_ESCAPE) or e.type == QUIT:
                pg_quit()
                exit()
            elif KEYDOWN:
                letra = e.unicode
                if len(letra) == 1 and letra.isalpha():  # 4.b- Verificar letras
                    adivinadas, incorrectas = verificar_letra(letra, actual_word, adivinadas, incorrectas)
                    # 4.e- Verificar condiciones de fin (victoria o derrota)
                    if len(incorrectas) >= espacios:
                        print('Perdiste')
                        corriendo = False

                    elif adivinadas == espacios:
                        print('Ganaste')
                        corriendo = False

                    # 4.d- Dibujar estado del juego en pantalla
                    elif agregar_letra(letra, actual_word):
                        # dibujar la letra en todos los espacios que correspondan
                        pass

                    else:
                        # dibujar una parte del hangman
                        errores += 1  # 4.c- Incrementar errores si corresponde

        # 4.f- Actualizar pantalla
        display.update()


# Instrucción: este bloque debe ser completado por el estudiante según las consignas
# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
