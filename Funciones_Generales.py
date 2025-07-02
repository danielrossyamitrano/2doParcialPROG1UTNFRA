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

    