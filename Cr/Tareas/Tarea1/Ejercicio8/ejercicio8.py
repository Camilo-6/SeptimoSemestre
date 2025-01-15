# Metodo para quitar los espacios blancos de un archivo de texto
def quitar_espacios_blancos(archivo_origen, archivo_destino):
    with open(archivo_origen, 'r') as archivo:
        lineas = archivo.readlines()
    texto_bonito = ''
    for linea in lineas:
        texto_bonito += linea.replace(' ', '')
    with open(archivo_destino, 'w') as archivo:
        archivo.write(texto_bonito)

#quitar_espacios_blancos('Criptograma_3.txt', 'criptograma_3_s.txt')

# Frecuencias típicas de las letras en español
frecuencias_espanol = {
    'e': 13.676, 'a': 12.529, 'o': 8.684, 's': 7.980, 'r': 6.873, 'n': 6.712, 'i': 6.87,
    'd': 5.856, 'l': 4.971, 'c': 4.679, 't': 4.629, 'u': 3.934, 'm': 3.150, 'p': 2.505,
    'b': 1.420, 'g': 1.006, 'y': 0.895, 'v': 0.895, 'q': 0.875, 'h': 0.704, 'f': 0.694,
    'z': 0.523, 'j': 0.443, 'x': 0.221, 'w': 0.023, 'k': 0.004
}

abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Metodo para calcular las frecuencias de los caracteres del texto de un archivo
def calcular_frecuencias(archivo, abecedario):
    with open(archivo, 'r') as file:
        texto = file.read()
    # Usar un diccionario para contar las ocurrencias de cada letra
    frecuencias = {letra: 0 for letra in abecedario}
    total_caracteres = 0
    # Contar las ocurrencias de cada letra
    for caracter in texto:
        if caracter in abecedario:
            frecuencias[caracter] += 1
            total_caracteres += 1
    # Calcular las frecuencias de las letras
    for letra in abecedario:
        frecuencias[letra] /= total_caracteres
    # Ordenar de mayor a menor las frecuencias
    frecuencias = {letra: frecuencias[letra] for letra in sorted(frecuencias.keys(), key=lambda letra: frecuencias[letra], reverse=True)}
    return frecuencias

#print(calcular_frecuencias('criptograma_3_s.txt', abecedario))
"""
{'I': 0.12842712842712842, 'L': 0.11688311688311688, 'G': 0.09956709956709957, 'A': 0.08802308802308802, 'H': 0.08513708513708514, 
'Q': 0.0836940836940837, 'P': 0.05339105339105339, 'R': 0.049062049062049064, 'Z': 0.046176046176046176, 'J': 0.044733044733044736, 
'D': 0.04329004329004329, 'S': 0.04184704184704185, 'K': 0.025974025974025976, 'F': 0.024531024531024532, 'T': 0.01443001443001443, 
'E': 0.012987012987012988, 'U': 0.008658008658008658, 'M': 0.007215007215007215, 'Y': 0.007215007215007215, 'N': 0.005772005772005772, 
'O': 0.005772005772005772, 'B': 0.004329004329004329, 'X': 0.002886002886002886, 'C': 0.0, 'V': 0.0, 'W': 0.0}
"""

import random

#mapeo_inicial = {'I': 'e', 'L': 'a'}
#mapeo_inicial = {'I': 'e', 'L': 'a', 'A': 'i', 'G': 'n', 'J': 'd', 'E': 'g'}
#mapeo_inicial = {'I': 'e', 'L': 'a', 'A': 'i', 'G': 'n', 'J': 'd', 'E': 'g', 'K': 'p', 'Z': 'c', 'Q': 's'}
#mapeo_inicial = {'I': 'e', 'L': 'a', 'A': 'i', 'G': 'n', 'J': 'd', 'E': 'g', 'K': 'p', 'Z': 'c', 'Q': 's', 'P': 'r', 'R': 't', 'H': 'o'}
#mapeo_inicial = {'A': 'i', 'D': 'l', 'E': 'g', 'G': 'n', 'H': 'o', 'I': 'e', 'J': 'd', 'K': 'p', 'L': 'a', 'O': 'q', 'P': 'r', 'Q': 's', 'R': 't', 'S': 'u', 'U': 'b', 'Z': 'c'}
#mapeo_inicial = {'A': 'i', 'D': 'l', 'E': 'g', 'F': 'm', 'G': 'n', 'H': 'o', 'I': 'e', 'J': 'd', 'K': 'p', 'L': 'a', 'O': 'q', 'P': 'r', 'Q': 's', 'R': 't', 'S': 'u', 'U': 'b', 'Z': 'c'}
#mapeo_inicial = {'A': 'i', 'B': 'j', 'D': 'l', 'E': 'g', 'F': 'm', 'G': 'n', 'H': 'o', 'I': 'e', 'J': 'd', 'K': 'p', 'L': 'a', 'M': 'f', 'O': 'q', 'P': 'r', 'Q': 's', 'R': 't', 'S':'u', 'T': 'v', 'U': 'b', 'X': 'y', 'Z': 'c'}
mapeo_inicial = {'A': 'i', 'B': 'j', 'D': 'l', 'E': 'g', 'F': 'm', 'G': 'n', 'H': 'o', 'I': 'e', 'J': 'd', 'K': 'p', 'L': 'a', 'M': 'f', 'N': 'h', 'O': 'q', 'P': 'r', 'Q': 's', 'R': 't', 'S':'u', 'T': 'v', 'U': 'b', 'X': 'y', 'Y': 'z', 'Z': 'c'}


# Metodo para crear un mapeo aleatorio basado en las frecuencias de las letras cifradas y reales y usando un mapeo inicial
def crear_mapeo_aleatorio(frecuencias_cifradas, frecuencias_reales):
    # Ordenar de mayor a menor las frecuencias de las letras cifradas y reales
    letras_cifradas = sorted(frecuencias_cifradas.keys(), key=lambda letra: frecuencias_cifradas[letra], reverse=True)
    letras_reales = sorted(frecuencias_reales.keys(), key=lambda letra: frecuencias_reales[letra], reverse=True)
    # Copiar el mapeo inicial
    mapeo = mapeo_inicial.copy()
    # Filtrar letras cifradas y reales ya mapeadas, y obtener las probabilidades de las letras reales disponibles
    letras_cifradas_disponibles = [letra for letra in letras_cifradas if letra not in mapeo_inicial]
    letras_reales_disponibles = [letra for letra in letras_reales if letra not in mapeo_inicial.values()]
    probabilidades_reales_disponibles = [frecuencias_reales[letra] for letra in letras_reales_disponibles]
    # Crear un mapeo aleatorio
    for letra_cifrada in letras_cifradas_disponibles:
        if letras_reales_disponibles:
            # Seleccionar una letra real disponible aleatoriamente, asignarla al mapeo y eliminarla de las disponibles
            letra_real = random.choices(letras_reales_disponibles, weights=probabilidades_reales_disponibles, k=1)[0]
            mapeo[letra_cifrada] = letra_real
            letras_reales_disponibles.remove(letra_real)
            # Actualizar las probabilidades de las letras reales disponibles
            probabilidades_reales_disponibles = [frecuencias_reales[letra] for letra in letras_reales_disponibles]
        else:
            break
    return mapeo

# Metodo para sustituir los caracteres de un texto usando un mapeo
def sustituir_texto(mapeo, archivo):
    with open(archivo, 'r') as file:
        texto = file.read()
    texto_descifrado = []
    # Sustituir cada caracter del texto usando el mapeo
    for caracter in texto:
        if caracter in mapeo:
            texto_descifrado.append(mapeo[caracter])
        else:
            # En caso de que el caracter no esté en el mapeo, se mantiene igual
            texto_descifrado.append(caracter)
    return ''.join(texto_descifrado)

# Metodo para verificar cuantas palabras se encuentran en un texto descifrado usando un diccionario
def verificar_palabras(texto_descifrado, diccionario):
    palabras_encontradas = []
    # Longitud minima de las palabras a buscar
    longitud_minima_palabra = 8
    # Buscar palabras en el texto descifrado
    for i in range(len(texto_descifrado)):
        for j in range(i + longitud_minima_palabra, len(texto_descifrado) + 1):
            secuencia = texto_descifrado[i:j].lower()
            # Si la secuencia es una palabra en el diccionario y no ha sido encontrada previamente, se agrega a la lista
            if secuencia in diccionario and secuencia not in palabras_encontradas:
                palabras_encontradas.append(secuencia)
    # Regresamos cuantas palabras se encontraron y la lista de palabras encontradas
    return len(palabras_encontradas), palabras_encontradas

# Metodo para generar un diccionario de palabras a partir de un archivo de texto
def generar_diccionario(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        palabras = set(file.read().splitlines())
    return palabras

# Diccionario de palabras en español https://github.com/xavier-hernandez/spanish-wordlist/blob/main/text/spanish_words.txt
# Modificado para no tener acentos
diccionario_espanol = generar_diccionario("spanish_words.txt")

# Frecuencias de los caracteres en el texto cifrado
frecuencias_cifradas = calcular_frecuencias('criptograma_3_s.txt', abecedario)

# Generar mapeos aleatorios y descifrar el texto
listo = False
while not listo:
    # Crear un mapeo aleatorio y sustituir el texto cifrado
    mapeo_aleatorio = crear_mapeo_aleatorio(frecuencias_cifradas, frecuencias_espanol)
    texto_descifrado = sustituir_texto(mapeo_aleatorio, 'criptograma_3_s.txt')
    # Revisar cuantas palabras se encontraron en el texto descifrado
    palabras_correctas, palabras_encontradas = verificar_palabras(texto_descifrado, diccionario_espanol)
    # Si se encontraron al menos n palabras, mostrar el texto descifrado y el mapeo
    if palabras_correctas >= 5:
        print("Texto sustituido")
        print(texto_descifrado)
        print(f"\n{palabras_correctas} palabras encontradas en el diccionario")
        print("Palabras encontradas:", palabras_encontradas)
        print("\nAbecedario usado:")
        print(mapeo_aleatorio)
        listo = True