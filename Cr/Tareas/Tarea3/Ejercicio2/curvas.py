from EllipticCurve import EllipticCurve
from tools import table
import random

# Generamos la curva eliptica
p = 23
a = 1
b = 17
eli = EllipticCurve(p, a, b)

# Mostramos los puntos de la curva
"""
for punto in eli.points:
    print(punto)
"""

# Alfabeto
alfabeto = "abcdefghijklmnopqrstuvwxyz "

# Generamos la tabla de codificacion
tabla = table(eli, alfabeto)

# Mostramos la tabla de codificacion
"""
for key, value in tabla.items():
    print(f"\"{key}\" -> {value}")
"""

# Funcion para convertir una letra a un punto
def letra_a_punto(letra):
    return tabla[letra]

# Funcion para convertir un punto a una letra
def punto_a_letra(punto):
    for key, value in tabla.items():
        if value == punto:
            return key

# Funcion para cifrar una letra
def cifrar_letra(letra, g, p_x, curva):
    # Convertimos la letra a un punto
    p_m = letra_a_punto(letra)
    # Escogemos un k entero
    k = random.randint(1, curva.order(g) - 1)
    # Calculamos el par de puntos (kG, P_m + kP_a)
    punto1 = curva.mult(k, g)
    kp_a = curva.mult(k, p_x)
    punto2 = curva.sum(p_m, kp_a)
    # Regresamos el par de puntos
    return punto1, punto2

# Funcion para cifrar un mensaje
def cifrar_mensaje(mensaje, g, p_a, curva):
    # Inicializamos el mensaje cifrado
    mensaje_cifrado = ""
    # Ciframos cada letra del mensaje
    for letra in mensaje:
        punto1, punto2 = cifrar_letra(letra, g, p_a, curva)
        mensaje_cifrado += punto_a_letra(punto1) + punto_a_letra(punto2)
    return mensaje_cifrado

# Funcion para descifrar una letra
def descifrar_letra(punto1, punto2, n_x, curva):
    # Calculamos el punto mediante P_m + kP_a - n_a(kG)
    # Calculamos n_a(kG)
    parte1 = curva.mult(n_x, punto1)
    # Calculamos el inverso para restarlo
    parte1 = curva.inv(parte1)
    # Realizamos la suma
    suma = curva.sum(punto2, parte1)
    # Regresamos la letra
    return punto_a_letra(suma)

# Funcion para descifrar un mensaje
def descifrar_mensaje(mensaje, n_x, curva):
    # Inicializamos el mensaje descifrado
    mensaje_descifrado = ""
    # Desciframos cada letra del mensaje
    for i in range(0, len(mensaje), 2):
        punto1 = letra_a_punto(mensaje[i])
        punto2 = letra_a_punto(mensaje[i + 1])
        mensaje_descifrado += descifrar_letra(punto1, punto2, n_x, curva)
    return mensaje_descifrado

# Mensaje a cifrar
mensaje = "quiero vacaciones"

# Punto base G
g = eli.points[-1]

# Alicia llave privada n_a
n_a = 2

# Alicia llave publica P_a
p_a = eli.mult(n_a, g)

# Bob llave privada n_b
n_b = 3

# Bob llave publica P_b
p_b = eli.mult(n_b, g)

# Alicia calcula k
k_a = eli.mult(n_a, p_b)

# Bob calcula k
k_b = eli.mult(n_b, p_a)

if not k_a == k_b:
    print("Error en la generacion de k")
    exit()

# Mostramos el mensaje
print(f"Mensaje: {mensaje}")

# Ciframos el mensaje
mensaje_cifrado = cifrar_mensaje(mensaje, g, p_a, eli)

# Mostramos el mensaje cifrado
print(f"Mensaje cifrado: {mensaje_cifrado}")

# Desciframos el mensaje
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, n_a, eli)

# Mostramos el mensaje descifrado
print(f"Mensaje descifrado: {mensaje_descifrado}")
