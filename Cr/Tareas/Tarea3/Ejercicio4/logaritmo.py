from random import randint
from sympy import Matrix # requiere instalar sympy con pip install sympy

# Funcion para calcular logaritmo discretos usando index-calculus
# Calcular log_a b mod p
# Fuente https://github.com/david-r-cox/pyDLP
def index_calc(p, a, b):
    # Paso 1, generamos la base y las congruencias, se generan 100 congruencias
    congruencias = []
    base = set()
    while len(congruencias) < 100:
        # Paso 2, generamos un numero aleatorio k
        k = randint(2, p)
        valor = pow(a, k, p)
        # Paso 3, verificamos si es B-suave
        es_suave, factores = fact_b_suave(100, valor)
        if es_suave:
            # Paso 4, añadimos la congruencia a la lista y actualizamos la base
            congruencia = (agrupar_factores(factores), k)
            congruencias.append(congruencia)
            base.update(congruencia[0].keys())
    base = list(base)
    # Paso 5, construimos la matriz
    matriz = []
    vector = []
    for congruencia, k in congruencias:
        fila = [congruencia.get(b, 0) for b in base]
        matriz.append(fila)
        vector.append(k)
    # Paso 6, resolvemos el sistema
    matriz_s = Matrix(matriz)
    vector_s = Matrix(vector)
    solucion = matriz_s.solve_least_squares(vector_s)
    # Paso 7, generamos los exponentes y logaritmos
    exponentes = [int(x) % (p - 1) for x in solucion]
    logaritmos = {base: exp for base, exp in zip(base, exponentes)}
    # Paso 8, intentamos resolver el logaritmo, en un numero maximo de 100000000 iteraciones
    for i in range (100000000):
        k = randint(2, p)
        # Paso 9, generamos un candidato
        inv = pow(a, -1, p)
        candidato = (b * pow(inv, k, p)) % p
        # Paso 10, verificamos si es B-suave
        es_suave, factores = fact_b_suave(100, candidato)
        if es_suave:
            # Paso 11, verificamos si es un logaritmo valido
            factores_exp = agrupar_factores(factores)
            eval = sum(logaritmos.get(base, 0) * exp for base, exp in factores_exp.items()) % (p - 1)
            eval = (eval + k) % (p - 1)
            if pow(a, eval, p) == b:
                return eval
    return None

# Funcion para factorizar un numero y ver si es B-suave
def fact_b_suave(b, n):
    factores = factorizar_n(n)
    if len(factores) > 0 and max(factores) <= b:
        return True, factores
    return False, factores

# Funcion para factorizar un numero
def factorizar_n(n):
    factores = []
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            factores.append(factor)
            n //= factor
        factor += 1
    if n > 1:
        factores.append(n)
    return factores

# Funcion para agrupar los factores y asi tener un exponente
def agrupar_factores(factores):
    factores_agrupados = {}
    for factor in factores:
        factores_agrupados[factor] = factores_agrupados.get(factor, 0) + 1
    return factores_agrupados

# Calculamos log_3 37 mod 1217
a = 3
b = 37
p = 1217
for i in range(0, p-1):
    if pow(a, i, p) == b:
        print(f"log_{a} {b} mod {p} = {i}, usando fuerza bruta")
        break
log = index_calc(p, a, b)
if log is not None:
    print(f"log_{a} {b} mod {p} = {log}, usando index-calculus")
else:
    print("No se logro encontrar el logaritmo, intenta con mas iteraciones")