# Metodo para obtener el determinante de una matriz 2x2
def determinante(matriz):
    a, b, c, d = matriz[0][0], matriz[0][1], matriz[1][0], matriz[1][1]
    return (a * d - b * c)

# Metodo para encontrar las matrices invertibles en Z_26
# Una matriz es invertible en z_n si y solo si el determinante no es
# congruente a 0 modulo p, para cada divisor de n
# Dos numeros x, y son congruentes modulo n si tienen el mismo residuo
# al ser divididos por n
# Al dividir 0 entre cualquier numero (excepto 0) el residuo es 0
def matrices_invertibles():
    matrices = []
    divisores = [2, 13, 26]
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    matriz = [[a, b], [c, d]]
                    det = determinante(matriz)
                    if all(det % divisor != 0 for divisor in divisores):
                        matrices.append(matriz)
    return matrices

print(len(matrices_invertibles()))