# Determinante fast: https://integratedmlai.com/find-the-determinant-of-a-matrix-with-pure-python-without-numpy-or-scipy/
# Determinante recursivo: https://www.youtube.com/watch?v=GhWpLf7-mK4&t=1242s
# Matriz invertible en Z_n: https://math.stackexchange.com/questions/1498737/inverting-a-matrix-in-mathbbz-n-mathbbz

from aritmetica_modular import reduce as modulo
from aritmetica_modular import mcd, inverso

# Modulo en el que estamos trabajando
M = 26

# Mapeo alfabeto
ALFABETO = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25
}

# Mapeo alfabeto invertido
ALFABETO_INVERTIDO = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'J',
    10: 'K',
    11: 'L',
    12: 'M',
    13: 'N',
    14: 'O',
    15: 'P',
    16: 'Q',
    17: 'R',
    18: 'S',
    19: 'T',
    20: 'U',
    21: 'V',
    22: 'W',
    23: 'X',
    24: 'Y',
    25: 'Z'
}

# Divide una cadena en bloques
def dividir_en_bloques(cadena, k):
    bloques = []
    for i in range(0, len(cadena), k):
        if (len(cadena) - i < k):
            bloques.append(cadena[i:] + 'X' * (k - (len(cadena) - i)))
        else:
            bloques.append(cadena[i:i+k])
    return bloques

# Convierte una cadena a un vector
def vector_fila(cadena):
    return [ALFABETO[str(c)] for c in cadena]

# Cifra un vector, regrea una cadena
def cifrar_vector(vector):    
    vector_cifrado = ""
    for v in vector:
        vector_cifrado += ALFABETO_INVERTIDO[modulo(v,M)]
    return vector_cifrado

# Multiplica un vector por una columna
def multiplica_vector_x_columna(fila,columna):
    resultado = 0
    for i in range(len(fila)):
        f = fila[i]
        c = columna[i]
        resultado += f * c
    return resultado

# Multiplica un vector por una matriz
def multiplica_vector_x_matriz(vector, matriz):
    n = len(matriz)
    nuevo_vector = []
    for i in range(n):
        columna = [matriz[j][i] for j in range(n)]
        nuevo_vector.append(modulo(multiplica_vector_x_columna(vector,columna),M))
    return nuevo_vector

# Multiplica dos matrices
def multiplica_matriz_x_matriz(matriz1, matriz2):
    matriz_resultante = []
    n = len(matriz1)
    for fila in matriz1:
        columnas = [[matriz2[j][i] for j in range(n)] for i in range(n)]
        nueva_fila = [multiplica_vector_x_columna(fila,columna) for columna in columnas]
        matriz_resultante.append(nueva_fila)
    return matriz_resultante

# Reduce una matriz modulo m
def matriz_modulo(matriz,m):
    matriz_resultante = []
    for fila in matriz:
        nueva_fila = [modulo(entrada,m) for entrada in fila]
        matriz_resultante.append(nueva_fila)
    return matriz_resultante
    

# Cifra una cadena con una matriz (Cifrado Hill)
def cifrar_hill(cadena, matriz):
    k = len(matriz)
    bloques = dividir_en_bloques(cadena,k)
    vectores = [vector_fila(bloque) for bloque in bloques]
    texto_cifrado = ""
    for vector in vectores:
        nuevo_vector = multiplica_vector_x_matriz(vector, matriz)
        texto_cifrado += cifrar_vector(nuevo_vector)
    return texto_cifrado

# Regresa el determinante de una matriz
def determinante(matriz):
    return determinante_aux(matriz, len(matriz))

def determinante_aux(matriz,n):
# Determinante
    det = 0
    if n == 1:
        det = matriz[0][0]
    else:
        for j in range(n):
            if matriz[0][j] != 0:
                det += pow(-1, j) * matriz[0][j] * determinante_aux(matriz_menor(matriz, n, 0, j), n-1)
    return det

# Regresa la submatriz
def matriz_menor(matriz, n, r, c):
    mm = []
    for i in range(n):
        if i != r:
            fila = []
            for j in range(n):
                if j != c:
                    fila.append(matriz[i][j])
            mm.append(fila)
    return mm

# Regresa la matriz transpuesta de una matriz cuadrada
def matriz_transpuesta(matriz):
    transpuesta = []
    n = len(matriz)
    for i in range(n):
        nueva_fila = [matriz[j][i] for j in range(n)]
        transpuesta.append(nueva_fila)
    return transpuesta

# Regresa la matriz adjunta de una matriz
def matriz_adjunta(matriz):
    return matriz_transpuesta(matriz_cofactores(matriz))

# Regresa la matriz de cofactores de una matriz
def matriz_cofactores(matriz):
    cofactores = []
    n = len(matriz)
    for i in range(n):
        fila = []
        for j in range(n):
            cofactor = pow(-1, i+j) * determinante(matriz_menor(matriz, n, i, j))
            fila.append(cofactor)
        cofactores.append(fila)        
    return cofactores

# Regresa la matriz inversa de una matriz
def matriz_inversa(matriz):
    d = determinante(matriz)
    if mcd(d,M) != 1:
        return None
    d_inverso = inverso(d,M)
    matriz_inversa = []
    for fila in matriz_adjunta(matriz):
        nueva_fila = [ modulo(d_inverso * x,M) for x in fila]
        matriz_inversa.append(nueva_fila)
    return matriz_inversa

if __name__ == "__main__":

    # Ejemplo de laboratorio: 

    clave = [
        [11, 0, 0],
        [0, 1, 1],
        [0, 0, 1]
    ]

    # Palabra a cifrar
    palabra = "CANGREJOX"
    print(palabra)

    # Ciframos la palabra con la clave
    cifrado = cifrar_hill(palabra,clave)
    print(cifrado)

    # CANGREJOX como matriz
    p = [
        [2, 0, 13], 
        [6, 17, 4], 
        [9, 14, 23]
    ]

    # WANORVVOL como matriz
    c = [
        [22, 0, 13],
        [14, 17, 21],
        [21, 14, 11],
    ]
    
    if matriz_inversa(p):
        # Obtenemos la matriz inversa de la clave
        clave_inversa = matriz_inversa(matriz_modulo(multiplica_matriz_x_matriz(matriz_inversa(p),c),M))
        # Desciframos
        descifrado = cifrar_hill(cifrado,clave_inversa)
        print(descifrado)