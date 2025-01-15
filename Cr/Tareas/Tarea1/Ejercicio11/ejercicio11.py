# Metodo para descifrar un par de letras con Playfair usando una matriz 5x5
def descifrar_par_playfair(letra1, letra2, matriz):
    # Encontrar las posiciones de las letras en la matriz
    pos1 = None
    pos2 = None
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == letra1:
                pos1 = (i, j)
            if matriz[i][j] == letra2:
                pos2 = (i, j)
    # Si las letras estan en la misma fila
    # Se usa la letra a la izquierda de cada letra
    if pos1[0] == pos2[0]:
        letra1_descifrada = matriz[pos1[0]][(pos1[1] - 1) % 5]
        letra2_descifrada = matriz[pos2[0]][(pos2[1] - 1) % 5]
    # Si las letras estan en la misma columna
    # Se usa la letra arriba de cada letra
    elif pos1[1] == pos2[1]:
        letra1_descifrada = matriz[(pos1[0] - 1) % 5][pos1[1]]
        letra2_descifrada = matriz[(pos2[0] - 1) % 5][pos2[1]]
    # Si las letras forman un rectangulo
    # Se usa la letra en la misma fila pero en la columna de la otra letra
    else:
        letra1_descifrada = matriz[pos1[0]][pos2[1]]
        letra2_descifrada = matriz[pos2[0]][pos1[1]]
    return letra1_descifrada + letra2_descifrada

# Metodo para descifrar un texto cifrado con Playfair usando una matriz 5x5
def descifrar_playfair(texto, matriz):
    # Separar el texto en pares de letras
    pares = []
    for i in range(0, len(texto), 2):
        pares.append(texto[i:i+2])
    # Descifrar los pares de letras
    texto_descifrado = ""
    for par in pares:
        texto_descifrado += descifrar_par_playfair(par[0], par[1], matriz)
    return texto_descifrado

# Metodo para descifrar el texto de un archivo cifrado con Playfair
# Recibe el archivo, la matriz 5x5 con la que se cifro el texto y un archivo para guardar el texto descifrado
def descifrar_bonito(archivo_origen, matriz, archivo_destino):
    # Leer el archivo
    texto = ""
    with open(archivo_origen, "r") as archivo:
        texto = archivo.read()
    # Descifrar el texto
    texto_descifrado = descifrar_playfair(texto, matriz)
    # Guardar el texto descifrado en un archivo
    with open(archivo_destino, "w") as archivo:
        archivo.write(texto_descifrado)
    return texto_descifrado

# Clave : "nicolas maqiavelo"
tablita = [
    ['n', 'i', 'c', 'o', 'l'],
    ['a', 's', 'm', 'q', 'v'],
    ['e', 'b', 'd', 'f', 'g'],
    ['h', 'j', 'k', 'p', 'r'],
    ['t', 'u', 'x', 'y', 'z']
]

#descifrar_bonito("Criptograma_6.txt", tablita, "descifrado_6.txt")
#descifrar_bonito("Criptograma_6.txt", tablita, "texto_bonito.txt")