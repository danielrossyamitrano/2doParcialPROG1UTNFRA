from .util import cargar_sonidos
from pygame import font, transform
from .util import cargar_imagen
# ----------------- CONFIGURACIÓN DE PANTALLA -----------------

ANCHO, ALTO = 800, 600
# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
NEGRO_TRANSPARENTE = (0, 0, 0, 0)  # Color
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# ----------------- SONIDOS ------------------
sonido_error = cargar_sonidos('Oof.mp3')  # Cargamos el sonido de error que elegimos
sonido_correcto = cargar_sonidos('correcto.mp3')  # Cargamos el sonido de acierto que elegimos

# ----------------- FUENTES -----------------
FUENTE = font.SysFont('Century', 48)
FUENTE_REPETIDA = font.SysFont('Century', 24)  # Fuente para mensajes repetidos

# ----------------- REESCALADO DE PARTES DEL CUERPO GATURRO -----------------
IMAGENES = [  # Reescalamos las imageens de gaturro y guardamos en un diccionario
    {'imagen': transform.scale(cargar_imagen('Cabeza_4.png'), [100, 100]), 'rect': [350, 200]},
    {'imagen': transform.scale(cargar_imagen('Torso_5.png'), [100, 100]), 'rect': [350, 201]},
    {'imagen': transform.scale(cargar_imagen('Brazo_Derecho_6.png'), [100, 100]), 'rect': [350, 200]},
    {'imagen': transform.scale(cargar_imagen('Brazo_Izquierdo_1.png'), [100, 100]), 'rect': [349, 202]},
    {'imagen': transform.scale(cargar_imagen('Pierna_Derecha_3.png'), [100, 100]), 'rect': [349, 201]},
    {'imagen': transform.scale(cargar_imagen('Pierna_Izquierda_2.png'), [100, 100]), 'rect': [349, 200]},
]