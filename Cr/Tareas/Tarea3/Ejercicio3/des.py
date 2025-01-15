def permutacion_inicial(bits):

    # Permutacion inicial
    tabla_IP = [
        [58, 50, 42, 34, 26, 18, 10, 2],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]
    ]

    # Asegúrate de que la cadena de bits tenga 64 bits
    if len(bits) != 64:
        raise ValueError("La cadena de bits debe tener 64 bits.")
    
    # Aplicamos la permutación inicial usando la tabla_IP
    permutacion = [bits[pos - 1] for fila in tabla_IP for pos in fila]
    return ''.join(permutacion)

def expandir_bloque(bloque_32bits):

    # Expancion
    tabla_E_bit_selection = [
        [32, 1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8, 9],
        [8, 9, 10, 11, 12, 13],
        [12, 13, 14, 15, 16, 17],
        [16, 17, 18, 19, 20, 21],
        [20, 21, 22, 23, 24, 25],
        [24, 25, 26, 27, 28, 29],
        [28, 29, 30, 31, 32, 1]
    ]

    # Aseguramos que el bloque de entrada tenga 32 bits
    if len(bloque_32bits) != 32:
        raise ValueError("El bloque debe ser de 32 bits.")
    
    # Creamos el nuevo bloque de 48 bits aplicando la tabla
    bloque_48bits = [bloque_32bits[pos - 1] for fila in tabla_E_bit_selection for pos in fila]
    
    # Convertimos la lista de bits en una cadena
    return ''.join(bloque_48bits)

def aplicar_xor_48bits(bloque_48bits, llave_48bits):
    # Aseguramos que tanto el bloque como la llave tengan 48 bits
    if len(bloque_48bits) != 48 or len(llave_48bits) != 48:
        raise ValueError("Tanto el bloque como la llave deben ser de 48 bits.")
    
    # Realizamos el XOR bit a bit entre el bloque y la llave
    resultado_xor = ''.join(
        str(int(bloque_48bits[i]) ^ int(llave_48bits[i])) for i in range(48)
    )
    
    return resultado_xor

def aplicar_cajas_s(bloque_48bits):

    # Cajas S
    tabla_S1 = [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ]
    tabla_S2 = [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ]
    tabla_S3 = [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ]
    tabla_S4 = [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ]
    tabla_S5 = [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ]
    tabla_S6 = [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ]
    tabla_S7 = [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ]
    tabla_S8 = [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]


    # Tablas S1 a S8
    tablas_s = [tabla_S1, tabla_S2, tabla_S3, tabla_S4, tabla_S5, tabla_S6, tabla_S7, tabla_S8]

    # Asegúrate de que el bloque tenga 48 bits
    if len(bloque_48bits) != 48:
        raise ValueError("El bloque debe tener 48 bits.")

    # Función auxiliar para convertir un número decimal a una cadena binaria de longitud n
    def decimal_a_binario(n, longitud):
        return bin(n)[2:].zfill(longitud)

    # Dividimos el bloque de 48 bits en 8 subbloques de 6 bits
    subbloques = [bloque_48bits[i:i+6] for i in range(0, 48, 6)]
    
    resultado = ""

    # Procesamos cada subbloque y aplicamos la caja S correspondiente
    for i, subbloque in enumerate(subbloques):
        # Seleccionamos la tabla S correspondiente
        tabla_s = tablas_s[i]

        # Obtenemos el primer y último bit, los convertimos a decimal
        fila = int(subbloque[0] + subbloque[5], 2)

        # Obtenemos los 4 bits del medio, los convertimos a decimal
        columna = int(subbloque[1:5], 2)

        # Buscamos el valor en la tabla S correspondiente
        valor_s = tabla_s[fila][columna]

        # Convertimos el valor obtenido en binario de 4 bits y lo concatenamos al resultado
        resultado += decimal_a_binario(valor_s, 4)

    # Regresamos el bloque de 32 bits resultante
    return resultado

def permutar_bloque_32bits(bloque_32bits):

    tabla_P = [
        [16, 7, 20, 21],
        [29, 12, 28, 17],
        [1, 15, 23, 26],
        [5, 18, 31, 10],
        [2, 8, 24, 14],
        [32, 27, 3, 9],
        [19, 13, 30, 6],
        [22, 11, 4, 25]
    ]

    # Aseguramos que el bloque de entrada tenga 32 bits
    if len(bloque_32bits) != 32:
        raise ValueError("El bloque debe ser de 32 bits.")
    
    # Aplicamos la permutación utilizando la tabla P
    permutacion = [bloque_32bits[pos - 1] for fila in tabla_P for pos in fila]
    
    # Devolvemos el bloque permutado como una cadena de 32 bits
    return ''.join(permutacion)

def aplicar_xor_32bits(bloque1, bloque2):
    # Aseguramos que ambos bloques tengan 32 bits
    if len(bloque1) != 32 or len(bloque2) != 32:
        raise ValueError("Ambos bloques deben ser de 32 bits.")
    
    # Realizamos la operación XOR bit a bit entre los dos bloques
    resultado_xor = ''.join(
        str(int(bloque1[i]) ^ int(bloque2[i])) for i in range(32)
    )
    
    return resultado_xor

def funcion_f(bloque_32bits, llave_48bits):
    # Aplicamos la expansion
    expansion = expandir_bloque(bloque_32bits)
    B = aplicar_xor_48bits(expansion, llave_48bits)
    C = aplicar_cajas_s(B)
    permutacion = permutar_bloque_32bits(C)
    return permutacion

def permutacion_inversa(bits):

    # Permutacion inicial inversa
    tabla_IP_inversa = [
        [40, 8, 48, 16, 56, 24, 64, 32],
        [39, 7, 47, 15, 55, 23, 63, 31],
        [38, 6, 46, 14, 54, 22, 62, 30],
        [37, 5, 45, 13, 53, 21, 61, 29],
        [36, 4, 44, 12, 52, 20, 60, 28],
        [35, 3, 43, 11, 51, 19, 59, 27],
        [34, 2, 42, 10, 50, 18, 58, 26],
        [33, 1, 41, 9, 49, 17, 57, 25]
    ]

    # Aseguramos que la cadena de bits tenga 64 bits
    if len(bits) != 64:
        raise ValueError("La cadena de bits debe tener 64 bits.")
    
    # Aplicamos la permutación inversa usando la tabla_IP_inversa
    permutacion = [bits[pos - 1] for fila in tabla_IP_inversa for pos in fila]
    
    return ''.join(permutacion)

def ignorar_bits_paridad(bloque_64):
    # Verificamos que el bloque tenga exactamente 64 bits
    if len(bloque_64) != 64 or not all(b in '01' for b in bloque_64):
        raise ValueError("El bloque debe ser una cadena de 64 bits de '0' y '1'.")

    bloques_procesados = []
    
    # Dividimos en 8 bloques de 8 bits
    for i in range(0, 64, 8):
        bloque_8 = bloque_64[i:i+8]
        
        # Eliminamos el bit de paridad (último bit)
        bloque_7 = bloque_8[:7]
        
        # Contamos la cantidad de 1's en el bloque de 7 bits
        cantidad_1s = bloque_7.count('1')
        
        # Agregamos 0 si la cantidad de 1's es impar, 1 si es par
        if cantidad_1s % 2 == 0:
            bloque_7 += '1'  # Par, agregamos 1
        else:
            bloque_7 += '0'  # Impar, agregamos 0
        
        # Agregamos el bloque procesado a la lista
        bloques_procesados.append(bloque_7)
    
    return ''.join(bloques_procesados)

def aplicar_PC_1(bloque_64bits):

    tabla_PC_1 = [
        [57, 49, 41, 33, 25, 17, 9],
        [1, 58, 50, 42, 34, 26, 18],
        [10, 2, 59, 51, 43, 35, 27],
        [19, 11, 3, 60, 52, 44, 36],
        [63, 55, 47, 39, 31, 23, 15],
        [7, 62, 54, 46, 38, 30, 22],
        [14, 6, 61, 53, 45, 37, 29],
        [21, 13, 5, 28, 20, 12, 4]
    ]

    # Asegúrate de que la cadena de bits tenga 64 bits
    if len(bloque_64bits) != 64:
        raise ValueError("La cadena de bits debe tener 64 bits.")
    
    # Aplicamos la permutación inicial usando la tabla_PC_1
    permutacion = [bloque_64bits[pos - 1] for fila in tabla_PC_1 for pos in fila]
    return ''.join(permutacion)

def llave_inicial(llave_64bits):
    return aplicar_PC_1(ignorar_bits_paridad(llave_64bits))

def desplazar_bits_izquierda(cadena_56bits, numero_desplazamientos):
    # Verificamos que la cadena sea de 56 bits
    if len(cadena_56bits) != 56 or not all(b in '01' for b in cadena_56bits):
        raise ValueError("La cadena debe ser una cadena de 56 bits de '0' y '1'.")

    # Si el valor es 1, 2, 9 o 16, se desplaza solo 1 posición a la izquierda
    if numero_desplazamientos in [1, 2, 9, 16]:
        desplazamiento = 1
    else:
        desplazamiento = 2
    
    # Desplazamiento circular a la izquierda
    cadena_desplazada = cadena_56bits[desplazamiento:] + cadena_56bits[:desplazamiento]
    
    return cadena_desplazada

def aplicar_PC_2(cadena_56bits):

    tabla_PC_2 = [
        [14, 17, 11, 24, 1, 5],
        [3, 28, 15, 6, 21, 10],
        [23, 19, 12, 4, 26, 8],
        [16, 7, 27, 20, 13, 2],
        [41, 52, 31, 37, 47, 55],
        [30, 40, 51, 45, 33, 48],
        [44, 49, 39, 56, 34, 53],
        [46, 42, 50, 36, 29, 32]
    ]

    # Verificamos que la cadena sea de 56 bits
    if len(cadena_56bits) != 56 or not all(b in '01' for b in cadena_56bits):
        raise ValueError("La cadena debe ser una cadena de 56 bits de '0' y '1'.")
    
    # Aplicamos la permutación de la tabla PC-2
    permutacion = [cadena_56bits[pos - 1] for fila in tabla_PC_2 for pos in fila]
    
    # Retornamos la cadena permutada de 48 bits
    return ''.join(permutacion)

def hex_a_bin(hexadecimal):
    # Convertir cada carácter hexadecimal a su representación binaria de 4 bits
    return bin(int(hexadecimal, 16))[2:].zfill(len(hexadecimal) * 4)

def cifrar_bloque(bloque_64bits, llave_64bits):
    # Aplicamos la permutacion
    bloque_permutacion_inicial = permutacion_inicial(bloque_64bits)

    # Dividimos el bloque
    mitad = len(bloque_permutacion_inicial) // 2
    l = bloque_permutacion_inicial[:mitad]
    r = bloque_permutacion_inicial[mitad:]

    # Obtenemos los bloques iniciales c_0d_0 de la llave
    c_id_i = llave_inicial(llave_64bits)

    for i in range(16):
        c_id_i = desplazar_bits_izquierda(c_id_i, i+1)
        k_i = aplicar_PC_2(c_id_i)
        l, r = r, aplicar_xor_32bits(l, funcion_f(r, k_i))

    y = permutacion_inversa(r+l)

    return y

def descifrar_bloque(bloque_64bits, llave_64bits):
    # Aplicamos la permutacion
    bloque_permutacion_inicial = permutacion_inicial(bloque_64bits)

    # Dividimos el bloque
    mitad = len(bloque_permutacion_inicial) // 2
    l = bloque_permutacion_inicial[:mitad]
    r = bloque_permutacion_inicial[mitad:]

    # Obtenemos los bloques iniciales c_0d_0 de la llave
    c_id_i = llave_inicial(llave_64bits)
    
    # Obtenemos las llaves
    subllaves = []
    for i in range(16):
        c_id_i = desplazar_bits_izquierda(c_id_i, i+1)
        k_i = aplicar_PC_2(c_id_i)
        subllaves.append(k_i)

    # Proceso inverso
    for k_i in reversed(subllaves):
        l, r = r, aplicar_xor_32bits(l, funcion_f(r, k_i))

    # Aplicamos la permutación inversa y regresamos el bloque descifrado
    y = permutacion_inversa(r + l)

    return y

def mensaje_a_bits(mensaje):
    bits = ''
    for letra in mensaje:
        bits += format(ord(letra),'08b')
    return bits

def bits_a_mensaje(bits):
    step = 8
    mensaje = ''
    for i in range(0,len(bits),step):
        bloque = bits[i:i+step]
        mensaje += chr(int(bloque,2))
    return mensaje

def dividir_en_bloques(cadena, k, x):
    """
        Divide una cadena en bloques

        Parameters :
        ------------

            cadena:
                cadena a dividir
            k:
                longitud de los bloques
            x: 
                relleno de los bloques cuando no sean de longitud k
        
        Returns :
        ---------

            lista con el mensaje dividido
    """
    bloques = []
    for i in range(0, len(cadena), k):
        if (len(cadena) - i < k):
            bloques.append(cadena[i:] + x * (k - (len(cadena) - i)))
        else:
            bloques.append(cadena[i:i+k])
    return bloques

def cifrar(mensaje, llave):
    # Dividimos el mensaje en bloques de 8 letras (64 bits) 
    bloques = dividir_en_bloques(mensaje, 8, '\x0e') # \x0e es un caracter no imprimible
    # Convertirmos los bloques a bits
    bits = ''.join([ mensaje_a_bits(bloque) for bloque in bloques])
    # Ciframos el mensaje
    mensaje_cifrado = ''
    for bloque in dividir_en_bloques(bits, 64, ''):
        mensaje_cifrado += cifrar_bloque(bloque, llave)
    return bits_a_mensaje(mensaje_cifrado)

def descifrar(mensaje, llave):
    if (len(mensaje) * 8) % 64 != 0:
        raise ValueError('La longitud del mensaje en bits no es multiplo de 64')
    # Convertimos el mensaje a bits
    bits = mensaje_a_bits(mensaje)
    # Desciframos el mensaje
    mensaje_descifrado = ''
    for bloque in dividir_en_bloques(bits, 64, ''):
        mensaje_descifrado += descifrar_bloque(bloque, llave)
    return bits_a_mensaje(mensaje_descifrado)
    
if __name__ == '__main__':
    bits = "1100101010111010101110101010101010101010101010111010101010101010"  # cadena de 64 bits

    # Llaves que no deben usarse en DES
    # Mayo 2023

    # Llaves débiles DES
    llaves_debiles = [
        hex_a_bin("0101010101010101"),
        hex_a_bin("fefefefefefefefe"),
        hex_a_bin("1f1f1f1f1f1f1f1f"),
        hex_a_bin("e0e0e0e0e0e0e0e0")
    ]

    # Llaves semidébiles DES
    llaves_semidebiles = [
        hex_a_bin("01fe01fe01fe01fe"), hex_a_bin("fe01fe01fe01fe01"),
        hex_a_bin("1fe01fe01fe01fe0"), hex_a_bin("e01fe01fe01fe01f"),
        hex_a_bin("01e001e001e001e0"), hex_a_bin("e001e001e001e001"),
        hex_a_bin("1ffe1ffe1ffe1ffe"), hex_a_bin("fe1ffe1ffe1ffe1f"),
        hex_a_bin("011f011f011f011f"), hex_a_bin("1f011f011f011f01"),
        hex_a_bin("e0fee0fee0fee0fe"), hex_a_bin("fee0fee0fee0fee0")    
    ]

    #Posiblemente débiles
    llaves_posiblemente_debiles = [
        hex_a_bin("1f1f01010e0e0101"), hex_a_bin("e00101e0f10101f1"),
        hex_a_bin("011f1f01010e0e01"), hex_a_bin("fe1f01e0fe0e01f1"),
        hex_a_bin("1f01011f0e01010e"), hex_a_bin("fe011fe0fe010ef1"),
        hex_a_bin("01011f1f01010e0e"), hex_a_bin("e01f1fe0f10e0ef1"),
                                        hex_a_bin("fe0101fefe0101fe"),
        hex_a_bin("e0e00101f1f10101"), hex_a_bin("e01f01fef10e01fe"),
        hex_a_bin("fefe0101fefe0101"), hex_a_bin("e0011ffef1010efe"),
        hex_a_bin("fee01f01fef10e01"), hex_a_bin("fe1f1ffefe0e0efe"),
        hex_a_bin("e0fe1f01f1fe0e01"), 
        hex_a_bin("fee0011ffef1010e"), hex_a_bin("1ffe01e00efe01f1"),
        hex_a_bin("e0fe011ff1fe010e"), hex_a_bin("01fe1fe001fe0ef1"),
        hex_a_bin("e0e01f1ff1f10e0e"), hex_a_bin("1fe001fe0ef101fe"),
        hex_a_bin("fefe1f1ffefe0e0e"), hex_a_bin("01e01ffe01f10efe"),

        hex_a_bin("fe1fe001fe0ef101"), hex_a_bin("0101e0e00101f1f1"),
        hex_a_bin("e01ffe01f10efe01"), hex_a_bin("1f1fe0e00e0ef1f1"),
        hex_a_bin("fe01e01ffe01f10e"), hex_a_bin("1f01fee00e0ef1f1"),
        hex_a_bin("e001fe1ff101fe0e"), hex_a_bin("011ffee0010efef1"),
                                        hex_a_bin("1f01e0fe0e01f1fe"),
        hex_a_bin("01e0e00101e1e101"), hex_a_bin("011fe0fe010ef1fe"),
        hex_a_bin("1ffee0010efef001"), hex_a_bin("0101fefe0101fefe"),
        hex_a_bin("1ffee0010ef1fe01"), hex_a_bin("1f1ffefe0e0efefe"),
        hex_a_bin("01fefe0101fefe01"),
        hex_a_bin("1fe0e0f10ef1f10e"), hex_a_bin("fefee0e0fefef1f1"),
        hex_a_bin("01fee01f01fef10e"), hex_a_bin("e0fefee0f1fefef1"),
        hex_a_bin("01e0fe1f01f1fe0e"), hex_a_bin("fee0e0fefef1f1fe"),
        hex_a_bin("1ffefe1f0efefe0e"), hex_a_bin("e0e0fefef1f1fefe"),
    ]

    # Prueba llaves debiles
    for k in llaves_debiles:
        print(cifrar_bloque(bits,k))

    # Prueba llaves semidebiles
    for k in llaves_semidebiles:
        print(cifrar_bloque(bits,k))

    # Prueba llaves posiblemente debiles
    for k in llaves_posiblemente_debiles:
        print(cifrar_bloque(bits,k))


