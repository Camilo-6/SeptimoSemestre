from unidecode import unidecode

# Limpiar de acentos un texto

# Función para eliminiar caracteres especiales
def eliminar_especiales(texto):
    texto_limpio = unidecode(texto)
    return texto_limpio
    
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

# Leer el archivo de texto
with open('Textos/codigo_da_vinci_2.txt', 'r') as archivo:
    texto = archivo.read()

# Calcular el índice de coincidencia
ic = calcular_indice_coincidencia(texto,'abcdefghijklmnopqrstuvwxyz')
print("Índice de coincidencia:", ic)
