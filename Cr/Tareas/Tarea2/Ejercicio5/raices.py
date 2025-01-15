import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../Ejercicio3'))
from simbolos import jacobi, descomponer
from poli import mod_poli
import random

# Algoritmo para encontrar la raiz cuadrado modulo p, p primo
def raiz_cuadrada_p(a, p):
    if not es_primo(p):
        raise ValueError(f"{p} no es primo")
    if a < 0 or a >= p:
        a = a % p
    if p == 2:
        raise ValueError(f"{p} no es impar")
    # Paso 1, sacar el simbolo de Legendre de a/p
    s = jacobi(a, p)
    # Paso 1, si s = -1, no existe la raiz cuadrada, regresamos a
    if s == -1:
        #return a
        raise ValueError(f"No existe la raiz cuadrada de {a} modulo {p}")
    # Paso 2, seleccionar un entero b, tal que 1 <= b < p y el simbolo de Legendre de b/p = -1
    b = 1
    while jacobi(b, p) != -1:
        b = random.randint(1, p - 1)
    # Paso 3, buscar un s tal que p-1 = 2^s * t, con t impar y s >= 1
    s, t = descomponer(p - 1)
    # Paso 4, encontrar a^-1 mod p
    a_inv = inverso(a, p)
    # Paso 5, calculamos c = b^t mod p
    c = pow(b, t, p)
    # Paso 5, calculamos r = a^((t+1)/2) mod p
    exp = (t + 1) // 2
    r = pow(a, exp, p)
    # Paso 6, iterar i de 1 a s-1
    for i in range(1, s):
        # Paso 6.1, calculamos d = (r^2 * a^-1)^2^(s-i-1) mod p
        exp = pow(2, s - i - 1)
        interno = pow(r, 2, p) * a_inv
        d = pow(interno, exp, p)
        # Paso 6.2, si d es congruente con -1 mod p, hacemos r = r * c mod p
        if d % p == p - 1:
            r = (r * c) % p
        # Paso 6.3, calculamos c = c^2 mod p
        c = pow(c, 2, p)
    # Paso 7, regresamos r mod p y -r mod p
    return (r % p, (-r) % p)

# Funcion para ver si un numero es primo
def es_primo(n):
    # Encontramos los primos menores o iguales a n
    primos = primos_menores_iguales(n)
    # Si el numero es primo, regresamos True
    return n in primos

# Funcion para encontrar los primos menores o iguales a n, Criba de Eratostenes
def primos_menores_iguales(n):
    # Paso 1, creamos una lista de booleanos de tamaño n
    primos = [True] * (n + 1)
    # Paso 2, iteramos sobre los numeros menores a n
    for i in range(2, n + 1):
        # Paso 2.1, si el numero es primo
        if primos[i]:
            # Paso 2.1.1, marcamos los multiplos de i como no primos
            for j in range(i * i, n + 1, i):
                primos[j] = False
    # Paso 3, regresamos los numeros primos
    return [i for i in range(2, n + 1) if primos[i]]

def mcd(a,b):
    """
    Regresa el maximo comun divisor de dos numeros.
    """
    while b != 0:
        a = a % b
        # Swap
        aux = a
        a = b
        b = aux
    return a

def reduce(x,n):
    """
    Regresa un numero reducido a modulo n
    """
    negativo = x < 0
    numero_reducido = abs(x) % n
    return n - numero_reducido if negativo else numero_reducido

def euclides_extendido(a, b):
    """
    Regresa el maximo comun divisor de 'a' y 'b' junto con los coeficientes de la combinación lineal. 
    """
    # Combinacion lineal
    # r = sa + tb
    s_0 = 1     # Coeficiente s
    s_1 = 0     # Carga con el divisor
    t_0 = 0     # Coeficiente t
    t_1 = 1     # Carga con el dividendo
    while b != 0:
        # Algoritmo de la division
        # a = bq + r
        q = int(a / b)  # Cociente
        r = a % b       # Residuo
        # Swap
        a = b
        b = r
        # Actualizamos los coeficientes s y t (Swap)
        s_0, s_1 = s_1, s_0 - q * s_1
        t_0, t_1 = t_1, t_0 - q * t_1
    # Imprimimos la combinacion lineal: r = as + bt
    # print(f"{q} = {x}({s_0}) + {y}({t_0})")
    # print(a,b,s_0,s_1,t_0,t_1)
    return a, s_0, t_0

def inverso(x,n):
    """
    Regresa el inverso multiplicativo de un numero (si lo hay).        
    """
    # Un numero tiene inverso multiplicativo si x,n son primos relativos (coprimos)
    if mcd(x,n) == 1:
        a, s, t = euclides_extendido(x,n)
        return reduce(s,n)
    else:
        raise ValueError(f"El inverso multiplicativo de {x} mod {n} no existe")

#print(raiz_cuadrada_p(968, 1223))
#print(raiz_cuadrada_p(209, 1223))
#print(raiz_cuadrada_p(12, 13))
#print(raiz_cuadrada_p(25, 50))

# Algoritmo para encontrar la raiz cuadrado modulo p, p primo y p = 3 mod 4
def raiz_3(a, p):
    if not es_primo(p):
        raise ValueError(f"{p} no es primo")
    if a < 0 or a >= p:
        a = a % p
    if p % 4 != 3:
        raise ValueError(f"{p} no es congruente con 3 modulo 4")
    # Paso 1, calculamos r = a^((p+1)/4) mod p
    exp = (p + 1) // 4
    r = pow(a, exp, p)
    # Paso 2, regresamos r mod p y -r mod p
    return (r % p, (-r) % p)

#print(raiz_3(968, 1223))

# Algoritmo para encontrar la raiz cuadrado modulo p, p primo y p = 5 mod 8
def raiz_5(a, p):
    if not es_primo(p):
        raise ValueError(f"{p} no es primo")
    if a < 0 or a >= p:
        a = a % p
    if p % 8 != 5:
        raise ValueError(f"{p} no es congruente con 5 modulo 8")
    if p == 2:
        raise ValueError(f"{p} no es impar")
    # Paso 1, calculamos d = a^((p-1)/4) mod p
    exp = (p - 1) // 4
    d = pow(a, exp, p)
    # Paso 2, si d = 1, calculamos r = a^((p+3)/8) mod p
    if d == 1:
        exp = (p + 3) // 8
        r = pow(a, exp, p)
    # Paso 2, si d = p-1, calculamos r = 2 * a * (4a)^((p-5)/8) mod p
    elif d == p - 1:
        exp = (p - 5) // 8
        r = 2 * a * pow(4 * a, exp, p) % p
    # Paso 3, regresamos r mod p y -r mod p
    return (r % p, (-r) % p)

#print(raiz_5(12, 13))

# Algoritmo para encontrar la raiz cuadrado modulo p, p primo, cuando la s en p-1 = 2^s * t es grande
def raiz_grande(a, p):
    if not es_primo(p):
        raise ValueError(f"{p} no es primo")
    if a < 0 or a >= p:
        a = a % p
    if p == 2:
        raise ValueError(f"{p} no es impar")
    # Paso 1, escogemos un entero b en Z_p, tal que el simbolo de Legendre de (b^2 - 4a)/p = -1
    b = 0
    while jacobi(pow(b, 2) - 4 * a, p) != -1:
        b = random.randint(0, p - 1)
    # Paso 2, sea f el polinomio x^2 - bx + a
    f = [1, -b, a]
    # Paso 3, calculamos r = x^(p+1)/2 mod f
    exp = (p + 1) // 2
    poli = [0] * (exp + 1)
    poli[0] = 1
    r = mod_poli(poli, f, p)
    r = r[0]
    return (r % p, (-r) % p)

#print(raiz_grande(968, 1223))
#print(raiz_grande(12, 13))

# Algoritmo para encontrar la raiz cuadrado modulo n, n = p * q, con p y q primos
def raiz_cuadrada_n(a, n):
    if a < 0 or a >= n:
        a = a % n
    # Paso 0, factorizamos n
    if factorizar(n) == 0:
        raise ValueError(f"{n} debe ser un n = p * q, con p y q primos")
    p, q = factorizar(n)
    # Paso 1, encontramos las raices cuadradas de a modulo p
    r_1, r_2 = raiz_cuadrada_p(a, p)
    # Paso 2, encontramos las raices cuadradas de a modulo q
    s_1, s_2 = raiz_cuadrada_p(a, q)
    # Paso 3, encontramos c y d tal que c * q + d * p = 1
    _, c, d = euclides_extendido(p, q)
    # Paso 4, calculamos x = (r_1 * d * q + s_1 * c * p) mod n
    x = (r_1 * d * q + s_1 * c * p) % n
    # Paso 4, calculamos y = (r_1 * d * q - s_1 * c * p) mod n
    y = (r_1 * d * q - s_1 * c * p) % n
    # Paso 5, regresamos x mod n, -x mod n, y mod n, -y mod n
    return (x % n, (-x) % n, y % n, (-y) % n)

# Funcion para factorizar un numero n en dos primos p y q
def factorizar(n):
    # Paso 1, obtenemos los primos menores a n
    primos = primos_menores(n)
    # Paso 2, iteramos sobre los primos
    for p in primos:
        for q in primos:
            # Paso 2.1, si p * q = n, regresamos p y q
            if p * q == n:
                return p, q
    # Paso 3, si no encontramos p y q, regresamos 0
    return 0

# Funcion para encontrar los primos menores a n, Criba de Eratostenes
def primos_menores(n):
    # Paso 1, creamos una lista de booleanos de tamaño n
    primos = [True] * n
    # Paso 2, iteramos sobre los numeros menores a n
    for i in range(2, n):
        # Paso 2.1, si el numero es primo
        if primos[i]:
            # Paso 2.1.1, marcamos los multiplos de i como no primos
            for j in range(i * i, n, i):
                primos[j] = False
    # Paso 3, regresamos los numeros primos
    return [i for i in range(2, n) if primos[i]]

#print(raiz_cuadrada_n(25, 51))

# Funcion para factorizar un numero n en una lista de factores primos
# https://stackoverflow.com/questions/32871539/integer-factorization-in-python
def factorizar_n(n):
    factores = []
    factor = 2
    while factor <= n:
        if n % factor == 0:
            factores.append(factor)
            n = n // factor
        else:
            factor += 1
    return factores

import itertools

# Algoritmo para encontrar las raices cuadradas módulo n para un n compuesto con múltiples factores primos
def raiz_cuadrada_n_gen(a, n):
    if a < 0 or a >= n:
        a = a % n
    if es_primo(n):
        return raiz_cuadrada_p(a, n)
    # Paso 0: Factorizamos n
    factores = factorizar_n(n)
    # Paso 1: Calculamos las raices cuadradas de a módulo cada factor primo
    raices_factor = []
    for p in factores:
        if p == 2:
            raices_factor.append(raiz_2(a))
        elif p == 3:
            raices_factor.append(raiz_3(a))
        else:
            raices_factor.append(raiz_cuadrada_p(a, p))
    # Paso 2: Iteramos sobre todas las combinaciones de las raices generadas modulo cada factor primo
    raices = []
    for combinacion in itertools.product(*raices_factor):
        # Paso 2.1: Calculamos una x que satisfaga las congruencias
        x = 0
        # Paso 2.2; Iteramos sobre cada factor primo
        for i, p in enumerate(factores):
            # Paso 2.2.1: Calculamos m = n // p
            m = n // p
            # Paso 2.2.2: Calculamos c = m^-1 mod p
            c = inverso(m, p)
            # Paso 2.2.3: Agregamos a x el valor de la combinacion modulo p multiplicado por c y m
            # Para que x cumpla con la congruencia
            x += combinacion[i] * c * m
        # Paso 2.3: Agregamos x modulo n y -x modulo n a la lista de raices
        raices.append(x % n)
        raices.append((-x) % n)
    # Paso 3: Eliminamos duplicados y regresamos los resultados únicos
    return list(set(raices))

# Algoritmo para encontrar la raiz cuadrado modulo 2
def raiz_2(a):
    if a < 0 or a >= 2:
        a = a % 2
    if a == 0:
        return (0, 0)
    return (1, 1)

# Algoritmo para encontrar la raiz cuadrado modulo 3
def raiz_3(a):
    if a < 0 or a >= 3:
        a = a % 3
    if a == 0:
        return (0, 0)
    if a == 1:
        return (1, 2)
    raise ValueError(f"No existe la raiz cuadrada de {a} modulo 3")

#print(raiz_cuadrada_n_gen(72, 102))
#print(raiz_cuadrada_n_gen(133, 177))
