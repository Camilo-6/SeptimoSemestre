from collections import Counter

# Metodo para quitar espacios y saltos de linea de un archivo de texto y guardar el resultado en otro archivo
def quitar_espacios(original, nuevo):
    with open(original, 'r') as archivo:
        texto = archivo.read()
    texto = texto.replace(' ', '')
    texto = texto.replace('\n', '')
    with open(nuevo, 'w') as archivo:
        archivo.write(texto)
    return texto

# Quitar los espacios del archivo de texto
"""
texto_limpio = quitar_espacios('criptograma_2.txt', 'criptograma_2_s.txt')
"""

# Calcular el indice de coincidencia de un texto dado un alfabeto
def calcular_indice_coincidencia(texto, alfabeto):
    # Contar la frecuencia de cada letra
    frecuencias = {letra: 0 for letra in alfabeto}
    for letra in texto:
        letra = letra.lower()
        if letra in frecuencias:
            frecuencias[letra] += 1
    # Calcular el total de letras
    total_letras = sum(frecuencias.values())
    #print("Total de letras:", total_letras)
    # Calcular el índice de coincidencia con la formula
    # IC = (f1 * (f1 - 1) + f2 * (f2 - 1) + ... + fn * (fn - 1)) / (n * (n - 1))
    indice_coincidencia = 0
    for frecuencia in frecuencias.values():
        indice_coincidencia += frecuencia * (frecuencia - 1)
    if total_letras > 1:
        indice_coincidencia /= total_letras * (total_letras - 1)
    else:
        indice_coincidencia = 0
    return indice_coincidencia

# Leer el archivo de texto
with open('criptograma_2_s.txt', 'r') as archivo:
    texto = archivo.read()

# Calcular el índice de coincidencia
"""
print("Indice de coincidencia:", calcular_indice_coincidencia(texto,"abcdefghijklmnopqrstuvwxyz"))
"""

# Metodo para encontrar cadenas repetidas en un texto (de una longitud dada o mayor) y las posiciones donde se encuentran
def encontrar_cadenas_repetidas(texto, longitud):
    # Encontrar cadenas de longitud dada o mayor y las posiciones donde se encuentran
    cadenas = {}
    for i in range(len(texto) - longitud + 1):
        for j in range(longitud, len(texto) - i + 1):
            cadena = texto[i:i + j]
            if cadena in cadenas:
                cadenas[cadena].append(i)
            else:
                cadenas[cadena] = [i]
    # Filtras las cadenas que no aparecen mas de una vez
    cadenas_repetidas = {cadena: posiciones for cadena, posiciones in cadenas.items() if len(posiciones) > 1}
    # Filtras las cadenas que son subcadenas de otras cadenas
    cadenas_no_utilizadas = []
    for cadena1 in cadenas_repetidas.keys():
        for cadena2 in cadenas_repetidas.keys():
            if cadena1 != cadena2 and cadena1 in cadena2:
                cadenas_no_utilizadas.append(cadena1)
    cadenas_repetidas = {cadena: posiciones for cadena, posiciones in cadenas_repetidas.items() if cadena not in cadenas_no_utilizadas}
    return cadenas_repetidas

# Encontrar las cadenas repetidas de longitud 7 o mayor y la distancia entre ellas
cadenas_que_se_repite = encontrar_cadenas_repetidas(texto, 7)
"""
print("--------------------")
print("Cadenas repetidas:")
for cadena, posiciones in cadenas_que_se_repite.items():
    print("Cadena:", cadena, "Posiciones:", posiciones)
"""

# Metodo para calcular la distancia entre las cadenas repetidas y ponerlas con la cadena y la distancia
def calcular_distancia_cadenas(cadenas_repetidas):
    cadenas_distancia = {}
    for cadena, posiciones in cadenas_repetidas.items():
        distancias = []
        for i in range(len(posiciones) - 1):
            distancia = posiciones[i + 1] - posiciones[i]
            distancias.append(distancia)
        cadenas_distancia[cadena] = distancias
    return cadenas_distancia

# Calcular la distancia entre las cadenas repetidas
distancias = calcular_distancia_cadenas(cadenas_que_se_repite)
"""
print("--------------------")
print("Distancias entre cadenas repetidas:")
for cadena, distancia in distancias.items():
    print("Cadena:", cadena, "Distancia:", distancia)
"""

# Metodo para calcular los factores primos de un numero
def calcular_factores_primos(numero):
    factores_primos = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            factores_primos.append(divisor)
            numero //= divisor
        else:
            divisor += 1
    return factores_primos

# Metodo para calcular los factores primos de las distancias entre las cadenas repetidas
def calcular_factores_primos_distancias(distancias):
    factores_primos_distancias = {}
    for cadena, distancia in distancias.items():
        factores_primos_distancias[cadena] = []
        for d in distancia:
            factores_primos = calcular_factores_primos(d)
            factores_primos_distancias[cadena].append(factores_primos)
    return factores_primos_distancias

# Calcular los factores primos de las distancias entre las cadenas repetidas
factores_primos_distancias = calcular_factores_primos_distancias(distancias)
"""
print("--------------------")
print("Factores primos de las distancias entre cadenas repetidas:")
for cadena, factores_primos in factores_primos_distancias.items():
    print("Cadena:", cadena, "Factores primos:", factores_primos)
"""

# Metodo para dividir el texto en fragmentos de una longitud dada y guardar todos los fragmentos en una lista
def dividir_texto_en_fragmentos(texto, longitud):
    fragmentos = []
    for i in range(0, len(texto), longitud):
        fragmento = texto[i:i + longitud]
        fragmentos.append(fragmento)
    return fragmentos

# Dividir el texto en fragmentos de longitud 10 y guardar los fragmentos en un archivo "criptograma_2_d.txt" separados por un salto de linea
fragmentos = dividir_texto_en_fragmentos(texto, 10)
"""
with open('criptograma_2_d.txt', 'w') as archivo:
    for fragmento in fragmentos:
        archivo.write(fragmento + '\n')
"""

# Metodo para obtener una lista de las letras de un texto y cuantas veces aparecen, ordenadas de mayor a menor frecuencia
def obtener_frecuencias_letras(texto):
    # Contar las ocurrencias de cada letra
    contador = Counter(texto)
    # Ordenar las letras de mayor a menor frecuencia de aparicion
    letras = [(letra, cuenta) for letra, cuenta in contador.items()]
    letras.sort(key=lambda x: x[1], reverse=True)
    return letras

# Metodo para obtener las frecuencias de letras en la posicion i de los fragmentos de un texto
def obtener_frecuencias_letras_posicion_fragmentos(fragmentos, i):
    # Obtener las letras de la posicion i de los fragmentos, si el fragmento no tiene la posicion i, se ignora
    letras = [fragmento[i] for fragmento in fragmentos if i < len(fragmento)]
    # Obtener las frecuencias de las letras
    frecuencias = obtener_frecuencias_letras(letras)
    return frecuencias

# Obtener las frecuencias de las letras en la posicion 0 de los fragmentos
posicion_actual = 0
frecuencias_letras_posicion = obtener_frecuencias_letras_posicion_fragmentos(fragmentos, posicion_actual)
"""
print("--------------------")
print("Frecuencias de las letras en la posicion " + str(posicion_actual) + " de los fragmentos:")
for letra, cantidad in frecuencias_letras_posicion:
    print("Letra:", letra, "Cantidad:", cantidad)
"""

# Clave
clave = "SUNTZARTEG"

# Tabla de Vigenere
tablita = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
    ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a"],
    ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b"],
    ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c"],
    ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d"],
    ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e"],
    ["g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f"],
    ["h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g"],
    ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h"],
    ["j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i"],
    ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    ["l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"],
    ["m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"],
    ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"],
    ["o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"],
    ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o"],
    ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"],
    ["r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"],
    ["s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"],
    ["t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s"],
    ["u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"],
    ["v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u"],
    ["w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v"],
    ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w"],
    ["y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x"],
    ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]
]

# Metodo para volver una letra a numero
def letra_a_numero(letra):
    return ord(letra) - ord('a')

# Metodo para volver un numero a letra
def numero_a_letra(numero):
    return chr(numero + ord('a'))

# Metodo para descifrar un texto usando una clave, la tabla de Vigenere y un alfabeto
def descifrar_vigenere(texto, clave, tablita, alfabeto):
    texto_descifrado = []
    clave_minuscula = clave.lower()
    clave_longitud = len(clave)
    clave_posicion = 0
    for letra in texto:
        if letra in alfabeto:
            letra_clave = clave_minuscula[clave_posicion % clave_longitud]
            letra_miniscula = letra.lower()
            fila = letra_a_numero(letra_clave)
            for i in range(len(tablita)):
                if tablita[fila][i] == letra_miniscula:
                    letra_descifrada = numero_a_letra(i)
                    break
            texto_descifrado.append(letra_descifrada)
            clave_posicion += 1
        else:
            texto_descifrado.append(letra)
    return ''.join(texto_descifrado)

# Descifrar el texto usando la clave obtenida y guardarlo en un archivo "criptograma_2_b.txt"
texto_descifrado = descifrar_vigenere(texto, clave, tablita, "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
"""
with open('criptograma_2_b.txt', 'w') as archivo:
    archivo.write(texto_descifrado)
"""
