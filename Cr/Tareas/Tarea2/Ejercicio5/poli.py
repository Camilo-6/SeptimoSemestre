# Los polinomios se representan como listas de coeficientes
# Ejemplo, el polinomio 3x^2 + 2x + 1 en Z_5[x] se representa como [3, 2, 1]
# Ejemplo, el polinomio 3x^2 + 5x en Z_7[x] se representa como [3, 5, 0]

# Funcion para sumar dos polinomios en Z_{p^n}[x]
def suma_poli(f, g, p_n):
    if f == [0]:
        return g
    if g == [0]:
        return f
    l_1 = len(f)
    l_2 = len(g)
    if l_1 < l_2:
        f = [0] * (l_2 - l_1) + f
    elif l_2 < l_1:
        g = [0] * (l_1 - l_2) + g
    resultado = [(f[i] + g[i]) % p_n for i in range(max(l_1, l_2))]
    while resultado and resultado[0] == 0:
        resultado.pop(0)
    if resultado == []:
        resultado = [0]
    return resultado

# Funcion para restar dos polinomios en Z_{p^n}[x]
def resta_poli(f, g, p_n):
    if g == [0]:
        return f
    l_1 = len(f)
    l_2 = len(g)
    if l_1 < l_2:
        f = [0] * (l_2 - l_1) + f
    elif l_2 < l_1:
        g = [0] * (l_1 - l_2) + g
    resultado = [(f[i] - g[i]) % p_n for i in range(max(l_1, l_2))]
    while resultado and resultado[0] == 0:
        resultado.pop(0)
    if resultado == []:
        resultado = [0]
    return resultado

# Funcion para multiplicar dos polinomios en Z_{p^n}[x]
def mult_poli(f, g, p_n):
    l_1 = len(f)
    l_2 = len(g)
    if f == [0] or g == [0]:
        return [0]
    if f == [1]:
        return g
    if g == [1]:
        return f
    resultado = [0] * (l_1 + l_2 - 1)
    for i in range(l_1):
        for j in range(l_2):
            resultado[i + j] += f[i] * g[j]
    resultado = [x % p_n for x in resultado]
    while resultado and resultado[0] == 0:
        resultado.pop(0)
    if resultado == []:
        resultado = [0]
    return resultado

# Funcion para dividir dos polinomios en Z_{p^n}[x], retorna el cociente y el residuo
# https://en.wikipedia.org/wiki/Polynomial_long_division#Pseudocode
def div_poli(f, g, p_n):
    if g == [0]:
        raise ValueError("No se puede dividir por 0")
    q = [0]
    r = f[:]
    while r != [0] and len(r) >= len(g):
        lead_r = r[0]
        lead_g = g[0]
        if lead_g == 0:
            raise ValueError("No se puede dividir por 0")
        coef = lead_r * pow(lead_g, -1, p_n) % p_n
        t = [coef] + [0] * (len(r) - len(g))
        while t and t[0] == 0:
            t.pop(0)
        if t == []:
            t = [0]
        q = suma_poli(q, t, p_n)
        aux = mult_poli(t, g, p_n)
        r = resta_poli(r, aux, p_n)
    return q, r

# Funcion para encontrar el maximo comun divisor de dos polinomios en Z_{p^n}[x]
def mcd_poli(f, g, p_n):
    while g != [0]:
        f, g = g, div_poli(f, g, p_n)[1]
    return f

# Funcion para exponenciar un polinomio a la k en Z_{p^n}[x]
def exp_poli(f, k, p_n):
    if k == 0:
        return [1]
    if k == 1:
        return f
    resultado = f[:]
    for i in range(2, k + 1):
        resultado = mult_poli(resultado, f, p_n)
    return resultado

# Funcion para realizar f(x) mod g(x) en Z_{p^n}[x]
def mod_poli(f, g, p_n):
    if g == [0]:
        raise ValueError("No se puede hacer modulo 0")
    residuo = f[:]
    l_1 = len(residuo)
    l_2 = len(g)
    if l_1 >= l_2:
        _, residuo = div_poli(residuo, g, p_n)
    while residuo and residuo[0] == 0:
        residuo.pop(0)
    if residuo == []:
        residuo = [0]
    return residuo