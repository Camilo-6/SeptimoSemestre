# Codigo para implementar VLSM (Variable Length Subnet Mask)
# Entrada: IP, Mascara de red, cantidad de subredes con nombres y Hosts por subred
# Salida: Tabla con la informacion de cada subred, incluyendo el Id de red, Mascara de red, Rango de direcciones utiles y Broadcast

# Metodos para obtener las entradas

from prettytable import PrettyTable

# Metodo para obtener la IP
def obtener_ip():
    print("Ingrese la direccion IP")
    print("Con el formato: n1.n2.n3.n4")
    print("Ejemplo: 192.168.1.0")
    ip = input("Ingrese la direccion: ")
    ip_partes = ip.split(".")
    ip_partes = [int(i) for i in ip_partes]
    return ip_partes

# Metodo para obtener la mascara de red
def obtener_mascara():
    print("Ingrese la mascara de red")
    print("Con el formato: n1.n2.n3.n4")
    print("Ejemplo: 255.255.255.0")
    mascara = input("Ingrese la mascara: ")
    mascara_partes = mascara.split(".")
    mascara_partes = [int(i) for i in mascara_partes]
    return mascara_partes

# Metodo para obtener la cantidad de subredes
def obtener_cantidad_subredes():
    print("Ingrese la cantidad de subredes con nombres y hosts por subred")
    print("Con el formato: nombre1,hosts1,nombre2,hosts2,...")
    print("Ejemplo: A,10,B,20,C,30")
    cantidad = input("Ingrese los datos de las subredes: ")
    cantidad = cantidad.split(",")
    subred_cant = []
    for i in range(0, len(cantidad), 2):
        subred_cant.append((cantidad[i], int(cantidad[i + 1])))
    return subred_cant

# Metodos para realizar los calculos

# Metodo para ordenar las subredes por cantidad de hosts
def ordenar_subredes(subredes):
    return sorted(subredes, key=lambda x: x[1], reverse=True)

# Metodo para obtener la cantidad de bits a usar
def bits_necesarios(hosts):
    n = 1
    listo = False
    while not listo:
        if 2 ** n > hosts:
            listo = True
        else:
            n += 1
    return n

# Metodo para calcular la cantidad de hosts utiles
def hosts_utiles(n):
    return 2 ** n - 2

# Metodo para calcular la mascara
def calcular_mascara(n):
    return 32 - n

# Metodo para obtener el numero magico
def numero_magico(mascara_red, mascara):
    numero_unos = sum([bin(i).count("1") for i in mascara_red])
    numero_unos_faltantes = mascara - numero_unos
    if numero_unos_faltantes < 0:
        return ValueError("Algo salio mal :(")
    numero_ceros = 8 - numero_unos_faltantes
    numerito = ""
    for i in range(numero_unos_faltantes):
        numerito += "1"
    for i in range(numero_ceros):
        numerito += "0"
    numerito_decimal = int(numerito, 2)
    return 256 - numerito_decimal

# Metodo para aumentar el ultimo octeto de la mascara
def aumentar_octeto(mascara_partes, numero):
    mascara_partes[3] += numero
    if mascara_partes[3] > 255:
        mascara_partes[2] += 1
        mascara_partes[3] -= 256
    if mascara_partes[2] > 255:
        mascara_partes[1] += 1
        mascara_partes[2] -= 256
    if mascara_partes[1] > 255:
        mascara_partes[0] += 1
        mascara_partes[1] -= 256
    if mascara_partes[0] > 255:
        print("Algo salio mal con la mascara :(")
        return ValueError("Algo salio mal con la mascara :(")
    return mascara_partes

# Metodo para aumentar el ultimo octeto de la IP
def aumentar_octeto_ip(ip_partes, numero):
    ip_partes[3] += numero
    if ip_partes[3] > 255:
        ip_partes[2] += 1
        ip_partes[3] -= 256
    if ip_partes[2] > 255:
        ip_partes[1] += 1
        ip_partes[2] -= 256
    if ip_partes[1] > 255:
        ip_partes[0] += 1
        ip_partes[1] -= 256
    if ip_partes[0] > 255:
        print("Algo salio mal con la IP :(")
        return ValueError("Algo salio mal con la IP :(")
    return ip_partes

# Metodos para obtener la tabla de subredes
def hacer_tablita(ip_partes, mascara_partes, subred_cant):
    subredes_ordenadas = ordenar_subredes(subred_cant)
    # Crear tabla usando PrettyTable
    tabla = PrettyTable()
    tabla.field_names = ["Nombre de Subred", "ID de Red", "Mascara de Red", 
                         "Primera Direccion", "Ultima Direccion", "Broadcast"]
    mascara_partes_original = mascara_partes.copy()
    for subred in subredes_ordenadas:
        nombre = subred[0]
        hosts = subred[1]
        n = bits_necesarios(hosts)
        hosts_utiles_subred = hosts_utiles(n)
        mascara = calcular_mascara(n)
        numero_magico_subred = numero_magico(mascara_partes_original, mascara)
        id_red = f"{ip_partes[0]}.{ip_partes[1]}.{ip_partes[2]}.{ip_partes[3]}"
        aumentar_octeto(mascara_partes, numero_magico_subred)
        mascara_red = f"{mascara_partes[0]}.{mascara_partes[1]}.{mascara_partes[2]}.{mascara_partes[3]}"
        aumentar_octeto_ip(ip_partes, 1)
        primera_direccion = f"{ip_partes[0]}.{ip_partes[1]}.{ip_partes[2]}.{ip_partes[3]}"
        aumentar_octeto_ip(ip_partes, hosts_utiles_subred - 1)
        ultima_direccion = f"{ip_partes[0]}.{ip_partes[1]}.{ip_partes[2]}.{ip_partes[3]}"
        aumentar_octeto_ip(ip_partes, 1)
        direccion_broadcast = f"{ip_partes[0]}.{ip_partes[1]}.{ip_partes[2]}.{ip_partes[3]}"
        aumentar_octeto_ip(ip_partes, 1)
        # Agregar fila a la tabla
        tabla.add_row([nombre, id_red, mascara_red, 
                       primera_direccion, ultima_direccion, direccion_broadcast])
    return tabla

    
# Cosas para que funcione
ip = obtener_ip()
print()
mascara = obtener_mascara()
print()
subredes = obtener_cantidad_subredes()
tablita = hacer_tablita(ip, mascara, subredes)
print("\nTabla de Subredes")
print(tablita)

""""
Ejemplos

- Ejemplo 1:
Clase de red (A) (direcciones de 0.0.0.0 a 127.255.255.255)
IP: 1.0.0.0
Mascara: 255.255.255.0
Subredes: A,40,B,20,C,10,D,5
+------------------+-----------+-----------------+-------------------+------------------+-----------+
| Nombre de Subred | ID de Red |  Mascara de Red | Primera Direccion | Ultima Direccion | Broadcast |
+------------------+-----------+-----------------+-------------------+------------------+-----------+
|        A         |  1.0.0.0  |  255.255.255.64 |      1.0.0.1      |     1.0.0.62     |  1.0.0.63 |
|        B         |  1.0.0.64 |  255.255.255.96 |      1.0.0.65     |     1.0.0.94     |  1.0.0.95 |
|        C         |  1.0.0.96 | 255.255.255.112 |      1.0.0.97     |    1.0.0.110     | 1.0.0.111 |
|        D         | 1.0.0.112 | 255.255.255.120 |     1.0.0.113     |    1.0.0.118     | 1.0.0.119 |
+------------------+-----------+-----------------+-------------------+------------------+-----------+

- Ejemplo 2:
Clase de red (D) (direcciones de 224.0.0.0 a 239.255.255.255)
IP: 224.132.1.0
Mascara: 255.255.255.0
Subredes: A,24,B,30,C,60,D,20
+------------------+---------------+-----------------+-------------------+------------------+---------------+
| Nombre de Subred |   ID de Red   |  Mascara de Red | Primera Direccion | Ultima Direccion |   Broadcast   |
+------------------+---------------+-----------------+-------------------+------------------+---------------+
|        C         |  224.132.1.0  |  255.255.255.64 |    224.132.1.1    |   224.132.1.62   |  224.132.1.63 |
|        B         |  224.132.1.64 |  255.255.255.96 |    224.132.1.65   |   224.132.1.94   |  224.132.1.95 |
|        A         |  224.132.1.96 | 255.255.255.128 |    224.132.1.97   |  224.132.1.126   | 224.132.1.127 |
|        D         | 224.132.1.128 | 255.255.255.160 |   224.132.1.129   |  224.132.1.158   | 224.132.1.159 |
+------------------+---------------+-----------------+-------------------+------------------+---------------+

- Ejemplo 3:
Clase de red (C) (direcciones de 192.0.0.0 a 223.255.255.255)
IP: 196.160.1.0
Mascara: 255.255.255.0
Subredes: A,30,B,30,C,30,D,30
+------------------+--------------+-----------------+-------------------+------------------+---------------+
| Nombre de Subred |  ID de Red   |  Mascara de Red | Primera Direccion | Ultima Direccion |   Broadcast   |
+------------------+--------------+-----------------+-------------------+------------------+---------------+
|        A         | 196.160.1.0  |  255.255.255.32 |    196.160.1.1    |   196.160.1.30   |  196.160.1.31 |
|        B         | 196.160.1.32 |  255.255.255.64 |    196.160.1.33   |   196.160.1.62   |  196.160.1.63 |
|        C         | 196.160.1.64 |  255.255.255.96 |    196.160.1.65   |   196.160.1.94   |  196.160.1.95 |
|        D         | 196.160.1.96 | 255.255.255.128 |    196.160.1.97   |  196.160.1.126   | 196.160.1.127 |
+------------------+--------------+-----------------+-------------------+------------------+---------------+
"""