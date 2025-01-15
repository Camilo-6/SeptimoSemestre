from EllipticCurve import EllipticCurve
from Point import Point
from tools import table
from des import hex_a_bin, cifrar, descifrar
from colorama import Fore, Back, Style
import random

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

# Generamos la curva eliptica
p = 23
a = 1
b = 17
eli = EllipticCurve(p, a, b)

# Alfabeto
alfabeto = "abcdefghijklmnopqrstuvwxyz "

# Tabla de codificación
tabla = table(eli, alfabeto)

# Punto base G
g = eli.points[-1]

# Alicia llave privada n_a
n_a = 2
# Bob llave privada n_b
n_b = 3

# Alicia llave publica
p_a = eli.mult(n_a,g)
# Bob llave publica
p_b = eli.mult(n_b,g)

# Alicia calcula k
k_a = eli.mult(n_a, p_b)

# Bob calcula k
k_b = eli.mult(n_b, p_a)

assert k_a == k_b

k = k_a or k_b

acuerdo = "te enviare un mensaje cifrado con des " \
"utiliza la llave conjunta k para poder descifrar el mensaje " \
"lo que debes hacer es obtener el hash del punto k usando sha doscientos cincuenta y seis " \
"y obtener los primeros ocho caracteres del hash los conviertes a su " \
"representacion binaria y esta sera la llave para descifrar el mensaje"

# Ciframos el mensaje
acuerdo_cifrado = cifrar_mensaje(acuerdo, g, p_b, eli)
# Desciframos el mensaje
acuerdo_descifrado = descifrar_mensaje(acuerdo_cifrado, n_b, eli)
# Suponiendo que se usa sha256 para obtener el hash del punto y se obtiene los
# primeros 8 caracteres en su representación binaria
bits = ''.join(format(byte, '08b') for byte in str((k.x,k.y)).encode('utf-8'))
# Rellenamos hasta completar 64 bits
llave_des = bits.ljust(64, '0')
# Mensaje a enviar
mensaje = 'lunes'
mensaje_cifrado = cifrar(mensaje, llave_des)
mensaje_descifrado = descifrar(mensaje_cifrado, llave_des)

# Colores
rojo = Fore.RED
verde = Fore.GREEN
azul = Fore.BLUE
amarillo = Fore.YELLOW
reset = Fore.RESET

print("""
Supongamos que Alice quiere enviar a Bob la palabra secreta ”lunes”. Alice y Bob
escogen un entero positivo p que sea primo o un entero de la forma 2^m y eligen
una curva elíptica con parámetros a y b: Ep(a,b).

    p = {}
    a = {}
    b = {}

La curva elíptica es la siguiente:

    {}

Los puntos de la curva son los siguientes: 

{}

Son suficientes puntos de la curva para mapear el siguiente alfabeto:

    {}

Alice y Bob escojen un punto base G = (x_1,y_1) en Ep(a,b). El punto base es el siguiente:

    G = {}

Alicia y Bob seleccionan un número privado n_a, n_b respectivamente:

    n_a = {}
    n_b = {}

Alicia calcula su llave pública P_a = n_a * G

    P_a = {} * {} = {}

Bob calcula su llave pública P_b = n_b * G

    P_b = {} * {} = {}

Alicia y Bob intercambian su llave pública de manera que cada uno puede calcular
la llave conjunta k de manera que n_a * P_b = k = n_b * P_a:

    Alicia calcula k = {} * {} = {}
    Bob calcula    k = {} * {} = {}

Como podemos ver, ambos llegan al mismo punto de la curva, este punto es la 
llave conjunta. Ahora deben de ponerse de acuerdo para decidir que el cifrado
será DES y cómo usar la llave conjunta para cifrar y descifrar el mensaje.
Alice comunica a Bob el siguiente acuerdo cifrado con curvas elípticas:

Acuerdo: {}
      
Acuerdo cifrado: {}
      
Bob recibe el acuerdo y lo descifra, esto puede hacerlo fácilmente usando
su llave privada:
      
Acuerdo descifrado: {}
      
Alicia utiliza la llave conjunta G para poder cifrar el mensaje "lunes" convirtiendo
la llave conjunta en un hash usando sha256 y obtiene la representación binaria de los primeros
8 caracteres del hash, esta será nuestra llave para DES:
      
    Llave para DES: {}
      
Alicia cifra el mensaje y se lo manda a Bob
      
    Mensaje cifrado: {}
      
Bob recibe el mensaje y lo descifra usando la llave conjunta como se 
describe en el acuerdo.
      
    Mensaje descifrado: {}

""".format(
    p,
    a,
    b,
    eli,
    eli.points,
    alfabeto,
    g,
    n_a,
    n_b,
    n_a, g, p_a,
    n_b, g, p_b,
    n_a, p_b, k_a,
    n_b, p_a, k_b,
    acuerdo,
    acuerdo_cifrado,
    acuerdo_descifrado,
    llave_des,
    mensaje_cifrado,
    mensaje_descifrado
))
