## Aqui podra encontrar 3 cifrados

#Funcion para limpiar un texto de espacios, saltos de linea y caracteres especiales
mcd = lambda x: x

def Limpiar(original, nuevo):
    """Funcion que limpia un texto de espacios, saltos de linea y caracteres especiales"""
    with open(original, 'r') as archivo:
        texto = archivo.read()
    texto = texto.replace(' ', '') #Elimina espacios
    texto = texto.replace('\n', '') #Elimina saltos de linea
    texto = texto.lower() #Convierte todo a minusculas
    texto = ''.join([i for i in texto if i.isalpha()]) #Elimina caracteres especiales
    texto = normalizar(texto) 
    with open(nuevo, 'w') as archivo:
        archivo.write(texto)
    return texto 

def normalizar(texto):
    """Funcion que elimina dieresis y tildes pero mantiene la ñ"""
    a,b = 'áéíóúü','aeiouu'
    trans = str.maketrans(a,b)
    return texto.translate(trans)

##Alfabeto de 27 caracteres con la ñ
alfabeto = 'abcdefghijklmnñopqrstuvwxyz'

## CIFRADO AFIN 


def transformacion_afin_vallida(a,n):
    """Funcion que verifica si una transformacion afin es valida"""
    if mcd(a,n) == 1:
        return True
    return False

def cifrado_afin(original,a,b,alfabeto,nuevo):
    """Funcion que cifra un texto con el cifrado afin"""
    with open(original, 'r') as archivo:
        texto = archivo.read()
    cifrado = ''
    for letra in texto:
        print (alfabeto.index(letra))
        print (a*alfabeto.index(letra))
        print ((a*alfabeto.index(letra) + b))
        cifrado += alfabeto[(a*alfabeto.index(letra) + b)%len(alfabeto)]
    print(cifrado)
    with open(nuevo, 'w') as archivo:
        archivo.write(cifrado)
    return cifrado

##Limpiar('archivos/Texto1.txt', 'archivos/Texto_Limpio.txt')
#Nota a puede tomar cualquier valor que no sea multiplo de 3
#cifrado_afin('archivos/Texto_Limpio.txt', 16, 3, alfabeto, 'archivos/Texto_Cifrado_Afin.txt')
#cifrado_afin('archivos/Texto_Limpio.txt', 5, 15, alfabeto, 'archivos/Texto_Cifrado_Afin_2.txt')

##https://es.stackoverflow.com/questions/135707/c%C3%B3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l

## Hill
#Primero definamos como se van a representar las matrices en el programa

# Es decir dada una matriz de la siguietne forma
# a11  a12
# a21 a22

#matriz = [[a11,a21...],[a12,a22...],...]

matriz_patito = [[7,10,5],[11,4,5],[20,1,7]]

def dividir_texto_bloques(texto, k):
    """Funcion que divide un texto en bloques"""
    bloques = []
    for i in range(0, len(texto), k):
        if (len(texto) - i < k):
            bloques.append(texto[i:] + 'x' * (k - (len(texto) - i)))
        else:
            bloques.append(texto[i:i+k])
    return bloques

def numero_a_letra(secciones, alfabeto):
    """Funcion que convierte un numero a una letra"""
    resultado = []
    for i in range(len(secciones)):
        numero = []
        for j in range(len(secciones[i])):
            numero.append(alfabeto.index(secciones[i][j]))
        resultado.append(numero)
    return resultado


def bloque_por_matriz(bloque, matriz):
    """Funcion que multiplica un bloque por una matriz"""
    resultado = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz)):
            suma += matriz[i][j] * bloque[j]
        resultado.append(suma)
        print(resultado)
    return resultado

def bloques_a_texto(bloques, alfabeto):
    """Funcion que convierte bloques a texto"""
    resultado = ''
    for bloque in bloques:
        for i in range(len(bloque)):
            resultado += alfabeto[bloque[i]%len(alfabeto)]
    return resultado

def cifrado_hill(original, matriz, alfabeto, nuevo):
    """ metodo que cifra un texto con el cifrado hill"""
    with open(original, 'r') as archivo:
        texto = archivo.read()
    secciones = dividir_texto_bloques(texto, len(matriz))
    secciones = numero_a_letra(secciones, alfabeto)
    seccionesCifradas = []
    for bloque in secciones:
        seccionesCifradas.append(bloque_por_matriz(bloque, matriz))
    textoCifrado = bloques_a_texto(seccionesCifradas, alfabeto)
    print(textoCifrado)
    with open(nuevo, 'w') as archivo:
        archivo.write(textoCifrado) 
    return textoCifrado

#cifrado_hill('archivos/Texto_Limpio.txt', matriz_patito, alfabeto, 'archivos/Texto_Cifrado_Hill.txt')
matriz_patito_2 = [[11,8],[12,13]]
#cifrado_hill('archivos/Texto_Limpio.txt', matriz_patito_2, alfabeto, 'archivos/Texto_Cifrado_Hill_2.txt')

#matriz_inversa = [[14,25,3],[14,3,11],[12,13,17]]--> para decifrar solo apliquen el cifrado con esta matriz

# furnte : https://www.youtube.com/watch?v=Y_UFbwClcEc
#        :https://www.youtube.com/watch?v=-EQ8UomTrAQ&t=534s

# Playfair

def generar_matriz_clave(clave, alfabeto):
    """Funcion que genera una matriz clave para el cifrado playfair"""
    clave = clave.replace('j', 'i') #<- Puedes remplazar la letra que quieras 
    clave = clave.replace('ñ', 'n') # <- solo ten en cuenta que deben de ser 25 letras
    matriz = []
    for letra in clave:
        if letra not in matriz:
            matriz.append(letra)
    for letra in alfabeto:
        if letra not in matriz and letra != 'j' and letra != 'ñ':
            matriz.append(letra)
    return matriz_cuadrada(matriz, 5)

def matriz_cuadrada (matriz,n):
    """Funcion que convierte una matriz en una matriz cuadrada"""
    matriz_cuadrada = []
    for i in range(0, len(matriz), n):
        matriz_cuadrada.append(matriz[i:i+n])
    return matriz_cuadrada

def dividir_en_tuplas(texto):
    """Funcion que divide un texto en tuplas"""
    texto = texto.replace('j', 'i')
    texto = texto.replace('ñ', 'n')
    tuplas = []
    for i in range(0, len(texto), 2):
        evaluar = texto[i:i+2]
        if len(evaluar) == 1:
            evaluar += 'x' #<- Puede ser la letra que quieras siempre cuando este en la tabla
        if evaluar[0] == evaluar[1]:
            evaluar = evaluar[0] + 'x'
        tuplas.append(evaluar)
    return tuplas

def obtener_posicion(letra, matriz):
    """Funcion que obtiene la posicion de una letra en una matriz"""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == letra:
                return (i,j)
    return None

def casos(tupla, matriz):
    """Funcion que maneja los casos del cifrado playfair"""
    pos1 = obtener_posicion(tupla[0], matriz)
    pos2 = obtener_posicion(tupla[1], matriz)
    if pos1[0] == pos2[0]:
        return (matriz[pos1[0]][(pos1[1] + 1)%5] + matriz[pos2[0]][(pos2[1] + 1)%5])
    elif pos1[1] == pos2[1]:
        return (matriz[(pos1[0] + 1)%5][pos1[1]] + matriz[(pos2[0] + 1)%5][pos2[1]])
    else:
        return (matriz[pos1[0]][pos2[1]] + matriz[pos2[0]][pos1[1]])


def cifrado_playfair(original, clave, alfabeto, nuevo):
    """Funcion que cifra un texto con el cifrado playfair"""
    with open(original, 'r') as archivo:
        texto = archivo.read()
    matriz = generar_matriz_clave(clave, alfabeto)
    tuplas = dividir_en_tuplas(texto)
    cifrado = ''
    for tupla in tuplas:
        cifrado += casos(tupla, matriz)
    with open(nuevo, 'w') as archivo:
        archivo.write(cifrado)
    return cifrado

#cifrado_playfair('archivos/Texto_Limpio.txt', 'criptografia', alfabeto, 'archivos/Texto_Playfair.txt')
#cifrado_playfair('archivos/Texto_Limpio.txt', 'patitos', alfabeto, 'archivos/Texto_Playfair_2.txt')

def encontrar_a_c():
    valores = []
    for a in range(26):
        for c in range(26):
            for b in range(26):
                for d in range(26):
                    det = a*d - b*c
                    det = det % 26
                    if mcd(det, 26) == 1:
                        valores.append((a, b, c, d))
    return valores
