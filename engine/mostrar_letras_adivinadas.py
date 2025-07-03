from .constantes import ANCHO, BLANCO, FUENTE
from pygame import draw, Surface
# ----------------- DIBUJAR LINEAS Y LETRAS EN PANTALLA -----------------

def mostrar_letras_adivinadas(pantalla:Surface, palabra_original:str, letras_adivinadas:list) -> None:
    cantidad_letras = len(palabra_original)
    espacio_entre_letras = 60  # Buscamos un espacion entre cada letra que se vea bien en pantalla
    y_linea = 530  # Le ponemos una altura a las lineas
    y_texto = 500  # Y aca a las letras que van apareciendo

    ancho_total = cantidad_letras * espacio_entre_letras  # Calculamos el ancho de toda la palabra
    x_inicio = (ANCHO - ancho_total) // 2  # Centramos la palabra en pantalla

    for i, letra in enumerate(palabra_original):
        # Recorremos la palabra original y sacamos el indice y la letra con enumerate
        x = x_inicio + i * espacio_entre_letras  # Calculamos la posicion en x de cada letra
        # x_inicio es el inicio de la palabra y i * espacio_entre_letras es el espacio entre cada letra

        draw.line(pantalla, BLANCO, (x, y_linea), (x + 40, y_linea), 3)  # Dibujamos la linea de cada letra

        letra_normalizada = letra.lower()  # Pasamos la letra a minuscula para una comparacion mas facik
        for tilde, sin_tilde in (('í', 'i'), ('ó', 'o'), ('á', 'a'), ('ú', 'u'), ('é', 'e')):
            letra_normalizada = letra_normalizada.replace(tilde, sin_tilde)
            # Eliminamos las tildes de las letras para que se puede comparar
        for doble in (('rr', 'r'), ('ll', 'l'), ('cc', 'c')):
            letra_normalizada = letra_normalizada.replace(*doble)  # Eliminamos las letras dobles por la misma razon

        if letra_normalizada in letras_adivinadas:  # Si esta la letra en las letras adivinadas
            texto = FUENTE.render(letra.upper(), True, BLANCO)
            # Convertimos la letra a mayuscula y la mostramos en pantalla
            rect = texto.get_rect(center=(x + 20, y_texto))  # Acomodamos la letra sobre la linea
            pantalla.blit(texto, rect)
