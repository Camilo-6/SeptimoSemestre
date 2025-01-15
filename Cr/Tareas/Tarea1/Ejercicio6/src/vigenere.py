## Programa para cifrar un archivo usando el cifrado de Vigenere
"""
from unidecode import unidecode

# Metodo para quitar espacios y saltos de linea de un archivo de texto y guardar el resultado en otro archivo
def Limpiar(original, nuevo):
    with open(original, 'r') as archivo:
        texto = archivo.read()
    texto = unidecode(texto)
    texto = texto.replace(' ', '')
    texto = texto.replace('\n', '')
    texto = texto.lower()
    texto = ''.join([i for i in texto if not i.isdigit()])
    texto = ''.join([i for i in texto if i.isalpha()])
    with open(nuevo, "w") as archivo:
        archivo.write(texto)
    return texto
"""
    

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


# Función para cifrar un texto a vigenere

def cifrar_vigenere(texto, clave, tablita, nuevo):
    salto = False
    with open(texto, 'r') as archivo:
        texto = archivo.read()
    texto_cifrado = ""
    print(len(clave))
    for i in range(len(texto)):
        letra = texto[i]
        fila = ord(clave[i % len(clave)]) - 97
        columna = ord(letra) - 97
        texto_cifrado += tablita[fila][columna]
    with open(nuevo, "w") as archivo:
        archivo.write(texto_cifrado)

    return texto_cifrado

    
## Apartir de la siguiente linea quite el # para probar el código

#Limpiar('archivos/codigo_da_vinci.txt', 'archivos/codigo_da_vinci_limpio.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'nananan', tablita, 'archivos/vinci_72.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'nananana', tablita, 'archivos/vinci_82.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'nanananan', tablita, 'archivos/vinci_92.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'nanananana', tablita, 'archivos/vinci_102.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'nananananan', tablita, 'archivos/vinci_112.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'nananananana', tablita, 'archivos/vinci_12.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'jarjarj', tablita, 'archivos/3Alfabetos/vinci_73.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'jarjarja', tablita, 'archivos/3Alfabetos/vinci_83.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'jarjarjar', tablita, 'archivos/3Alfabetos/vinci_93.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'jarjarjarr', tablita, 'archivos/3Alfabetos/vinci_103.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'jarjarjaarj', tablita, 'archivos/3Alfabetos/vinci_113.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'jarjarjaaajr', tablita, 'archivos/3Alfabetos/vinci_123.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'foxyfox', tablita, 'archivos/4Alfabetos/vinci_74.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'foxyxxxo', tablita, 'archivos/4Alfabetos/vinci_84.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'foxyxyfyo', tablita, 'archivos/4Alfabetos/vinci_94.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'foxyxyfoyx', tablita, 'archivos/4Alfabetos/vinci_104.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'foxyxxfoxyy', tablita, 'archivos/4Alfabetos/vinci_114.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'foxyyyfoxfox', tablita, 'archivos/4Alfabetos/vinci_124.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'soreyso', tablita, 'archivos/5Alfabetos/vinci_75.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'soreyyso', tablita, 'archivos/5Alfabetos/vinci_85.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'soreyrere', tablita, 'archivos/5Alfabetos/vinci_95.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'soreyreyso', tablita, 'archivos/5Alfabetos/vinci_105.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'soreysoyeso', tablita, 'archivos/5Alfabetos/vinci_115.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'soreysoyreor', tablita, 'archivos/5Alfabetos/vinci_125.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'mikleom', tablita, 'archivos/6Alfabetos/vinci_76.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'mikleomi', tablita, 'archivos/6Alfabetos/vinci_86.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'mikleomkl', tablita, 'archivos/6Alfabetos/vinci_96.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'mikleomeee', tablita, 'archivos/6Alfabetos/vinci_106.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'mikleomleol', tablita, 'archivos/6Alfabetos/vinci_116.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'mikleomiikem', tablita, 'archivos/6Alfabetos/vinci_126.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'lazurov', tablita, 'archivos/lAlfabetos/vinci_77.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'lazurove', tablita, 'archivos/lAlfabetos/vinci_88.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'abcdefghi', tablita, 'archivos/lAlfabetos/vinci_99.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'caseunhoxy', tablita, 'archivos/lAlfabetos/vinci_1010.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'matesupzyrw', tablita, 'archivos/lAlfabetos/vinci_1111.txt')
#cifrar_vigenere('archivos/codigo_da_vinci_limpio.txt', 'comalzerywxn', tablita, 'archivos/lAlfabetos/vinci_1212.txt')
"""
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'ebebebe', tablita, 'archivos/textos_patito/patito_72.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'sbsmssb', tablita, 'archivos/textos_patito/patito_73.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'izipopi', tablita, 'archivos/textos_patito/patito_74.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'hyyowwi', tablita, 'archivos/textos_patito/patito_75.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'aeiouza', tablita, 'archivos/textos_patito/patito_76.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'rapidos', tablita, 'archivos/textos_patito/patito_77.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'ebebebee', tablita, 'archivos/textos_patito/patito_82.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'sbsmssbm', tablita, 'archivos/textos_patito/patito_83.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'izipopiz', tablita, 'archivos/textos_patito/patito_84.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'hyyowwio', tablita, 'archivos/textos_patito/patito_85.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'aeiouzaz', tablita, 'archivos/textos_patito/patito_86.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'rapidosz', tablita, 'archivos/textos_patito/patito_88.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'ebebebeeb', tablita, 'archivos/textos_patito/patito_92.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'sbsmssbmb', tablita, 'archivos/textos_patito/patito_93.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'izipopizp', tablita, 'archivos/textos_patito/patito_94.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'hyyowwiow', tablita, 'archivos/textos_patito/patito_95.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'aeiouzazo', tablita, 'archivos/textos_patito/patito_96.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'rapidoszu', tablita, 'archivos/textos_patito/patito_99.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'ebebebeebe', tablita, 'archivos/textos_patito/patito_102.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'sbsmssbmbs', tablita, 'archivos/textos_patito/patito_103.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'izipopizpo', tablita, 'archivos/textos_patito/patito_104.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'hyyowwiowi', tablita, 'archivos/textos_patito/patito_105.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'aeiouzazou', tablita, 'archivos/textos_patito/patito_106.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'rapidoszum', tablita, 'archivos/textos_patito/patito_1010.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'ebebebeebeb', tablita, 'archivos/textos_patito/patito_112.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'sbsmssbmbsm', tablita, 'archivos/textos_patito/patito_113.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'izipopizpoz', tablita, 'archivos/textos_patito/patito_114.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'hyyowwiowih', tablita, 'archivos/textos_patito/patito_115.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'aeiouzazoue', tablita, 'archivos/textos_patito/patito_116.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'rapidoszumx', tablita, 'archivos/textos_patito/patito_1111.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'ebebebeebebb', tablita, 'archivos/textos_patito/patito_122.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'sbsmssbmbsmm', tablita, 'archivos/textos_patito/patito_123.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'izipopizpozi', tablita, 'archivos/textos_patito/patito_124.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'hyyowwiowihy', tablita, 'archivos/textos_patito/patito_125.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'aeiouzazouea', tablita, 'archivos/textos_patito/patito_126.txt')
cifrar_vigenere('archivos/textos_patito/patito_limpio.txt', 'rapidoszumxf', tablita, 'archivos/textos_patito/patito_1212.txt')
"""


