# Default alphabet
alphabet = 'ABC'

def isPrime(n):
    '''Nos dice si un número n es primo'''
    if n < 2:
        return False
    primos = criba(n)
    if primos[n]:
        return True
    return False

def inv_add(a, mod):
    '''Nos da el inverso aditivo tal que a + i == 0 modulo n'''
    for i in range(mod):
        if (a+i)%mod == 0:
            return i
    return None

def inv_mult(a, mod):
    '''Nos da el inverso multiplicativo modulo n'''
    for i in range(mod):
        if (a*i)%mod == 1:
            return i
    return None

def table(elliptic_curve, alphabet = alphabet):
    # TODO: arreglar esto
    '''Regesa una tabla de un abecedario mapeado a puntos de la curva elíptica e'''
    pts = elliptic_curve.points
    if len(pts) < len(alphabet):
        # print("Las letras mapeadas no caben en la definición de la curva. Se recortará el alfabeto...\n")
        l = alphabet[:len(pts)]
    else:
        # print("Faltan caracteres a relacionar, se duplicará el alfabeto")
        l = alphabet
        """
        while len(pts) > len(l):
            l = l+l
        l = alphabet[:len(pts)]
        """
        while len(pts) > len(l):
            l += alphabet
        l = l[:len(pts)]
    table = {}

    i = 0
    while i != len(pts):
        table[l[i]] = pts[i]
        i+=1
    return table

# Criba de Eratostenes
def criba(n):
    if n < 2:
        return []
    primos = [True for i in range(n+1)]
    primos[0] = False
    primos[1] = False
    p = 2
    while p*p <= n:
        if primos[p]:
            for i in range(p*p, n+1, p):
                primos[i] = False
        p+=1
    return primos
