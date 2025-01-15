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

# Metodo para resolver dos congruencias de la forma ax + y ≡ b (mod m) y cx + y ≡ d (mod m), obteniendo los valores de x y y
def resolver_congruencias(a, b, c, d, m):
    # Primero resolver para x
    # Restar la segunda congruencia de la primera para eliminar y
    # (ax + y - (cx + y)) ≡ (b - d) (mod m) => (a - c)x ≡ (b - d) (mod m)
    a_menos_c = a - c
    b_menos_d = b - d
    # Encontrar x en (a - c)x ≡ (b - d) (mod m)
    # Encontrar el inverso modular de (a - c) mod m
    inv = inverso(a_menos_c % m, m)
    # Resolver para x
    x = (inv * (b_menos_d % m)) % m
    # Resolver para y
    # Sustituir x en ax + y ≡ b (mod m) y encontrar y
    y = (b - a * x) % m
    return x, y