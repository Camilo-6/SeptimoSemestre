import random
from collections import Counter

# Primero encontrar una palabra con 8 letras, luego aumentar hasta 4 palabras
# Despues de patricio aunmentar a 9 letras
# Mapeo inicial
# palabras constante, anterior, historia (algo reconocido por _istoria), la (luego reconocer primera es _a), patricio, oficiales, de (reconocida por _e), nuestros (reconocida por n_estros), hombres libres (reconocer ho__res li_res), y (reconocer espacio entre patricios _ plebe_os), esclavos (reconocer escla_os), despues ordenar el mapeo y ver quien falta
# encontrar quienes son B, D, E, U, V, Y, Z (D, E, U, V y Z no aparecen en el texto cifrado)
# B es q por lucha _ue termino y Y es g por anti_ua roma, para las demas letras asignamos aleatoriamente
mapeo_inicial = {'A': 'b','B': 'q','C': 'l','F': 'h','G': 'o','H': 'm','I': 'i','J': 'r','K': 'a','L': 'd','M': 'e','N': 'n','O': 's','P': 't','Q': 'u','R': 'c','S': 'p','T': 'v','W': 'y','X': 'f','Y': 'g'}

# Frecuencias típicas de las letras en español
frecuencias_espanol = {
    'e': 13.676, 'a': 12.529, 'o': 8.684, 's': 7.980, 'r': 6.873, 'n': 6.712, 'i': 6.87,
    'd': 5.856, 'l': 4.971, 'c': 4.679, 't': 4.629, 'u': 3.934, 'm': 3.150, 'p': 2.505,
    'b': 1.420, 'g': 1.006, 'y': 0.895, 'v': 0.895, 'q': 0.875, 'h': 0.704, 'f': 0.694,
    'z': 0.523, 'j': 0.443, 'x': 0.221, 'w': 0.023, 'k': 0.004
}

# Texto cifrado
#texto_cifrado = "CKFIOPGJIKLMPGLKOCKOOGRIMLKLMOFKOPKNQMOPJGOLIKOMOCKFIOPGJIKLMCKOCQRFKOLMRCKOMOFGHAJMOCIAJMOWMORCKTGOSKPJIRIGOWSCMAMWGOOMNGJMOWOIMJTGOHKMOPJGOWGXIRIKCMOMNQNKSKCKAJKGSJMOGJMOWGSJIHILGOOMMNXJMNPKJGNOIMHSJMHKNPQTIMJGNQNKCQRFKRGNOPKNPMTMCKLKQNKOTMRMOWGPJKOXJKNRKWKAIMJPKCQRFKBQMPMJHINGOIMHSJMRGNCKPJKNOXGJHKRIGNJMTGCQRIGNKJIKLMPGLKCKOGRIMLKLGMCFQNLIHIMNPGLMCKORCKOMOMNSQYNKMNCKOKNPMJIGJMOMSGRKOFIOPGJIRKOMNRGNPJKHGORKOISGJPGLKOSKJPMOQNKRGHSCMPKLIXMJMNRIKRIGNLMCKOGRIMLKLMNLITMJOGOMOPKHMNPGOQNKHQCPISCMMORKCKYJKLQKCLMRGNLIRIGNMOOGRIKCMOMNCKKNPIYQKJGHKFKCCKHGOSKPJIRIGOSCMAMWGOWMORCKTGOMNCKMLKLHMLIKOMNGJMOXMQLKCMOTKOKCCGOHKMOPJGOGXIRIKCMOWOIMJTGOWKLMHKOMNRKOIPGLKOMOPKORCKOMOPGLKTIKMNRGNPJKHGOYJKLKRIGNMOMOSMRIKCMO"

# Obtener el texto cifrado desde el archivo criptograma_1.txt, ademas quitar los espacios en blanco
texto_original = ""
with open("primero/criptograma_1.txt", "r") as file:
    texto_original = file.read()
texto_cifrado = texto_original.replace(" ", "")

# Metodo para calcular las frecuencias de los caracteres en un texto usando un diccionario
def calcular_frecuencias(texto):
    # Contar las ocurrencias de cada caracter
    contador = Counter(texto)
    # Calcular las frecuencias de los caracteres
    total_caracteres = sum(contador.values())
    frecuencias = {caracter: cuenta / total_caracteres for caracter, cuenta in contador.items()}
    return frecuencias

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
def sustituir_texto(texto, mapeo):
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
    longitud_minima_palabra = 9
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
diccionario_espanol = generar_diccionario("primero/spanish_words_limpio.txt")

# Frecuencias de los caracteres en el texto cifrado
frecuencias_cifradas = calcular_frecuencias(texto_cifrado)

# Generar mapeos aleatorios y descifrar el texto
listo = False
while not listo:
    # Crear un mapeo aleatorio y sustituir el texto cifrado
    mapeo_aleatorio = crear_mapeo_aleatorio(frecuencias_cifradas, frecuencias_espanol)
    texto_descifrado = sustituir_texto(texto_cifrado, mapeo_aleatorio)
    # Revisar cuantas palabras se encontraron en el texto descifrado
    palabras_correctas, palabras_encontradas = verificar_palabras(texto_descifrado, diccionario_espanol)
    # Si se encontraron al menos 4 palabras, mostrar el texto descifrado y el mapeo
    if palabras_correctas >= 4:
        print("Texto sustituido")
        print(texto_descifrado)
        print(f"\n{palabras_correctas} palabras encontradas en el diccionario")
        print("Palabras encontradas:", palabras_encontradas)
        print("\nAbecedario usado:")
        print(mapeo_aleatorio)
        listo = True
