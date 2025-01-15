def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def Rho_Pollard(n):
    #Paso 1 - Declarar a=2 y b=2
    a = 2 
    b = 2
    #Paso 2 - Desde 1 hasta que ya no se pueda (xd) hacer lo siguiemte
    for i in range(1,100000000):
    #2.1- Calcular a = a^2+1 mod n, b = b^2+1 mod n y otra vez b = b^2+1 mod n 
        a = (pow(a,2)+1) % n
        print(f"Calculando a={a}^2+1 mod {n}={a}")
        b = (pow(b,2)+1) % n
        print(f"Calculando b={b}^2+1 mod {n}={b}") 
        b = (pow(b,2)+1) % n
        print(f"Calculando b={b}^2+1 mod {n}={b}") 
        # 2.2 Calcular d = gcd(a-b,n)
        d = gcd(a-b,n)
        print(f"\n gcd({a}-{b},{n}) = {d}")
        #2.3 Si 1<d<n regresar d y terminar con éxito
        if(1<d<n):
            print(f"Se cumple que 1 < {d} < {n} \n Tenemos un factor d = {d}")
            e = n//d
            print(f" El otro factor es e = {n} / {d} = {e}")
            print(f"\n ÉXITO, se contraron los factores de {n}\n Los factores son es d = {d}, e = {e}\n n = d*e = {d * e}")
            break
        #2.4 Si d =n terminar el algoritmo con fracaso
        if(d == n):
            print(f"FRACASO\n No se encontraron factores para {n}")
            break

# Algoritmo para obtener los primos menores a n
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

# Algoritmo para ver si un numero n es b-smooth usando los primos menores a b
def es_b_smooth(n, primos):
    # Paso 1, iteramos sobre los primos menores a n
    for primo in primos:
        # Paso 2, mientras n sea divisible por el primo
        while n % primo == 0:
            # Paso 3, actualizamos n
            n = n // primo
    # Paso 4, si n es 1 regresamos True
    if n == 1:
        return True
    # Paso 5, regresamos False
    return False

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

# Funcion para agrupar los factores primos y asi tener un exponente
def agrupar_factores(factores):
    factores_agrupados = {}
    for factor in factores:
        if factor in factores_agrupados:
            factores_agrupados[factor] += 1
        else:
            factores_agrupados[factor] = 1
    return factores_agrupados

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

# Algoritmo para criba cuadratica https://micsymposium.org/mics_2011_proceedings/mics2011_submission_28.pdf y https://en.wikipedia.org/wiki/Quadratic_sieve
def criba_cuadratica(n):
    # Paso 1, obtener el nivel de suavidad
    b = int(n ** 0.5)
    # Paso 2, obtener los primos menores a b
    p_b = primos_menores(b)
    # Paso 3, obtener F, la base de factores
    f = []
    # Paso 3, iteramos sobre los primos menores a b
    for primo in p_b:
        # Paso 4, calcular z = n^{p-1/2} mod p
        z = pow(n, (primo - 1) // 2, primo)
        # Paso 5, si z es 1, agregar p a f
        if z == 1:
            f.append(primo)
    # Paso 6, buscar numeros suaves
    suaves = []
    i = b
    # Paso 7, mientras no se tengan suficientes numeros suaves
    while len(suaves) < len(f) + 1:
        # Paso 8, calculamos i^2 mod n
        posible = pow(i, 2, n)
        # Paso 9, revisamos si es b-smooth
        if es_b_smooth(posible, f):
            # Paso 10, si es b-smooth, lo agregamos a suaves
            suaves.append(i)
        # Paso 11, aumentamos i
        i += 1
    # Paso 12, iteramos sobre los numeros suaves, intentando factorizar n
    for suave in suaves:
        # Paso 13, factorizamos el numero suave
        factoress = factorizar_n(suave)
        factores_exp = agrupar_factores(factoress)
        # Paso 14, revisar el producto de los factores impares, los que deben contribuir al factor
        producto = 1
        for factor, exponente in factores_exp.items():
            if exponente % 2 == 1:
                producto *= factor
        # Paso 15, si el producto de los factores impares no es el numero suave ni n
        if producto != suave and producto != n:
            # Paso 16, calcular el factor candidato que es la diferencia entre el producto y el numero suave
            candidado = producto - suave
            if candidado < 0:
                candidado = -candidado
            # Paso 17, calcular el mcd del factor candidato y n
            numero = mcd(candidado, n)
            # Paso 18, si el mcd es un divisor no trivial de n, es decir mayor a 1 y menor a n
            if 1 < numero < n:
                # Paso 19, regresar el divisor y el cociente
                return numero, n // numero
    # Paso 20, regresar None
    return None

if __name__== "__main__":
    #Rho_Pollard(256961)
    print(criba_cuadratica(8746))
