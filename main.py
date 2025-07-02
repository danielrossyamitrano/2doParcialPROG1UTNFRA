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
from engine import agregar_letra, dibujar_cuerpo, elegir_palabra, mostrar_letras_adivinadas, verificar_letra
from engine import abrir_txt as cargar_palabras, cargar_imagen, cargar_musica, salir, detener_musica
from engine.constantes import ANCHO, ALTO, NEGRO, FUENTE_REPETIDA, ROJO
from pygame import init as pg_init, display, event, time, transform
from pygame.locals import *
from time import sleep
from os import path

pg_init()


# ------------------ FUNCION PRINCIPAL -------------------
def jugar(pantalla):
    imagen_fondo = cargar_imagen('fondo_final.png')  # Cargamos la imagen para el fondo del juego
    fondo_escalado = transform.scale(imagen_fondo, [800, 600])  # Escalamos la imagen al tamaño de la ventana
    pantalla.blit(fondo_escalado, (0, 0))

    cargar_musica('MusicaFondo.wav')  # Cargamos la musica de fondo

    # 1. Cargar palabras desde archivo y elegir una al azar
    palabras = cargar_palabras(path.join('palabras_programacion.txt'))  # Cargamos las palabras desde un archivo .txt
    elegida = elegir_palabra(palabras)  # Se elige una palabra al azar de esta lista de palabras
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
                        pantalla.fill(NEGRO)  # Pantalla en negro para mostrar el mensaje que perdiste

                        imagen_perdedor = cargar_imagen('you_died.png')  # Cargamos la imagen que avisa que perdiste
                        cargar_musica('risa_bruja_perdedor.mp3')  # Reproducimos el sonido del perdedor
                        img_perdedor_escalada = transform.scale(imagen_perdedor, (700, 200))
                        # Reescalamos la imagen para que entre bien en la pantall
                        rect = img_perdedor_escalada.get_rect(center=(ANCHO // 2, ALTO // 2))
                        # Creamos una superficie donde se va a mostrar la imagen

                        pantalla.blit(img_perdedor_escalada, rect)
                        detener_musica()
                        display.update()

                        sleep(6)
                        # Agregamos tiempo de espera antes de que se actualice la pantalla
                        # asi da teiempo al audio a reproducirse

                        corriendo = False

                    elif set(actual_word) <= set(adivinadas):
                        # Usamos set para verificar que todas las letras de la palabra fueron adivinadas,
                        # el set hace que no importe el orden de las letras y elimina las repetidas

                        pantalla.fill(NEGRO)  # Pantalla en negro para poner el mensaje ganador

                        imagen_ganador = cargar_imagen('Respect.png')  # Cargamos la imagen en una variable
                        cargar_musica('respect.mp3')  # Cargamos musica ganadora
                        img_ganador_escalada = transform.scale(imagen_ganador, (400, 300))
                        rect = img_ganador_escalada.get_rect(center=(ANCHO // 2, ALTO // 2))
                        # Armamos un rectangulo donde mostrar la imagen y la centramos
                        # para que quede en el medio de la pantalla

                        pantalla.blit(img_ganador_escalada, rect)  # Bliteamos la imagen en pantalla
                        detener_musica()
                        display.update()  # Actualizamos la pantalla

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
                                imagen, rect = dibujar_cuerpo(errores, gaturro)
                                # Bliteamos la imagen del cuerpo del personaje que corresponde
                                pantalla.blit(imagen, rect)
                                # 4.c- Incrementar errores si corresponde
                                errores += 1
                                # sumamos un error si la letra no está en la palabra

        if corriendo:
            mostrar_letras_adivinadas(pantalla, elegida, adivinadas)

        if mensaje:
            texto = FUENTE_REPETIDA.render(mensaje, True, ROJO)  # Color rojo
            rect = texto.get_rect(center=(ANCHO // 2, ALTO - 50))  # Abajo en el centro
            pantalla.blit(texto, rect)
            display.update()
            if sleep(2) is None:
                mensaje = ''
                eraser = fondo_escalado.subsurface(rect)
                pantalla.blit(eraser, rect)
                display.update()

        # 4.f- Actualizar pantalla
        display.update()


# Instrucción: este bloque debe ser completado por el estudiante según las consignas
# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
# jugar()

if __name__ == "__main__":
    # ----------------- CONFIGURACIÓN DE PANTALLA -----------------

    fondo = display.set_mode((ANCHO, ALTO))
    display.set_caption("Ahorcado 💀 by EL DREAM TEAM ⭐")  # Nombre del juego
    icono = cargar_imagen("gaturro.png")  # Icono del juego
    display.set_icon(icono)
    FPS = time.Clock()

    # ----------------- REESCALADO DE PARTES DEL CUERPO GATURRO -----------------
    gaturro = [  # Reescalamos las imageens de gaturro y guardamos en un diccionario
        {'imagen': transform.scale(cargar_imagen('Cabeza_4.png'), [100, 100]), 'rect': [350, 200]},
        {'imagen': transform.scale(cargar_imagen('Torso_5.png'), [100, 100]), 'rect': [350, 201]},
        {'imagen': transform.scale(cargar_imagen('Brazo_Derecho_6.png'), [100, 100]), 'rect': [350, 200]},
        {'imagen': transform.scale(cargar_imagen('Brazo_Izquierdo_1.png'), [100, 100]), 'rect': [349, 202]},
        {'imagen': transform.scale(cargar_imagen('Pierna_Derecha_3.png'), [100, 100]), 'rect': [349, 201]},
        {'imagen': transform.scale(cargar_imagen('Pierna_Izquierda_2.png'), [100, 100]), 'rect': [349, 200]},
    ]
    jugar(fondo)