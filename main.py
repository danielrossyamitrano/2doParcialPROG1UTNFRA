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

from pygame import SRCALPHA, init as pg_init, display, font, Surface, event, quit as pg_quit, time, draw, transform
from funciones import abrir_txt as cargar_palabras, cargar_imagen, cargar_musica
from pygame.locals import *
from os import path, getcwd
from random import choice
from sys import exit
from time import sleep

pg_init()

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------
ANCHO, ALTO = 800, 600
VENTANA = display.set_mode((ANCHO, ALTO))

display.set_caption("Ahorcado 💀 by EL DREAM TEAM ⭐")  # Nombre del juego
icono = cargar_imagen("gaturro.png")  # Icono del juego
display.set_icon(icono)

FPS = time.Clock()

# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NEGRO_TRANSPARENTE = (0, 0, 0, 0)  # Color
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
def dibujar_cuerpo(errores, gaturro):
    # cuerpo_personaje = Surface((200, 200), SRCALPHA)  # Crear superficie para el cuerpo del personaje
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    return gaturro[errores]['imagen'], gaturro[errores]['rect']


# ----------------- DIBUJAR JUEGO EN PANTALLA -----------------
# def dibujar_juego(palabra, letras_adivinadas, errores):
#     # Llenar fondo, mostrar palabra oculta, letras ingresadas y dibujar estructura y cuerpo
#     pass

def dibujar_lineas(pantalla, palabra_elegida: str):
    fondo_palabra = Surface((740, 150), SRCALPHA)
    fondo_palabra.fill(NEGRO_TRANSPARENTE)

    cantidad_letras = len(palabra_elegida)
    espacio_entre_lineas = 60
    largo_linea = 40

    # Ancho total ocupado por todas las líneas
    ancho_total = cantidad_letras * espacio_entre_lineas

    # Calcular el punto de inicio en X para centrar
    x_inicio = (fondo_palabra.get_width() - ancho_total) // 2

    for i in range(cantidad_letras):
        x = x_inicio + i * espacio_entre_lineas
        draw.line(fondo_palabra, BLANCO, (x, 100), (x + largo_linea, 100), 4)

    pantalla.blit(fondo_palabra, (30, 440))  # Posición en pantalla


# ----------------- VERIFICAR LETRA -----------------
#Desglocé la función en dos porque me parecía que tenía dos return values diferentes. (dani)
# Joaco: Me parecio mejor que tambien se muestre la lista de letras ya utilizadas,
# sobretodo las erradas, arme otra lista para eso

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
# sonido_error = pygame.mixer.Sound("error.wav")  # Asegurate de tener este archivo 
# sonido_acierto = pygame.mixer.Sound("")  # Mati hace magia y agrega el sonido de acierto
# sonido_muerte = pygame.mixer.Sound("")
# sonido_ganador = pygame.mixer.Sound("")

# ----------------- BUCLE PRINCIPAL -----------------

IMAGENES = [
    {'imagen': transform.scale(cargar_imagen('Cabeza_4.png'), [100, 100]), 'rect': [350, 200]},
    {'imagen': transform.scale(cargar_imagen('Torso_5.png'), [100, 100]), 'rect': [350, 201]},
    {'imagen': transform.scale(cargar_imagen('Brazo_Derecho_6.png'), [100, 100]), 'rect': [350, 200]},
    {'imagen': transform.scale(cargar_imagen('Brazo_Izquierdo_1.png'), [100, 100]), 'rect': [349, 202]},
    {'imagen': transform.scale(cargar_imagen('Pierna_Derecha_3.png'), [100, 100]), 'rect': [349, 201]},
    {'imagen': transform.scale(cargar_imagen('Pierna_Izquierda_2.png'), [100, 100]), 'rect': [349, 200]},
]


def jugar():
    fondo = cargar_imagen('FondoFinal.png')
    fondo_escalado = transform.scale(fondo, [800, 600])
    VENTANA.blit(fondo_escalado, (0, 0))

    cargar_musica('MusicaFondo.wav')

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
    dibujar_lineas(VENTANA, elegida)
    while corriendo:
        FPS.tick(60)  # 4.g- Controlar FPS
        # 3. Crear un bucle while que termine al cerrar el juego o al ganar/perder
        for e in event.get([KEYDOWN, QUIT]):  #4.a- Capturar eventos (teclas)
            if (e.type == KEYDOWN and e.key == K_ESCAPE) or e.type == QUIT:
                pg_quit()
                exit()
            # imprimir las lineas de la palabra a adivinar

            elif e.type == KEYDOWN:
                letra = e.unicode
                if len(letra) == 1 and letra.isalpha():  # 4.b- Verificar letras
                    adivinadas, incorrectas = verificar_letra(letra, actual_word, adivinadas, incorrectas)
                    # 4.e- Verificar condiciones de fin (victoria o derrota)
                    if len(incorrectas) > 6:
                        print('Perdiste')
                        sleep(3)
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
                        if errores <= 5:
                            imagen, rect = dibujar_cuerpo(errores, IMAGENES)
                            VENTANA.blit(imagen, rect)
                            errores += 1  # 4.c- Incrementar errores si corresponde

        # 4.f- Actualizar pantalla
        display.update()


# Instrucción: este bloque debe ser completado por el estudiante según las consignas
# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
