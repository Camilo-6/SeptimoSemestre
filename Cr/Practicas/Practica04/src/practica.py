def mcd(a,b):
    """
    Regresa el maximo comun divisor de dos numeros.
    """
    while b != 0:
        a = a % b
        # Swap
        aux = a
        a = b
        b = aux
    return a

def reduce(x,n):
    """
    Regresa un numero reducido a modulo n
    """
    negativo = x < 0
    numero_reducido = abs(x) % n
    return n - numero_reducido if negativo else numero_reducido

def inverso(x,n):
    """
    Regresa el inverso multiplicativo de un numero (si lo hay).        
    """
    # Un numero tiene inverso multiplicativo si x,n son primos relativos (coprimos)
    if mcd(x,n) == 1:
        a, s, t = euclides_extendido(x,n)
        return reduce(s,n)
    else:
        raise ValueError(f"El inverso multiplicativo de {x} mod {n} no existe")

def euclides_extendido(a, b):
    """
    Regresa el maximo comun divisor de 'a' y 'b' junto con los coeficientes de la combinación lineal. 
    """
    # Combinacion lineal
    # r = sa + tb
    s_0 = 1     # Coeficiente s
    s_1 = 0     # Carga con el divisor
    t_0 = 0     # Coeficiente t
    t_1 = 1     # Carga con el dividendo
    while b != 0:
        # Algoritmo de la division
        # a = bq + r
        q = int(a / b)  # Cociente
        r = a % b       # Residuo
        # Swap
        a = b
        b = r
        # Actualizamos los coeficientes s y t (Swap)
        s_0, s_1 = s_1, s_0 - q * s_1
        t_0, t_1 = t_1, t_0 - q * t_1
    # Imprimimos la combinacion lineal: r = as + bt
    # print(f"{q} = {x}({s_0}) + {y}({t_0})")
    # print(a,b,s_0,s_1,t_0,t_1)
    return a, s_0, t_0

# Metodo para resolver dos congruencias de la forma ax + y ≡ b (mod m) y cx + y ≡ d (mod m), obteniendo los valores de x y y
def resolver_congruencias(a, b, c, d, m):
    # Primero resolver para x
    # Restar la segunda congruencia de la primera para eliminar y
    # (ax + y - (cx + y)) ≡ (b - d) (mod m) => (a - c)x ≡ (b - d) (mod m)
    a_menos_c = a - c
    b_menos_d = b - d
    # Encontrar x en (a - c)x ≡ (b - d) (mod m)
    # Encontrar el inverso modular de (a - c) mod m
    inv = inverso(a_menos_c % m, m)
    # Resolver para x
    x = (inv * (b_menos_d % m)) % m
    # Resolver para y
    # Sustituir x en ax + y ≡ b (mod m) y encontrar y
    y = (b - a * x) % m
    return x, y

# Bytes Magicos
bpng = [137, 80, 78, 71, 13, 10, 26, 10]
bpdf = [37, 80, 68, 70]
bmp4 = [0, 0, 0, 32, 102, 116, 121, 112]
bmp3 = [73, 68, 51]
bytes_magicos = [bpng, bpdf, bmp4, bmp3]

# Metodo para abrir un archivo y obtener los primeros 8 bytes en decimal
def obtener_primeros_8_bytes(archivo):
    with open(archivo, "rb") as f:
        primeros_bytes = f.read(8)
        primeros_numeros = [int(byte) for byte in primeros_bytes]
    return primeros_numeros

# Metodo para aplicar una funcion a cada byte de un archivo (en forma de decimal) y guardar el resultado en un nuevo archivo (en forma de bytes)
def aplicar_funcion_a_bytes(archivo, funcion, archivo_salida):
    with open(archivo, "rb") as f:
        bytes = f.read()
        numeros = [int(byte) for byte in bytes]
    resultado = [funcion(byte) % 256 for byte in numeros]
    with open(archivo_salida, "wb") as f:
        f.write(bytearray(resultado))

# Error para devolver cuando no se pueda descifrar un archivo
class ErrorDescifrado(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Metodo para dado los primeros 8 bytes (en forma decimal) de un archivo, intentar descifrarlo (sabiendo que es un archivo PNG, PDF, MP4 o MP3)
# Devolver una funcion que lo descifre y que tipo de archivo es
def obtener_funcion_descifrado(primeros_bytes):
    for byte_magico in bytes_magicos:
        try:
            # Caso especial, si son los bytes magicos de un archivo mp4 tomar los bytes 5, 6 y 7
            if byte_magico == bmp4:
                a, b = resolver_congruencias(primeros_bytes[6], byte_magico[6], primeros_bytes[5], byte_magico[5], 256)
                if (a * primeros_bytes[4] + b) % 256 == byte_magico[4]:
                    return lambda z: (z * a + b) % 256, bytes_magicos.index(byte_magico)
            else:
                x, y = resolver_congruencias(primeros_bytes[0], byte_magico[0], primeros_bytes[1], byte_magico[1], 256)
                if (x * primeros_bytes[2] + y) % 256 == byte_magico[2]:
                    return lambda z: (z * x + y) % 256, bytes_magicos.index(byte_magico)
        except:
            pass
    return ErrorDescifrado("No se pudo descifrar el archivo")

# Metodo para intentar descifrar un archivo y guardar el resultado en un nuevo archivo
def magia(archivo):
    try:
        primeros_bytes = obtener_primeros_8_bytes(archivo)
        funcion_descifrado, tipo_archivo = obtener_funcion_descifrado(primeros_bytes)
        salida = archivo[:-4]
        if tipo_archivo == 0:
            salida += ".png"
        elif tipo_archivo == 1:
            salida += ".pdf"
        elif tipo_archivo == 2:
            salida += ".mp4"
        elif tipo_archivo == 3:
            salida += ".mp3"
        aplicar_funcion_a_bytes(archivo, funcion_descifrado, salida)
    except ErrorDescifrado as e:
        print(e)

#magia("archivos/file2.lol")
#magia("archivos/file3.lol")
#magia("archivos/file4.lol")

# Metodo fuerza bruta para encontrar funcion de descifrado
# Dados los primeros 8 bytes de un archivo, intentar todas las combinaciones posibles de a y b (de 0 a 255) para encontrar la funcion de descifrado
def fuerza_bruta(primeros_bytes, bytes_objetivo):
    for a in range(256):
        for b in range(256):
            try:
                copia = primeros_bytes.copy()
                copia = [(x * a + b) % 256 for x in copia]
                longitud = len(bytes_objetivo)
                if copia[:longitud] == bytes_objetivo:
                    return lambda z: (z * a + b) % 256
            except:
                pass
    return ErrorDescifrado("No se pudo descifrar el archivo")

# Metodo para convertir un caracter de base64 a su valor decimal
def base64_a_decimal(caracter):
    if 'A' <= caracter <= 'Z':
        return ord(caracter) - ord('A')
    if 'a' <= caracter <= 'z':
        return ord(caracter) - ord('a') + 26
    if '0' <= caracter <= '9':
        return ord(caracter) - ord('0') + 52
    if caracter == '+':
        return 62
    if caracter == '/':
        return 63
    raise ValueError("Caracter no valido")

# Metodo para convertir un numero decimal a su valor binario usando 6 bits
def decimal_a_binario(valor):
    return format(valor, '06b')

# Metodo para convertir un valor binario a su numero decimal
def binario_a_decimal(valor):
    return int(valor, 2)

# Metodo para convertir un numero decimal a su caracter ASCII como hexadecimal
def decimal_a_hexadecimal(valor):
    return format(valor, '02x')

# Metodo para el algoritmo de descifrado de base64
# Dado un texto cifrado en base64, devolver el texto descifrado como bytes
def decode64(texto):
    # Convertir el texto a una lista de valores decimales, ignorando los caracteres de padding
    valores = [base64_a_decimal(caracter) for caracter in texto if caracter != '=']
    # Convertir los valores decimales a binario
    binario = "".join([decimal_a_binario(valor) for valor in valores])
    # Ajustar la longitud del binario al multiplo de 8 bits (bytes)
    padding = (8 - len(binario) % 8) % 8
    binario = binario[:-padding] if padding else binario
    # Separar el binario en grupos de 8 bits
    grupos = [binario[i:i+8] for i in range(0, len(binario), 8)]
    # Convertir los grupos de 8 bits a su valor decimal
    decimales = [binario_a_decimal(grupo) for grupo in grupos]
    # Convertir los valores decimales a caracteres ASCII como hexadecimal
    hexadecimal = [decimal_a_hexadecimal(decimal) for decimal in decimales]
    # Convertir los caracteres ASCII a bytes
    return bytes.fromhex("".join(hexadecimal))

# Metodo para descifrar un archivo base64 y guardar el resultado
def magia_v2(archivo, archivo_salida):
    with open(archivo, "r") as f:
        texto = f.read()
    datos_descifrados = decode64(texto)
    with open(archivo_salida, "wb") as f:
        f.write(datos_descifrados)

#magia_v2("archivos/file1.lol", "archivos/file1.png")

# Metodo para convertir un valor decimal a su caracter de base64
def decimal_a_base64(valor):
    if 0 <= valor <= 25:
        return chr(valor + ord('A'))
    if 26 <= valor <= 51:
        return chr(valor - 26 + ord('a'))
    if 52 <= valor <= 61:
        return chr(valor - 52 + ord('0'))
    if valor == 62:
        return '+'
    if valor == 63:
        return '/'
    raise ValueError("Valor no valido")

# Metodo para convertir bytes a su valor binario de 8 bits
def byte_a_binario(byte):
    return format(byte, '08b')

# Metodo para convertir un binario a su valor decimal
def binario_a_byte(binario):
    return int(binario, 2)

# Metodo para el algoritmo de cifrado de base64
# Dado un texto en bytes, devolver el texto cifrado en base64
def encode64(bytes):
    # Convertir los bytes a valores binarios
    binarios = [byte_a_binario(byte) for byte in bytes]
    # Unir los valores binarios en un solo string
    binario = "".join(binarios)
    # Separar el binario en grupos de 6 bits
    grupos = [binario[i:i+6] for i in range(0, len(binario), 6)]
    # Si el ultimo grupo tiene menos de 6 bits, agregar ceros al final y calcular el padding
    if len(grupos[-1]) < 6:
        padding = 6 - len(grupos[-1])
        grupos[-1] += "0" * (6 - len(grupos[-1]))
    else:
        padding = 0
    # Convertir los grupos de 6 bits a su valor decimal
    decimales = [binario_a_byte(grupo) for grupo in grupos]
    # Convertir los valores decimales a caracteres de base64
    base64 = [decimal_a_base64(decimal) for decimal in decimales]
    # Calcular el padding en base a los bits faltantes
    padding = "=" * (padding // 2)
    # Regresar el resultado como texto base64 con el padding si es necesario
    return "".join(base64) + padding

# Metodo para cifrar un archivo y guardar el resultado
def magiant_v2(archivo, archivo_salida):
    with open(archivo, "rb") as f:
        datos = f.read()
    texto_cifrado = encode64(datos)
    with open(archivo_salida, "w") as f:
        f.write(texto_cifrado)

#magiant_v2("archivos/file1.png", "archivos/file1.xd")
#magia_v2("archivos/file1.xd", "archivos/file5.png")
#magiant_v2("archivos/file2.pdf", "archivos/file2.xd")
#magia_v2("archivos/file2.xd", "archivos/file6.pdf")
#magiant_v2("archivos/file3.mp3", "archivos/file3.xd")
#magia_v2("archivos/file3.xd", "archivos/file7.mp3")
#magiant_v2("archivos/file4.mp4", "archivos/file4.xd")
#magia_v2("archivos/file4.xd", "archivos/file8.mp4")

# Metodo para cifrar un archivo usando una funcion afin y guardar el resultado en un nuevo archivo
def magiant(archivo, a, b, archivo_salida):
    funcion_cifrado = lambda z: (a * z + b) % 256
    aplicar_funcion_a_bytes(archivo, funcion_cifrado, archivo_salida)

#magiant("archivos/file1.png", 3, 5, "archivos/file11.owo")
#magia("archivos/file11.owo")
#magiant("archivos/file2.pdf", 11, 17, "archivos/file12.owo")
#magia("archivos/file12.owo")
#magiant("archivos/file3.mp3", 13, 7, "archivos/file13.owo")
#magia("archivos/file13.owo")
#magiant("archivos/file4.mp4", 19, 4, "archivos/file14.owo")
#magia("archivos/file14.owo")