# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
from .constantes import IMAGENES

def dibujar_cuerpo(errores, gaturro):
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    return IMAGENES[errores]['imagen'], gaturro[errores]['rect']