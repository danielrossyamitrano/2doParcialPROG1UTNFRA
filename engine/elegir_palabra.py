from random import choice

# ----------------- ELEGIR PALABRA AL AZAR -----------------
def elegir_palabra(lista_palabras:list) -> str:
    # Elegir una palabra aleatoria de la lista y convertirla a mayúsculas
    chosen = choice(lista_palabras)
    return chosen.upper()
