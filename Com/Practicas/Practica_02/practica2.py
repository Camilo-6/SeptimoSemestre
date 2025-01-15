# Metodo para abrir un archivo y obtener el texto dentro
# Recibe una cadena con el nombre del archivo
# Devuelve una cadena con el texto dentro del archivo
def abrir_archivo(archivo):
    try:
        with open(archivo, "r") as file:
            texto = file.read()
        return texto
    except:
        return ValueError("Error al abrir el archivo")
    
# Metodo para guardar un texto en un archivo
# Recibe una cadena con el texto y una cadena con el nombre del archivo
# Devuelve True si se guardo correctamente
def guardar_texto(texto, archivo):
    try:
        with open(archivo, "w") as file:
            file.write(texto)
        return True
    except:
        return False
    
# Representacion 2
# Usara el alfabeto {0,1}
# Usando la matriz de adyacencia de la grafica, si existe una arista entre los vertices i y j se representara con un 1 y si no con un 0
# La matriz se representara como una cadena de numeros binarios sin separacion, donde solo se podran los valores de la matriz de adyacencia
# Ejemplo
# La grafica con los vertices 1, 2 y 3 y las aristas 1-2 y 1-3 se representara como:
# 011100100
# Ya que la matriz de adyacencia es:
# 0 1 1
# 1 0 0
# 1 0 0

# Metodo para obtener la matriz de adyacencia de la representacion 2 de graficas
# Recibe una cadena con la representacion de la grafica
# Devuelve una cadena con la representacion de la matriz de adyacencia
# Toma complejidad O(n) donde n es la longitud de la cadena
# len() toma complejidad O(1) https://stackoverflow.com/questions/1115313/cost-of-len-function
def obtener_matriz_representacion2(texto):
    # Revisamos que la longitud de la cadena sea valida
    if len(texto) == 0:
        return ValueError("Error cadena vacia")
    # Verificar que la longitud de la cadenas sea el cuadrado de un numero entero
    if len(texto) != int(len(texto)**0.5)**2:
        return ValueError("Error longitud de la cadena invalida")
    # Revisar que solo existan 0 y 1 en la cadena
    for caracter in texto:
        if caracter != "0" and caracter != "1":
            return ValueError("Error caracter invalido")
    # Crear la matriz de adyacente
    tamano = int(len(texto)**0.5)
    matriz = [[0 for i in range(tamano)] for j in range(tamano)]
    # Llenar la matriz
    for i in range(tamano):
        for j in range(tamano):
            matriz[i][j] = texto[i*tamano+j]
            matriz[i][j] = int(matriz[i][j])
    # Devolver la matriz
    return matriz

# Metodo para obtener el numero de vertices y aristas dado una matriz de adyacencia
# Recibe una matriz de adyacencia
# Devuelve el numero de vertices y aristas
# Toma complejidad O(n^2) donde n es el numero de vertices
def obtener_numero_vertices_aristas_representacion2(matriz):
    vertices = len(matriz)
    aristas = 0
    # Contar las aristas
    for i in range(len(matriz)):
        for j in range(i, len(matriz)):
            if matriz[i][j] == 1:
                aristas += 1
    return vertices, aristas

# Representacion para el certificado
# Sera una permutacion de los vertices, es decir, una lista de vertices sin repetir alguno y sin faltar alguno
# La permutacion de los vertices representara la ruta Hamiltoniana, es decir, el camino que recorre todos los vertices
# Los certificados se codificaran como numeros enteros (donde cada numero representa un vertice) y se separaran por comas
# Ejemplo
# La grafica con los vertices 0, 1 y 2 y las aristas 0-1 y 0-2
# Un posible certificado seria [1, 0, 2] y se codificaria como "1,0,2"

import random

# Metodo para generar aleatoriamente un certificado
# Recibe una matriz de adyacencia
# Devuelve un certificado
# Toma complejidad O(n^2) donde n es el numero de vertices
def generar_certificado(matriz):
    vertices = len(matriz)
    lista = []
    lista_certificado = []
    # Crear una lista con los vertices
    # Toma complejidad O(n) donde n es el numero de vertices
    for i in range(vertices):
        lista.append(i)
    # Obtener la longitud de la lista
    # Toma complejidad O(1) https://stackoverflow.com/questions/1115313/cost-of-len-function
    longitud = len(lista)
    # Generar un certificado aleatorio
    # Toma complejidad O(n^2) donde n es el numero de vertices
    while longitud > 0:
        # Generar un indice aleatorio
        # Toma complejidad O(log n) https://stackoverflow.com/questions/29461787/what-is-big-o-runtime-of-the-standard-random-number-generator-in-python-worst
        indice = random.randint(0, longitud-1)
        # Obtener el vertice en el indice
        # Toma complejidad O(n) https://wiki.python.org/moin/TimeComplexity
        vertice = lista.pop(indice)
        # Agregar el vertice a la lista
        # Toma complejidad O(1) https://wiki.python.org/moin/TimeComplexity
        lista_certificado.append(vertice)
        longitud -= 1
    return lista_certificado

# Metodo para guardar un certificado en un archivo
# Recibe una cadena con el nombre del archivo y un certificado
# Toma complejidad O(n) donde n es el numero de vertices, esto ignorando la complejidad de guardar texto en un archivo y transformar un numero a una cadena
def guardar_certificado(archivo, certificado):
    # Converitr el certificado a una cadena
    cadena = ""
    # Agregar cada vertice a la cadena
    # Toma complejidad O(n) donde n es el numero de vertices
    for vertice in certificado:
        # Convertir el vertice a una cadena y agregarlo a la cadena
        cadena += str(vertice) + ","
    cadena = cadena[:-1]
    # Guardar la cadena en un archivo
    guardar_texto(cadena, archivo)

# Metodo para obtener el primer y ultimo vertice de un certificado
# Recibe un certificado
# Devuelve el primer y ultimo vertice
# Toma complejidad O(1)
def obtener_primer_ultimo_vertice(certificado):
    return certificado[0], certificado[-1]

# Metodo para obtener el certificado en una cadena de su representacion
# Recibe una cadena con la representacion del certificado
# Devuelve un certificado
# Toma complejidad O(nl) donde l es la longitud de la cadena y n es el numero de vertices, esto ignorando la complejidad de convertir una cadena a un numero
def obtener_certificado(cadena):
    # Separar la cadena por comas
    # Toma complejidad O(l) donde l es la longitud de la cadena
    certificado = cadena.split(",")
    # Convertir los vertices a enteros
    # Toma complejidad O(n) donde n es el numero de vertices de la grafica a la que pertenece el certificado
    for i in range(len(certificado)):
        # Convertir el vertice a un entero y reemplazarlo en la lista
        certificado[i] = int(certificado[i])
    return certificado

# Metodo para verificar si un certificado induce una ruta Hamiltoniana existente en una grafica
# Recibe una matriz de adyacencia para la grafica y un certificado para la ruta Hamiltoniana
# Devuelve True si el certificado es valido, False en caso contrario
# Toma complejidad O(n) donde n es el numero de vertices de la grafica
def verificar_certificado(matriz, certificado):
    # Generamos las aristas que tenemos que verificar que existan
    # Toma complejidad O(n) donde n es el numero de vertices de la grafica
    aristas = []
    for i in range(len(certificado)-1):
        # Agregar la arista a la lista
        # Toma complejidad O(1) https://wiki.python.org/moin/TimeComplexity
        aristas.append((certificado[i], certificado[i+1]))
    # Verificamos que las aristas existan en la grafica
    # Toma complejidad O(n) donde n es el numero de vertices de la grafica
    for arista in aristas:
        # Verificar que la arista exista
        # Toma complejidad O(1)
        if matriz[arista[0]][arista[1]] == 0:
            return False
    return True

# Metodos para el manejo desde la terminal
import argparse

def ejercicio2(archivo_entrada, archivo_salida):
    try:
        texto = abrir_archivo(archivo_entrada)
        representacion = obtener_matriz_representacion2(texto)
        cert = generar_certificado(representacion)
        guardar_certificado(archivo_salida, cert)
        print("Certificado guardado en", archivo_salida)
    except ValueError as e:
        print("Error:", e)

def ejercicio3(archivo_entrada_1, archivo_entrada_2):
    try:
        texto1 = abrir_archivo(archivo_entrada_1)
        texto2 = abrir_archivo(archivo_entrada_2)
        matriz = obtener_matriz_representacion2(texto1)
        certificado = obtener_certificado(texto2)
        vertices, aristas = obtener_numero_vertices_aristas_representacion2(matriz)
        primer_vertice, ultimo_vertice = obtener_primer_ultimo_vertice(certificado)
        cert_valido = verificar_certificado(matriz, certificado)
        print("Numero de vertices:", vertices)
        print("Numero de aristas:", aristas)
        print("Primer vertice de la ruta inducida:", primer_vertice)
        print("Ultimo vertice de la ruta inducida:", ultimo_vertice)
        respuesta = "Si" if cert_valido else "No"
        print("¿El ejemplar, con el certificado dado, satisface la condicion de pertenencia al lenguaje correspondiente? ", respuesta)
    except ValueError as e:
        print("Error:", e)

def main():
    # Crear el parser principal
    parser = argparse.ArgumentParser(description="Programa con dos modos de operacion")
    subparsers = parser.add_subparsers(dest='modo', help='Modos de operacion')
    # Ejercicio 2
    parser_ejercicio2 = subparsers.add_parser('ej2', help='Ejercicio 2: archivo de entrada y salida')
    parser_ejercicio2.add_argument('-i', '--entrada', help='Archivo de entrada, que contiene la representacion de la grafica', required=True)
    parser_ejercicio2.add_argument('-o', '--salida', help='Archivo de salida, donde se guardara el certificado', required=True)
    # Ejercicio 3
    parser_ejercicio3 = subparsers.add_parser('ej3', help='Ejercicio 3: dos archivos de entrada')
    parser_ejercicio3.add_argument('-g', '--grafica', help='Archivo que contiene la representacion de la grafica', required=True)
    parser_ejercicio3.add_argument('-c', '--certificado', help='Archivo que contiene el certificado', required=True)
    # Parsear los argumentos
    args = parser.parse_args()
    # Llamar al modo correspondiente
    if args.modo == 'ej2':
        ejercicio2(args.entrada, args.salida)
    elif args.modo == 'ej3':
        ejercicio3(args.grafica, args.certificado)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# Ejemplo de uso
# python3 practica2.py ej2 -i grafica.txt -o certificado.txt
# python3 practica2.py ej3 -g grafica.txt -c certificado.txt
# Codigo ejecutado en Fedora 40 Workstation y Python 3.12.6

# Para las complejidades de los algoritmos se omitieron las complejidades de guardar y leer archivos
# Ademas las complejidades de las operaciones de transformar un numero a una cadena y transformar una cadena a un numero
# Pero la complejidad de convertir un numero N a una cadena es O(log N)
# Y la complejidad de convertir una cadena de longitud L a un numero es O(L)
# https://stackoverflow.com/questions/4483189/convert-string-to-number-vice-versa-complexity
# Con eso en cuenta, las complejidades de los metodos se podrian ajustar, pero para facilitar la lectura y entendimiento de las complejidades se omitieron
# Al final son complejidades polinomiales y no afectan en que tan rapido sean los algoritmos


