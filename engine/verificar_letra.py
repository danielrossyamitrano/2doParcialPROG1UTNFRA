# ----------------- VERIFICAR LETRA -----------------
from .constantes import sonido_error, sonido_correcto

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
