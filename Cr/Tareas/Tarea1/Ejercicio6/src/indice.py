#from unidecode import unidecode

# Limpiar de acentos un texto

"""
# Función para eliminiar caracteres especiales
def eliminar_especiales(texto):
    texto_limpio = unidecode(texto)
    return texto_limpio
"""

# Calcular el indice de coincidencia de un texto dado un alfabeto
def calcular_indice_coincidencia(texto, alfabeto):
    # Contar la frecuencia de cada letra
    with open(texto, 'r') as archivo:
        texto = archivo.read()
    frecuencias = {letra: 0 for letra in alfabeto}
    for letra in texto:
        letra = letra.lower()
        if letra in frecuencias:
            frecuencias[letra] += 1
    # Calcular el total de letras
    total_letras = sum(frecuencias.values())
    print("Total de letras:", total_letras)
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


abecedario= 'abcdefghijklmnopqrstuvwxyz'

# Calcular el índice de coincidencia

#print("r=2,l=7", calcular_indice_coincidencia('archivos/vinci_72.txt', abecedario))
#print("r=2,l=8", calcular_indice_coincidencia('archivos/vinci_82.txt', abecedario))
#print("r=2,l=9", calcular_indice_coincidencia('archivos/vinci_92.txt', abecedario))
#print("r=2,l=10", calcular_indice_coincidencia('archivos/vinci_102.txt', abecedario))
#print("r=2,l=11", calcular_indice_coincidencia('archivos/vinci_112.txt', abecedario))
#print("r=2,l=12", calcular_indice_coincidencia('archivos/vinci_122.txt', abecedario))
#print("r=3, l=7",calcular_indice_coincidencia('archivos/3Alfabetos/vinci_73.txt', abecedario))
#print("r=3, l=8",calcular_indice_coincidencia('archivos/3Alfabetos/vinci_83.txt', abecedario))
#print("r=3, l=9",calcular_indice_coincidencia('archivos/3Alfabetos/vinci_93.txt', abecedario))
#print("r=3, l=10",calcular_indice_coincidencia('archivos/3Alfabetos/vinci_103.txt', abecedario))
#print("r=3, l=11",calcular_indice_coincidencia('archivos/3Alfabetos/vinci_113.txt', abecedario))
#print("r=3, l=12",calcular_indice_coincidencia('archivos/3Alfabetos/vinci_123.txt', abecedario))
#print("r=4, l=7",calcular_indice_coincidencia('archivos/4Alfabetos/vinci_74.txt', abecedario))
#print("r=4, l=8",calcular_indice_coincidencia('archivos/4Alfabetos/vinci_84.txt', abecedario))
#print("r=4, l=9",calcular_indice_coincidencia('archivos/4Alfabetos/vinci_94.txt', abecedario))
#print("r=4, l=10",calcular_indice_coincidencia('archivos/4Alfabetos/vinci_104.txt', abecedario))
#print("r=4, l=11",calcular_indice_coincidencia('archivos/4Alfabetos/vinci_114.txt', abecedario))
#print("r=4, l=12",calcular_indice_coincidencia('archivos/4Alfabetos/vinci_124.txt', abecedario))
#print("r=5, l=7",calcular_indice_coincidencia('archivos/5Alfabetos/vinci_75.txt', abecedario))
#print("r=5, l=8",calcular_indice_coincidencia('archivos/5Alfabetos/vinci_85.txt', abecedario))
#print("r=5, l=9",calcular_indice_coincidencia('archivos/5Alfabetos/vinci_95.txt', abecedario))
#print("r=5, l=10",calcular_indice_coincidencia('archivos/5Alfabetos/vinci_105.txt', abecedario))
#print("r=5, l=11",calcular_indice_coincidencia('archivos/5Alfabetos/vinci_115.txt', abecedario))
#print("r=5, l=12",calcular_indice_coincidencia('archivos/5Alfabetos/vinci_125.txt', abecedario))
#print("r=6, l=7",calcular_indice_coincidencia('archivos/6Alfabetos/vinci_76.txt', abecedario))
#print("r=6, l=8",calcular_indice_coincidencia('archivos/6Alfabetos/vinci_86.txt', abecedario))
#print("r=6, l=9",calcular_indice_coincidencia('archivos/6Alfabetos/vinci_96.txt', abecedario))
#print("r=6, l=10",calcular_indice_coincidencia('archivos/6Alfabetos/vinci_106.txt', abecedario))
#print("r=6, l=11",calcular_indice_coincidencia('archivos/6Alfabetos/vinci_116.txt', abecedario))
#print("r=6, l=12",calcular_indice_coincidencia('archivos/6Alfabetos/vinci_126.txt', abecedario))
"""
print("r=l=7",calcular_indice_coincidencia('archivos/lAlfabetos/vinci_77.txt', abecedario))
print("r=l=8",calcular_indice_coincidencia('archivos/lAlfabetos/vinci_88.txt', abecedario))
print("r=l=9",calcular_indice_coincidencia('archivos/lAlfabetos/vinci_99.txt', abecedario))
print("r=l=10",calcular_indice_coincidencia('archivos/lAlfabetos/vinci_1010.txt', abecedario))
print("r=l=11",calcular_indice_coincidencia('archivos/lAlfabetos/vinci_1111.txt', abecedario))
print("r=l=12",calcular_indice_coincidencia('archivos/lAlfabetos/vinci_1212.txt', abecedario))
"""

# Metodo para limpar el texto de archivo, solo dejando letra minusculas, sin acentos, sin espacios y sin caracteres especiales
def limpiar_texto(archivo, archivo_limpio):
    with open(archivo, 'r') as file:
        texto = file.read()
    texto_limpio = ''
    for caracter in texto:
        caracter_limpio = limpiar_caracter(caracter)
        texto_limpio += caracter_limpio
    with open(archivo_limpio, 'w') as file:
        file.write(texto_limpio)
    # Imprimir la cantidad de caracteres limpios
    print("Cantidad de caracteres limpios:", len(texto_limpio))

# Metodo que recibe un caracter y lo limpia, solo dejando letra minusculas, sin acentos, sin espacios y sin caracteres especiales
def limpiar_caracter(caracter):
    if caracter == 'A' or caracter == 'Á' or caracter == 'a' or caracter == 'á':
        return 'a'
    elif caracter == 'B' or caracter == 'b':
        return 'b'
    elif caracter == 'C' or caracter == 'c':
        return 'c'
    elif caracter == 'D' or caracter == 'd':
        return 'd'
    elif caracter == 'E' or caracter == 'É' or caracter == 'e' or caracter == 'é':
        return 'e'
    elif caracter == 'F' or caracter == 'f':
        return 'f'
    elif caracter == 'G' or caracter == 'g':
        return 'g'
    elif caracter == 'H' or caracter == 'h':
        return 'h'
    elif caracter == 'I' or caracter == 'Í' or caracter == 'i' or caracter == 'í':
        return 'i'
    elif caracter == 'J' or caracter == 'j':
        return 'j'
    elif caracter == 'K' or caracter == 'k':
        return 'k'
    elif caracter == 'L' or caracter == 'l':
        return 'l'
    elif caracter == 'M' or caracter == 'm':
        return 'm'
    elif caracter == 'N' or caracter == 'n' or caracter == 'Ñ' or caracter == 'ñ':
        return 'n'
    elif caracter == 'O' or caracter == 'Ó' or caracter == 'o' or caracter == 'ó':
        return 'o'
    elif caracter == 'P' or caracter == 'p':
        return 'p'
    elif caracter == 'Q' or caracter == 'q':
        return 'q'
    elif caracter == 'R' or caracter == 'r':
        return 'r'
    elif caracter == 'S' or caracter == 's':
        return 's'
    elif caracter == 'T' or caracter == 't':
        return 't'
    elif caracter == 'U' or caracter == 'Ú' or caracter == 'u' or caracter == 'ú':
        return 'u'
    elif caracter == 'V' or caracter == 'v':
        return 'v'
    elif caracter == 'W' or caracter == 'w':
        return 'w'
    elif caracter == 'X' or caracter == 'x':
        return 'x'
    elif caracter == 'Y' or caracter == 'y':
        return 'y'
    elif caracter == 'Z' or caracter == 'z':
        return 'z'
    else:
        return ''

"""
print(calcular_indice_coincidencia('archivos/textos_patito/patito_72.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_73.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_74.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_75.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_76.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_77.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_82.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_83.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_84.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_85.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_86.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_88.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_92.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_93.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_94.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_95.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_96.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_99.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_102.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_103.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_104.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_105.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_106.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_1010.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_112.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_113.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_114.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_115.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_116.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_1111.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_122.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_123.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_124.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_125.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_126.txt', abecedario))
print(calcular_indice_coincidencia('archivos/textos_patito/patito_1212.txt', abecedario))
"""


