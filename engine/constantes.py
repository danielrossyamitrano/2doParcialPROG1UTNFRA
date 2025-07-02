from .util import cargar_sonidos
from pygame import font, transform, mixer
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
mixer.init()
sonido_error = cargar_sonidos('Oof.mp3')  # Cargamos el sonido de error que elegimos
sonido_correcto = cargar_sonidos('correcto.mp3')  # Cargamos el sonido de acierto que elegimos

# ----------------- FUENTES -----------------
font.init()
FUENTE = font.SysFont('Century', 48)
FUENTE_REPETIDA = font.SysFont('Century', 24)  # Fuente para mensajes repetidos

