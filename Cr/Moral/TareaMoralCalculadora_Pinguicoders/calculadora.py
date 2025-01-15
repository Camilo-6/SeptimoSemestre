from functools import cmp_to_key

# Equipo Pinguicoders
# Arrieta Mancera Luis Sebastian - 318174116
# Cruz Cruz Alan Josue - 319327133
# Garcia Ponce Jose Camilo - 319210536
# Matute Canton Sara Lorena - 319331622

# Calculadora para los campos finitos de 4, 8 y 64 elementos
# Para el campo finito de 4 elementos se utiliza el polinomio x^2 + x + 1
# Para el campo finito de 8 elementos se utiliza el polinomio x^3 + x^2 + 1
# Para el campo finito de 64 elementos se utiliza el polinomio x^6 + x + 1
# Soporta las operaciones de suma, resta, multiplicacion, division y exponenciacion

# Elementos del campo finito de 4 elementos
cf4 = ["0", "1", "a", "a+1"]
cf4_e = ["0", "a^0", "a^1", "a^2"]
# Tabla de suma para el campo finito de 4 elementos
suma4 = [["0", "1", "a", "a+1"],
         ["1", "0", "a+1", "a"],
         ["a", "a+1", "0", "1"],
         ["a+1", "a", "1", "0"]]
# Tabla de multiplicacion para el campo finito de 4 elementos
mult4 = [["0", "0", "0", "0"],
         ["0", "1", "a", "a+1"],
         ["0", "a", "a+1", "1"],
         ["0", "a+1", "1", "a"]]

# Elementos del campo finito de 8 elementos
cf8 = ["0", "1", "a", "a+1", "a^2", "a^2+1", "a^2+a", "a^2+a+1"]
cf8_e = ["0", "a^0", "a^1", "a^5", "a^2", "a^3", "a^6", "a^4"]
# Tabla de suma para el campo finito de 8 elementos
suma8 = [["0", "1", "a", "a+1", "a^2", "a^2+1", "a^2+a", "a^2+a+1"],
         ["1", "0", "a+1", "a", "a^2+1", "a^2", "a^2+a+1", "a^2+a"],
         ["a", "a+1", "0", "1", "a^2+a", "a^2+a+1", "a^2", "a^2+1"],
         ["a+1", "a", "1", "0", "a^2+a+1", "a^2+a", "a^2+1", "a^2"],
         ["a^2", "a^2+1", "a^2+a", "a^2+a+1", "0", "1", "a", "a+1"],
         ["a^2+1", "a^2", "a^2+a+1", "a^2+a", "1", "0", "a+1", "a"],
         ["a^2+a", "a^2+a+1", "a^2", "a^2+1", "a", "a+1", "0", "1"],
         ["a^2+a+1", "a^2+a", "a^2+1", "a^2", "a+1", "a", "1", "0"]]
# Tabla de multiplicacion para el campo finito de 8 elementos
mult8 = [["0", "0", "0", "0", "0", "0", "0", "0"],
         ["0", "1", "a", "a+1", "a^2", "a^2+1", "a^2+a", "a^2+a+1"],
         ["0", "a", "a^2", "a^2+a", "a^2+1", "a^2+a+1", "1", "a+1"],
         ["0", "a+1", "a^2+a", "a^2+1", "1", "a", "a^2+a+1", "a^2"],
         ["0", "a^2", "a^2+1", "1", "a^2+a+1", "a+1", "a", "a^2+a"],
         ["0", "a^2+1", "a^2+a+1", "a", "a+1", "a^2+a", "a^2", "1"],
         ["0", "a^2+a", "1", "a^2+a+1", "a", "a^2", "a+1", "a^2+1"],
         ["0", "a^2+a+1", "a+1", "a^2", "a^2+a", "1", "a^2+1", "a"]]

# Elementos del campo finito de 64 elementos
cf64 = ["0", "1", "a", "a+1", "a^2", "a^2+1", "a^2+a", "a^2+a+1",
        "a^3", "a^3+1", "a^3+a", "a^3+a+1", "a^3+a^2", "a^3+a^2+1", "a^3+a^2+a", "a^3+a^2+a+1",
        "a^4", "a^4+1", "a^4+a", "a^4+a+1", "a^4+a^2", "a^4+a^2+1", "a^4+a^2+a", "a^4+a^2+a+1",
        "a^4+a^3", "a^4+a^3+1", "a^4+a^3+a", "a^4+a^3+a+1", "a^4+a^3+a^2", "a^4+a^3+a^2+1", "a^4+a^3+a^2+a", "a^4+a^3+a^2+a+1",
        "a^5", "a^5+1", "a^5+a", "a^5+a+1", "a^5+a^2", "a^5+a^2+1", "a^5+a^2+a", "a^5+a^2+a+1",
        "a^5+a^3", "a^5+a^3+1", "a^5+a^3+a", "a^5+a^3+a+1", "a^5+a^3+a^2", "a^5+a^3+a^2+1", "a^5+a^3+a^2+a", "a^5+a^3+a^2+a+1",
        "a^5+a^4", "a^5+a^4+1", "a^5+a^4+a", "a^5+a^4+a+1", "a^5+a^4+a^2", "a^5+a^4+a^2+1", "a^5+a^4+a^2+a", "a^5+a^4+a^2+a+1",
        "a^5+a^4+a^3", "a^5+a^4+a^3+1", "a^5+a^4+a^3+a", "a^5+a^4+a^3+a+1", "a^5+a^4+a^3+a^2", "a^5+a^4+a^3+a^2+1", "a^5+a^4+a^3+a^2+a", "a^5+a^4+a^3+a^2+a+1"]

cf64_e = ["0", "a^0", "a^1", "a^6", "a^2", "a^12", "a^7", "a^26",
        "a^3", "a^32", "a^13", "a^35", "a^8", "a^48", "a^27", "a^18",
        "a^4", "a^24", "a^33", "a^16", "a^14", "a^52", "a^36", "a^54",
        "a^9", "a^45", "a^49", "a^38", "a^28", "a^41", "a^19", "a^56",
        "a^5", "a^62", "a^25", "a^11", "a^34", "a^31", "a^17", "a^47",
        "a^15", "a^23", "a^53", "a^51", "a^37", "a^44", "a^55", "a^40",
        "a^10", "a^61", "a^46", "a^30", "a^50", "a^22", "a^39", "a^43",
        "a^29", "a^60", "a^42", "a^21", "a^20", "a^59", "a^57", "a^58"]
# Tabla de suma para el campo finito de 64 elementos
suma64 = [] # TODO
# Tabla de multiplicacion para el campo finito de 64 elementos
mult64 = [] # TODO

# Operaciones, van a recibir los indices de los elementos en los campos finitos y sobre que campo finito se va a operar
# Se retorna el resultado de la operacion como cadena

# Suma
def suma(a, b, cf):
    if cf == 4:
        return suma4[a][b]
    elif cf == 8:
        return suma8[a][b]
    elif cf == 64:
        return suma_especial_64(cf64[a], cf64[b])
    
# Suma especial para el campo finito de 64 elementos
def suma_especial_64(a, b):
    # Se separan los elementos de a, separando por el signo "+"
    a_partes = a.split("+")
    # Se separan los elementos de b, separando por el signo "+"
    b_partes = b.split("+")
    elementos = []
    # Juntamos los elementos de a y b, solo tomando los elementos que no aparecen en ambos
    for i in a_partes:
        if i not in b_partes:
            elementos.append(i)
    for i in b_partes:
        if i not in a_partes:
            elementos.append(i)
    # Revisamos si no hay elementos, entonces la suma es 0
    if len(elementos) == 0:
        return "0"
    # Si hay un solo elemento, entonces la suma es ese elemento
    elif len(elementos) == 1:
        return elementos[0]
    # Si hay varios elementos, se unen con el signo "+"
    else:
        # Ordenamos los elementos para que esten en el orden correcto, usando la funcion para comparar dos elementos
        elementos = sorted(elementos, key=cmp_to_key(comparar))
        return "+".join(elementos)

# Comparacion para poder ordenar en 64 elementos
# Siguiendo este orden 0 < 1 < a < a^2 < a^3 < a^4 < a^5 < a^6
def comparar(a, b):
    if a == b:
        return 0
    elif a == "0":
        return 1
    elif b == "0":
        return -1
    elif a == "1":
        return 1
    elif b == "1":
        return -1
    elif a == "a":
        return 1
    elif b == "a":
        return -1
    elif a == "a^2":
        return 1
    elif b == "a^2":
        return -1
    elif a == "a^3":
        return 1
    elif b == "a^3":
        return -1
    elif a == "a^4":
        return 1
    elif b == "a^4":
        return -1
    elif a == "a^5":
        return 1
    elif b == "a^5":
        return -1
    elif a == "a^6":
        return 1
    elif b == "a^6":
        return -1
    
# Resta
def resta(a, b, cf):
    # Si tenemos a - b = x, entonces a = x + b
    if cf == 4:
        for i in range(4):
            if suma(i, b, cf) == cf4[a]:
                return cf4[i]
    elif cf == 8:
        for i in range(8):
            if suma(i, b, cf) == cf8[a]:
                return cf8[i]
    elif cf == 64:
        for i in range(64):
            if suma(i, b, cf) == cf64[a]:
                return cf64[i]

# Multiplicacion
def mult2(a, b, cf):
    if cf == 4:
        return mult4[a][b]
    elif cf == 8:
        return mult8[a][b]
    elif cf == 64:
        return mult64[a][b]
def mult(a, b, cf):
    # Usamos cfi_e para saber el exponente de a y b, sumamos los exponentes y buscamos el resultado en cfi_e
    if cf == 4:
        if a == 0 or b == 0:
            return 0
        else:
            e1 = cf4_e[a]
            e2 = cf4_e[b]
            # Quitamos las dos primeros caracteres para obtener el exponente, ya que son de la forma "a^n"
            e1 = int(e1[2:])
            e2 = int(e2[2:])
            e = (e1 + e2) % 3
            elemento = "a^" + str(e)
            indice = buscar_elemento(elemento, cf4_e)
            return cf4[indice]
    elif cf == 8:
        if a == 0 or b == 0:
            return 0
        else:
            e1 = cf8_e[a]
            e2 = cf8_e[b]
            e1 = int(e1[2:])
            e2 = int(e2[2:])
            e = (e1 + e2) % 7
            elemento = "a^" + str(e)
            indice = buscar_elemento(elemento, cf8_e)
            return cf8[indice]
    elif cf == 64:
        if a == 0 or b == 0:
            return 0
        else:
            e1 = cf64_e[a]
            e2 = cf64_e[b]
            e1 = int(e1[2:])
            e2 = int(e2[2:])
            e = (e1 + e2) % 63
            elemento = "a^" + str(e)
            indice = buscar_elemento(elemento, cf64_e)
            return cf64[indice]
        
# Buscar un elemento en la lista de elementos, regresando el indice
def buscar_elemento(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

# Division
def div(a, b, cf):
    if b == 0:
        return "No se puede dividir por 0"
    # Si tenemos a / b = x, entonces a = x * b
    if cf == 4:
        for i in range(4):
            if mult(i, b, cf) == cf4[a]:
                print(i)
                return cf4[i]
    elif cf == 8:
        for i in range(8):
            if mult(i, b, cf) == cf8[a]:
                return cf8[i]
    elif cf == 64:
        for i in range(64):
            if mult(i, b, cf) == cf64[a]:
                return cf64[i]

# Exponenciacion
def exp(a, b, cf):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        if cf == 4:
            e1 = cf4_e[a]
            e2 = cf4_e[b]
            e1 = int(e1[2:])
            e2 = int(e2[2:])
            e = (e1 * e2) % 3
            elemento = "a^" + str(e)
            indice = buscar_elemento(elemento, cf4_e)
            return cf4[indice]
        elif cf == 8:
            e1 = cf8_e[a]
            e2 = cf8_e[b]
            e1 = int(e1[2:])
            e2 = int(e2[2:])
            e = (e1 * e2) % 7
            elemento = "a^" + str(e)
            indice = buscar_elemento(elemento, cf8_e)
            return cf8[indice]
        elif cf == 64:
            e1 = cf64_e[a]
            e2 = cf64_e[b]
            e1 = int(e1[2:])
            e2 = int(e2[2:])
            e = (e1 * e2) % 63
            elemento = "a^" + str(e)
            indice = buscar_elemento(elemento, cf64_e)
            return cf64[indice]
        
# Funcion para pedir un elemento de un campo finito y regresar el indice
def pedir_elemento(cf):
    if cf == 4:
        print("Elementos del campo finito de 4 elementos:")
        for i in range(4):
            print(f"{i}: {cf4[i]}")
        elemento = int(input("Ingresa el indice del elemento: "))
        if elemento < 0 or elemento > 3:
            print("Elemento no valido")
            return -1
        return elemento
    elif cf == 8:
        print("Elementos del campo finito de 8 elementos:")
        for i in range(8):
            print(f"{i}: {cf8[i]}")
        elemento = int(input("Ingresa el indice del elemento: "))
        if elemento < 0 or elemento > 7:
            print("Elemento no valido")
            return -1
        return elemento
    elif cf == 64:
        print("Elementos del campo finito de 64 elementos:")
        for i in range(64):
            print(f"{i}: {cf64[i]}")
        elemento = int(input("Ingresa el indice del elemento: "))
        if elemento < 0 or elemento > 63:
            print("Elemento no valido")
            return -1
        return elemento
    
# Funcion para pedir un campo finito
def pedir_cf():
    print("Campos finitos:")
    print("1. 4 elementos")
    print("2. 8 elementos")
    print("3. 64 elementos")
    cf = int(input("Ingresa el campo finito: "))
    if cf == 1:
        return 4
    elif cf == 2:
        return 8
    elif cf == 3:
        return 64
    else :
        print("Campo finito no valido")
        return -1
    
# Funcion para pedir una operacion
def pedir_operacion():
    print("Operaciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Exponenciacion")
    operacion = int(input("Ingresa la operacion: "))
    if operacion < 1 or operacion > 5:
        print("Operacion no valida")
        return -1
    return operacion

# Funcion principal
# Primero pedir el campo finito, luego pedir los elementos y la operacion
def main():
    cf = pedir_cf()
    if cf == -1:
        return
    operacion = pedir_operacion()
    if operacion == -1:
        return
    a = pedir_elemento(cf)
    if a == -1:
        return
    b = pedir_elemento(cf)
    if b == -1:
        return
    respuesta = ""
    if operacion == 1:
        respuesta = suma(a, b, cf)
    elif operacion == 2:
        respuesta = resta(a, b, cf)
    elif operacion == 3:
        respuesta = mult(a, b, cf)
    elif operacion == 4:
        respuesta = div(a, b, cf)
    elif operacion == 5:
        respuesta = exp(a, b, cf)
    elemento_1 = ""
    elemento_2 = ""
    if cf == 4:
        elemento_1 = cf4[a]
        elemento_2 = cf4[b]
    elif cf == 8:
        elemento_1 = cf8[a]
        elemento_2 = cf8[b]
    elif cf == 64:
        elemento_1 = cf64[a]
        elemento_2 = cf64[b]
    operacion_str = ""
    if operacion == 1:
        operacion_str = " mas "
    elif operacion == 2:
        operacion_str = " menos "
    elif operacion == 3:
        operacion_str = " por "
    elif operacion == 4:
        operacion_str = " entre "
    elif operacion == 5:
        operacion_str = " elevado a "
    print(f"El resultado de {elemento_1}{operacion_str}{elemento_2} es {respuesta}")

if __name__ == "__main__":
    main()
