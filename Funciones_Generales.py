from pygame import draw
import pygame

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


def elegir_palabra(lista_palabras):
    # Elegir una palabra aleatoria de la lista y convertirla a mayúsculas
    chosen = choice(lista_palabras)
    return chosen.upper()

def agregar_letra(letra: str, palabra: str):
    # Retornar True si la letra está en la palabra, False si no
    return letra in palabra

def mostrar_letras_adivinadas(pantalla, palabra_original, letras_adivinadas):
    cantidad_letras = len(palabra_original)
    espacio_entre_letras = 60
    y_linea = 530  # Altura de la línea base
    y_texto = 500  # Altura de la letra (un poco más arriba)
    ANCHO = 800
    BLANCO = (255, 255, 255)
    FUENTE = pygame.font.SysFont (None, 48)

    ancho_total = cantidad_letras * espacio_entre_letras
    x_inicio = (ANCHO - ancho_total) // 2

    for i, letra in enumerate(palabra_original):
        x = x_inicio + i * espacio_entre_letras

        # 1. Dibujar la línea base
        inicio_linea = (x, y_linea)
        fin_linea = (x + 40, y_linea)  # Línea de 40 píxeles de largo
        draw.line(pantalla, BLANCO, inicio_linea, fin_linea, 3)

        # 2. Normalizar la letra para comparación
        letra_normalizada = letra.lower()
        for tilde, sin_tilde in (('í','i'), ('ó','o'), ('á','a'), ('ú','u'), ('é','e')):
            letra_normalizada = letra_normalizada.replace(tilde, sin_tilde)
        for doble in (('rr','r'), ('ll','l'), ('cc','c')):
            letra_normalizada = letra_normalizada.replace(*doble)

        # 3. Si fue adivinada, dibujar la letra sobre la línea
        if letra_normalizada in letras_adivinadas:
            texto = FUENTE.render(letra.upper(), True, BLANCO)
            rect = texto.get_rect(center=(x + 20, y_texto))  # x + 20 centra la letra sobre la línea
            pantalla.blit(texto, rect)    