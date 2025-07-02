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

#---------------------------------------------------------------------------------
from funciones import abrir_txt as cargar_palabras, cargar_imagen, cargar_musica, cargar_sonidos, salir
from pygame import init as pg_init, display, font, event, time, draw, transform
from pygame.locals import *
from random import choice
from time import sleep
from os import path

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

# ----------------- FUENTES -----------------

FUENTE = font.SysFont('Century', 48)
FUENTE_REPETIDA = font.SysFont('Century', 24)  # Fuente para mensajes repetidos


#-------------------Modelo de funciones, se deberan realizar en un archivo aparte
# Las funciones del personaje deben ser creadas y completadas por el equipo en un archivo aparte
# -------------------

# ----------------- ELEGIR PALABRA AL AZAR -----------------

def elegir_palabra(lista_palabras):
    # Elegir una palabra aleatoria de la lista y convertirla a mayúsculas
    chosen = choice(lista_palabras)
    return chosen.upper()


# ----------------- DIBUJAR PARTES DEL CUERPO -----------------

def dibujar_cuerpo(errores, gaturro):
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    return gaturro[errores]['imagen'], gaturro[errores]['rect']


# ----------------- DIBUJAR LINEAS Y LETRAS EN PANTALLA -----------------

def mostrar_letras_adivinadas(pantalla, palabra_original, letras_adivinadas):
    cantidad_letras = len(palabra_original)
    espacio_entre_letras = 60  # Buscamos un espacion entre cada letra que se vea bien en pantalla
    y_linea = 530  # Le ponemos una altura a las lineas
    y_texto = 500  # Y aca a las letras que van apareciendo

    ancho_total = cantidad_letras * espacio_entre_letras  # Calculamos el ancho de toda la palabra
    x_inicio = (ANCHO - ancho_total) // 2  # Centramos la palabra en pantalla

    for i, letra in enumerate(
            palabra_original):  # Recorremos la palabra original y sacamos el indice y la letra con enumerate
        x = x_inicio + i * espacio_entre_letras  # Calculamos la posicion en x de cada letra

        draw.line(pantalla, BLANCO, (x, y_linea), (x + 40, y_linea), 3)  # Dibujamos la linea de cada letra

        letra_normalizada = letra.lower()  # Pasamos la letra a minuscula para una comparacion mas facik
        for tilde, sin_tilde in (('í', 'i'), ('ó', 'o'), ('á', 'a'), ('ú', 'u'), ('é', 'e')):
            letra_normalizada = letra_normalizada.replace(tilde, sin_tilde)
            # Eliminamos las tildes de las letras para que se puede comparar
        for doble in (('rr', 'r'), ('ll', 'l'), ('cc', 'c')):
            letra_normalizada = letra_normalizada.replace(*doble)  # Eliminamos las letras dobles por la misma razon

        if letra_normalizada in letras_adivinadas:  # Si esta la letra en las letras adivinadas
            texto = FUENTE.render(letra.upper(), True,
                                  BLANCO)  # Convertimos la letra a mayuscula y la mostramos en pantalla
            rect = texto.get_rect(center=(x + 20, y_texto))  # Acomodamos la letra sobre la linea
            pantalla.blit(texto, rect)


# ----------------- VERIFICAR LETRA -----------------

def verificar_letra(letra: str, palabra: str, letras_adivinadas: list, letras_incorrectas: list):
    if not (letra in letras_adivinadas and letra in letras_incorrectas):  # Verificamos si la letra ya no fue utilizada
        # mensaje_repetida = f"La letra '{letra}' ya fue utilizada"  # Mensaje si es que ya fue utilizada
        # return letras_adivinadas, letras_incorrectas, mensaje_repetida  #
        if letra in palabra:  # Si la letra esta en la palabra
            sonido_correcto.play()  # Reproducimos el sonido de acierto
            letras_adivinadas.append(letra)  # Y agregamos la letra a la lista de letras adivinadas
        else:  # Si la letra no esta en la palabra
            sonido_error.play()  #Reproducimos el sonido de error
            letras_incorrectas.append(letra)  # Y la agregamos a la lista de letras incorrectas

    return letras_adivinadas, letras_incorrectas


def agregar_letra(letra: str, palabra: str):
    # Retornar True si la letra está en la palabra, False si no
    return letra in palabra


# ----------------- SONIDOS ------------------

sonido_error = cargar_sonidos('Oof.mp3')  # Cargamos el sonido de error que elegimos
sonido_correcto = cargar_sonidos('correcto.mp3')  # Cargamos el sonido de acierto que elegimos

# ----------------- REESCALADO DE PARTES DEL CUERPO GATURRO -----------------

IMAGENES = [  # Reescalamos las imageens de gaturro y guardamos en un diccionario
    {'imagen': transform.scale(cargar_imagen('Cabeza_4.png'), [100, 100]), 'rect': [350, 200]},
    {'imagen': transform.scale(cargar_imagen('Torso_5.png'), [100, 100]), 'rect': [350, 201]},
    {'imagen': transform.scale(cargar_imagen('Brazo_Derecho_6.png'), [100, 100]), 'rect': [350, 200]},
    {'imagen': transform.scale(cargar_imagen('Brazo_Izquierdo_1.png'), [100, 100]), 'rect': [349, 202]},
    {'imagen': transform.scale(cargar_imagen('Pierna_Derecha_3.png'), [100, 100]), 'rect': [349, 201]},
    {'imagen': transform.scale(cargar_imagen('Pierna_Izquierda_2.png'), [100, 100]), 'rect': [349, 200]},
]


# ------------------ FUNCION PRINCIPAL -------------------

def jugar():
    fondo = cargar_imagen('FondoFinal.png')  # Cargamos la imagen para el fondo del juego
    fondo_escalado = transform.scale(fondo, [800, 600])  # Escalamos la imagen al tamaño de la ventana
    VENTANA.blit(fondo_escalado, (0, 0))

    cargar_musica('MusicaFondo.wav')  # Cargamos la musica de fondo

    # 1. Cargar palabras desde archivo y elegir una al azar
    palabras = cargar_palabras(path.join('palabras_programacion.txt'))  # Cargamos las palabras desde un archivo .txt
    elegida = choice(palabras)  # Se elige una palabra al azar de esta lista de palabras
    # espacios = len(elegida)  # Crea una lista con los espacios que tiene la palabra elegida
    # 2. Inicializar estructuras necesarias: letras_adivinadas, errores, reloj, banderas
    adivinadas = []  # Lista de letras adivinadas
    incorrectas = []  # Lista de letras incorrectas
    errores = 0  # Contador de errores

    for pair in ('í', 'i'), ('ó', 'o'), ('á', 'a'), ('ú', 'u'), ('é', 'e'):
        # reemplaza las vocales con tílde porque en Pygame esos son dos teclas y requeriría un parser.
        actual_word = elegida.replace(*pair)

    # esto es porque al adivinar una letra se ocupan todos los espacios que tienen la misma letra.
    # Ademas, python es case sensitive
    actual_word = actual_word.replace('rr', 'r').replace('cc', 'c').replace('ll', 'l').lower()
    corriendo = True
    mensaje = ""  # Inicializamos un mensaje vacío para mostrar si la letra ya fue utilizada

    while corriendo:
        FPS.tick(60)  # 4.g- Controlar FPS

        # VENTANA.blit(fondo_escalado, (0, 0))
        # Dibujamos el fondo en cada iteracion del bucle para que no se superpongan las imagenes y textos

        # 3. Crear un bucle while que termine al cerrar el juego o al ganar/perder
        for e in event.get([KEYDOWN, QUIT]):  #4.a- Capturar eventos (teclas)
            if (e.type == KEYDOWN and e.key == K_ESCAPE) or e.type == QUIT:
                salir()
            # imprimir las lineas de la palabra a adivinar

            elif e.type == KEYDOWN:
                letra = e.unicode
                if len(letra) == 1 and letra.isalpha():  # 4.b- Verificar letras
                    #adivinadas, incorrectas = verificar_letra(letra, actual_word, adivinadas, incorrectas)
                    if letra in adivinadas or letra in incorrectas:  # Verifica si la letra fue usada antes
                        mensaje = f"La letra '{letra}' ya fue utilizada. Intente con otra."
                        # Si fue utilizada antes mostramos el mensaje para que se sepa
                    else:
                        adivinadas, incorrectas = verificar_letra(letra, actual_word, adivinadas, incorrectas)
                        # Si no fue utilizada el mensaje no se muestra y verificamos si la letra esta en la palabra
                        mensaje = ""  # limpiar mensaje si la letra fue válida

                    # 4.e- Verificar condiciones de fin (victoria o derrota)
                    if len(incorrectas) > 6:  # Cuando se superan los 6 errores, perdes
                        VENTANA.fill(NEGRO)  # Pantalla en negro para mostrar el mensaje que perdiste

                        imagen_perdedor = cargar_imagen('you_died.png')  # Cargamos la imagen que avisa que perdiste
                        cargar_musica('risa_bruja_perdedor.mp3')  # Reproducimos el sonido del perdedor
                        img_perdedor_escalada = transform.scale(imagen_perdedor, (700, 200))
                        # Reescalamos la imagen para que entre bien en la pantall
                        rect = img_perdedor_escalada.get_rect(
                            center=(ANCHO // 2, ALTO // 2))  # Creamos una superficie donde se va a mostrar la imagen

                        VENTANA.blit(img_perdedor_escalada, rect)
                        # display.update()

                        sleep(6)
                        # Agregamos tiempo de espera antes de que se actualice la pantalla
                        # asi da teiempo al audio a reproducirse

                        corriendo = False

                    elif set(actual_word) <= set(adivinadas):
                        # Usamos set para verificar que todas las letras de la palabra fueron adivinadas,
                        # el set hace que no importe el orden de las letras y elimina las repetidas

                        VENTANA.fill(NEGRO)  # Pantalla en negro para poner el mensaje ganador

                        imagen_ganador = cargar_imagen('Respect.png')  # Cargamos la imagen en una variable
                        cargar_musica('respect.mp3')  # Cargamos musica ganadora
                        img_ganador_escalada = transform.scale(imagen_ganador, (400, 300))
                        rect = img_ganador_escalada.get_rect(center=(ANCHO // 2, ALTO // 2))
                        # Armamos un rectangulo donde mostrar la imagen y la centramos
                        # para que quede en el medio de la pantalla

                        VENTANA.blit(img_ganador_escalada, rect)  # Bliteamos la imagen en pantalla
                        # display.update()  # Actualizamos la pantalla

                        sleep(7.5)  # Agregamos tiempo de espera antes de que se actualice la pantalla
                        # asi da teiempo al audio a reproducirse

                        corriendo = False

                    # 4.d- Dibujar estado del juego en pantalla
                    elif not agregar_letra(letra, actual_word):
                        # dibujar la letra en todos los espacios que correspondan
                        if not mensaje:  # no se penaliza al jugador por elegir de nuevo una letra
                            # porque no se están mostrando las letras ya elegidas.
                            if errores <= 5:
                                # dibujar una parte del hangman
                                imagen, rect = dibujar_cuerpo(errores, IMAGENES)
                                # Bliteamos la imagen del cuerpo del personaje que corresponde
                                VENTANA.blit(imagen, rect)
                                # 4.c- Incrementar errores si corresponde
                                errores += 1
                                # sumamos un error si la letra no está en la palabra

        mostrar_letras_adivinadas(VENTANA, actual_word, adivinadas)
        if mensaje:
            texto = FUENTE_REPETIDA.render(mensaje, True, ROJO)  # Color rojo
            rect = texto.get_rect(center=(ANCHO // 2, ALTO - 50))  # Abajo en el centro
            VENTANA.blit(texto, rect)
            display.update()
            if sleep(2) is None:
                mensaje = ''
                eraser = fondo_escalado.subsurface(rect)
                VENTANA.blit(eraser, rect)
                display.update()

        # 4.f- Actualizar pantalla
        display.update()


# Instrucción: este bloque debe ser completado por el estudiante según las consignas
# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
