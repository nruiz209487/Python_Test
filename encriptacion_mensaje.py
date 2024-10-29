
def encriptacion_mensaje(mensaje, clave):
    res = ""
    mensaje=mensaje.lower()
    abecedario = 'abcdefghijklmnopqrstuvwxyz'  
    for letra in mensaje:
        if letra in abecedario:
            indice = abecedario.index(letra)
            nuevo_indice = (indice + clave) % len(abecedario)
            res += abecedario[nuevo_indice]
    return res
