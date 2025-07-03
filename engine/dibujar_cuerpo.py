from pygame import Surface

# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
def dibujar_cuerpo(errores:list, gaturro:list) -> Surface:
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    return gaturro[errores]['imagen'], gaturro[errores]['rect']