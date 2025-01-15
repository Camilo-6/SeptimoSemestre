# Representacion 1
# Usara el alfabeto {0,1,2,3,4,5,6,7,8,9,(,),\n,-,,}
# Primero esta un numero entero que representa el numero de vertices de la grafica
# Despues hay un salto de linea
# Luego hay un serie de pares de numeros enteros separados por un guion medio que representan las aristas de la grafica
# Los pares de numeros estan dentro de parentesis y separados por comas

# Ejemplo
# La grafica con los vertices 1, 2 y 3 y las aristas 1-2 y 1-3 se representara como:
# 3\n(1-2),(1-3)

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

# Metodo para obtener la lista de vertices y aristas de la representacion 1 de graficas
# Recibe una cadena con la representacion de la grafica
# Devuelve una lista con los vertices y una lista con las aristas
# Toma complejidad O(n+v+elog(v)+e^2+ve) donde n es la longitud de la cadena, e es el numero de aristas y v es el numero de vertices
# Toma complejidad O(n+v^4) donde n es la longitud de la cadena y v es el numero de vertices
def obtener_listas_representacion1(texto):
    vertices = []
    aristas = []
    # Revisar que la longitud de la cadena sea valida
    # Toma complejidad O(1) https://stackoverflow.com/questions/1115313/cost-of-len-function
    if len(texto) == 0:
        return ValueError("Error cadena vacia")
    # Se separar el numero de vertices y las aristas
    # Toma complejidad O(n) donde n es la longitud de la cadena
    vertices_aristas = texto.split("\n")
    # Revisar que solo existan entre 1 y 2 partes
    # Toma complejidad O(1)
    if len(vertices_aristas) > 2 or len(vertices_aristas) < 1:
        return ValueError("Error representacion incorrecta")
    # Agregar la cantidad de vertices a la lista
    # Toma complejidad O(v) donde v es el numero de vertices
    numero_vertices = 0
    try:
        numero_vertices = int(vertices_aristas[0])
    except:
        return ValueError("Error numero de vertices invalido")
    if numero_vertices < 0:
        return ValueError("Error no hay vertices")
    for i in range(numero_vertices):
        vertices.append(i+1)
    # Si no hay aristas, devolver las listas
    # Toma complejidad O(1)
    if len(vertices_aristas) == 1:
        return vertices, aristas
    # Se separar los pares de numeros en la lista de aristas
    # Toma complejidad O(n) donde n es la longitud de la cadena
    pares = vertices_aristas[1].split(",")
    # Quitar los parentesis de los pares
    # Toma complejidad O(n) donde n es la longitud de la cadena
    for i in range(len(pares)):
        pares[i] = pares[i].replace("(", "").replace(")", "")
    # Separar los numeros de los pares
    # Toma complejidad O(elog(v)) donde e es el numero de aristas y v es el numero de vertices
    aristas = []
    for par in pares:
        # Separar los numeros
        # Toma complejidad O(log(v)) donde v es el numero de vertices, ya que cada vertice es un numero escrito en base 10
        aristas.append(par.split("-"))
        # Revisar que cada arista tenga dos numeros
        # Toma complejidad O(1)
        if len(aristas[-1]) != 2:
            return ValueError("Error arista invalida")
        # Agregar las aristas a la lista
        # Toma complejidad O(1)
        try:
            aristas[-1] = (int(aristas[-1][0]), int(aristas[-1][1]))
        except:
            return ValueError("Error vertice invalido")
    # Eliminar aristas repetidas
    # Toma complejidad O(e^2) donde e es el numero de aristas
    aristas_bonitas = []
    for arista in aristas:
        if arista not in aristas_bonitas:
            aristas_bonitas.append(arista)
    # Revisar que las aristas tengan vertices validos
    # Toma complejidad O(ve) donde v es el numero de vertices y e es el numero de aristas
    for arista in aristas_bonitas:
        if arista[0] not in vertices or arista[1] not in vertices:
            return ValueError("Error las aristas no tienen vertices validos")
    # Devolver las listas
    return vertices, aristas

# Metodo para obtener el numero de vertices y aristas dado una lista de vertices y aristas
# Recibe una lista con los vertices y una lista con las aristas
# Devuelve el numero de vertices y aristas
# Toma complejidad O(1) https://stackoverflow.com/questions/1115313/cost-of-len-function
def obtener_numero_vertices_aristas(vertices, aristas):
    return len(vertices), len(aristas)

# Metodo para convertir una lista de vertices y aristas en una matriz de adyacencia
# Recibe una lista con los vertices y una lista con las aristas
# Devuelve una lista con la matriz de adyacencia
# Toma complejidad O(n^2) donde n es el numero de vertices
def obtener_matriz_adyacencia(vertices, aristas):
    # Crear matriz de len(vertices) x len(vertices) llena de 0
    matriz = [[0 for i in range(len(vertices))] for j in range(len(vertices))]
    # Recorrer las aristas y llenar la matriz (considerar que los vertices empiezan en 1)
    for arista in aristas:
        matriz[arista[0]-1][arista[1]-1] = 1
        matriz[arista[1]-1][arista[0]-1] = 1
    # Devolver la matriz
    return matriz

# Metodo para converir una matriz de adyacencia en una cadena de la representacion 2 de graficas
# Recibe una lista con la matriz de adyacencia
# Devuelve una cadena con la representacion de la matriz de adyacencia
# Toma complejidad O(n^2) donde n es el numero de vertices
def obtener_representacion2(matriz):
    representacion = ""
    # Recorrer la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            representacion += str(matriz[i][j])
    # Devolver la representacion
    return representacion

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

# Metodo para obtener el vertice con mayor grado dado una matriz de adyacencia
# Recibe una matriz de adyacencia
# Devuelve el vertice con mayor grado
# Toma complejidad O(n^2) donde n es el numero de vertices
def obtener_vertice_mayor_grado(matriz):
    maximo = 0
    vertice = 0
    # Contar el grado de cada vertice
    for i in range(len(matriz)):
        grado = 0
        for j in range(len(matriz)):
            grado += matriz[i][j]
        # Actualizar el vertice con mayor grado
        if grado > maximo:
            maximo = grado
            vertice = i
    return vertice

""" https://cp-algorithms.com/graph/euler_path.html https://www.geeksforgeeks.org/eulerian-path-undirected-graph/  
stack St;
put start vertex in St;
until St is empty
  let V be the value at the top of St;
  if degree(V) = 0, then
    add V to the answer;
    remove V from the top of St;
  otherwise
    find any edge coming out of V;
    remove it from the graph;
    put the second end of this edge in St;
"""

# Metodo para obtener el grado de un vertice dado una matriz de adyacencia
# Recibe una matriz de adyacencia y el indice del vertice
# Devuelve el grado del vertice
# Toma complejidad O(n) donde n es el numero de vertices
def obtener_grado_vertice(matriz, vertice):
    grado = 0
    for i in range(len(matriz)):
        grado += matriz[vertice][i]
    return grado

# Metodo para hacer un recorrido DFS en una matriz de adyacencia
# Recibe una matriz de adyacencia, el vertice inicial y una lista de vertices visitados
# Devuelve una lista con los vertices visitados
# Toma complejidad O(n^2) donde n es el numero de vertices https://www.geeksforgeeks.org/time-and-space-complexity-of-dfs-and-bfs-algorithm/
# Toma complejidad O(v+e) donde v es el numero de vertices y e es el numero de aristas
def dfs(matriz, vertice, visitados):
    visitados[vertice] = True
    for i, conectado in enumerate(matriz[vertice]):
        if conectado == 1 and not visitados[i]:
            dfs(matriz, i, visitados)

# Metodo para obtener un camino euleriano dado una matriz de adyacencia
# Recibe una matriz de adyacencia
# Devuelve falso si no existe un camino euleriano, verdadero y una lista de vertices si existe
# Toma complejidad O(n^2 + en) donde n es el numero de vertices y e es el numero de aristas
# Toma complejidad O(n^3) donde n es el numero de vertices
# https://cp-algorithms.com/graph/euler_path.html 
# https://www.geeksforgeeks.org/java-program-to-check-whether-undirected-graph-is-connected-using-dfs/ 
# https://www.geeksforgeeks.org/eulerian-path-undirected-graph/ 
def camino_euleriano_matriz(matriz):
    # Lista de vertices del camino euleriano
    lista = []
    numero_vertices = len(matriz)
    # Paso 1) Checar que el numero de vertices con grado impar sea exactamente 2 o 0
    # Toma complejidad O(n^2) donde n es el numero de vertices
    vertices_impares = []
    for i in range(numero_vertices):
        if obtener_grado_vertice(matriz, i) % 2 == 1:
            vertices_impares.append(i)
    if len(vertices_impares) != 2 and len(vertices_impares) != 0:
        return False, lista
    # Paso 2) Checar que la grafica inducida por los vertices con aristas sea conexa
    # Realizar DFS para revisar los vertices visitados
    # Toma complejidad O(n^2) donde n es el numero de vertices o 0(v+e) donde v es el numero de vertices y e es el numero de aristas
    visitados = [False] * numero_vertices
    dfs(matriz, 0, visitados)
    # Verificar que todos los vertices con aristas hayan sido visitados
    # Toma complejidad O(n^2) donde n es el numero de vertices
    for i in range(numero_vertices):
        if obtener_grado_vertice(matriz, i) > 0 and not visitados[i]:
            return False, lista
    # Paso 3) Encontrar el camino euleriano
    # Toma complejidad O(ve) donde v es el numero de vertices y e es el numero de aristas
    # Toma complejidad O(n^3) donde n es el numero de vertices
    # Pila vacia
    pila = []
    # Si no hay vertices de grado impar, empezar por cualquier vertice
    if len(vertices_impares) == 0:
        vertice_inicial = 0
        pila.append(vertice_inicial)
    # Si hay vertices de grado impar, empezar por uno de ellos
    else:
        vertice_inicial = vertices_impares[0]
        pila.append(vertice_inicial)
    # Mientras la pila no este vacia
    while len(pila) > 0:
        # Obtener el vertice de la cima de la pila
        vertice = pila[-1]
        # Si el vertice no tiene aristas
        if obtener_grado_vertice(matriz, vertice) == 0:
            # Agregar el vertice a la lista
            lista.append(vertice)
            # Quitar el vertice de la pila
            pila.pop()
        else:
            # Si el vertice tiene aristas, encontrar una arista, quitarla y agregar el otro vertice a la pila
            for i in range(numero_vertices):
                if matriz[vertice][i] == 1:
                    matriz[vertice][i] = 0
                    matriz[i][vertice] = 0
                    pila.append(i)
                    break
    # Devolver la lista con los vertices del camino euleriano
    return True, lista

# Metodos para el manejo desde la terminal
import argparse

def ejercicio3(archivo_entrada, archivo_salida):
    try:
        texto = abrir_archivo(archivo_entrada)
        vertices, aristas = obtener_listas_representacion1(texto)
        numero_vertices, numero_aristas = obtener_numero_vertices_aristas(vertices, aristas)
        print("Numero de vertices:", numero_vertices)
        print("Numero de aristas:", numero_aristas)
        matriz = obtener_matriz_adyacencia(vertices, aristas)
        representacion = obtener_representacion2(matriz)
        guardar_texto(representacion, archivo_salida)
        print("Representacion 2 guardada en", archivo_salida)
    except ValueError as e:
        print("Error:", e)


def ejercicio4(archivo_entrada):
    try:
        texto = abrir_archivo(archivo_entrada)
        matriz = obtener_matriz_representacion2(texto)
        numero_vertices, numero_aristas = obtener_numero_vertices_aristas_representacion2(matriz)
        print("Numero de vertices:", numero_vertices)
        print("Numero de aristas:", numero_aristas)
        vertice = obtener_vertice_mayor_grado(matriz)
        print("Vertice con mayor grado:", vertice+1)
        camino, lista = camino_euleriano_matriz(matriz)
        if camino:
            print("Camino euleriano: SI")
            print("Camino:")
            camino_texto = ""
            for vertice in lista:
                camino_texto += str(vertice+1) + " -> "
            print(camino_texto[:-4])
        else:
            print("Camino euleriano: NO")
    except ValueError as e:
        print("Error:", e)

def main():
    # Crear el parser principal
    parser = argparse.ArgumentParser(description="Programa con dos modos de operacion")
    subparsers = parser.add_subparsers(dest='modo', help='Modos de operacion')
    # Ejercicio 3
    parser_ejercicio3 = subparsers.add_parser('ej3', help='Ejercicio 3: archivo de entrada y salida')
    parser_ejercicio3.add_argument('-i', '--input', help='Archivo de entrada', required=True)
    parser_ejercicio3.add_argument('-o', '--output', help='Archivo de salida', required=True)
    # Ejercicio 4: solo archivo de entrada
    parser_ejercicio4 = subparsers.add_parser('ej4', help='Ejercicio 4: solo archivo de entrada')
    parser_ejercicio4.add_argument('-i', '--input', help='Archivo de entrada', required=True)
    # Parsear los argumentos
    args = parser.parse_args()
    # Llamar al modo correspondiente
    if args.modo == 'ej3':
        ejercicio3(args.input, args.output)
    elif args.modo == 'ej4':
        ejercicio4(args.input)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# Ejecutar con python practica.py ej3 -i entrada.txt -o salida.txt
# Ejecutar con python practica.py ej4 -i entrada.txt
# Ejecutado en Fedora 40, Python 3.12.5