# Algoritmo del Simbolo de Jacobi
# Si n es primo, es el simbolo de Legendre
def jacobi(a, n):
    if n < 3:
        raise ValueError(f"{n} debe ser mayor o igual a 3")
    if a < 0 or a >= n:
        a = a % n # Hacemos esto para que a este en el rango [0, n)
    # Paso 1, si a = 0, el simbolo es 0
    if a == 0:
        return 0
    # Paso 2, si a = 1, el simbolo es 1
    if a == 1:
        return 1
    # Paso 3, describir a como 2^e * m, con m impar
    e, m = descomponer(a)
    # Paso 4, si e es par, s es 1
    if e % 2 == 0:
        s = 1
    # Paso 4, si n es congruente con 1 o 7 modulo 8, s es 1
    elif n % 8 == 1 or n % 8 == 7:
        s = 1
    # Paso 4, si n es congruente con 3 o 5 modulo 8, s es -1
    elif n % 8 == 3 or n % 8 == 5:
        s = -1
    # Paso 5, si n es congruente con 3 modulo 4 y m es congruente con 3 modulo 4, s es -s
    if n % 4 == 3 and m % 4 == 3:
        s = -s
    # Paso 6, q es n mod m
    q = n % m
    # Paso 7, si m es 1, el simbolo es s
    if m == 1:
        return s
    # Paso 7, en otro caso, el simbolo es s * jacobi(q, m)
    return s * jacobi(q, m)

# Metodo para describir un entero a como 2^e * m, con m impar
def descomponer(a):
    e = 0
    while a % 2 == 0:
        a = a // 2
        e += 1
    return e, a

#print(jacobi(7411, 9283))
#print(jacobi(5, 21))
#print(jacobi(158, 235))