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

from pygame import SRCALPHA, init as pg_init, display, font, Surface
from random import choice

# from funciones import abrir_txt
# from os import path, getcwd

# ruta = path.join(getcwd(), 'data', 'palabras_astronomia.txt')
# lineas = abrir_txt(ruta)


pg_init()

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------
ANCHO, ALTO = 800, 600
VENTANA = display.set_mode((ANCHO, ALTO))
#completar con nombre del equipo
display.set_caption("Juego del Ahorcado by El DREAM TEAM")

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
    cuerpo_personaje = Surface((200, 200), SRCALPHA) # Crear superficie para el cuerpo del personaje
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
    letras_incorrectas = []
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
# sonido_error = pygame.mixer.Sound("error.wav")  # Asegurate de tener este archivo
# sonido_acierto = pygame.mixer.Sound("")  # Mati hace magia y agrega el sonido de acierto

# ----------------- BUCLE PRINCIPAL -----------------
def jugar():
    # 1. Cargar palabras desde archivo y elegir una al azar
    # 2. Inicializar estructuras necesarias: letras_adivinadas, errores, reloj, banderas
    # 3. Crear un bucle while que termine al cerrar el juego o al ganar/perder
    # 4. Dentro del bucle:
    #     - Capturar eventos (teclas)
    #     - Verificar letras
    #     - Incrementar errores si corresponde
    #     - Dibujar estado del juego en pantalla
    #     - Verificar condiciones de fin (victoria o derrota)
    #     - Actualizar pantalla
    #     - Controlar FPS

    # Instrucción: este bloque debe ser completado por el estudiante según las consignas
    pass

# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
# jugar()