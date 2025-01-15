# Cifrador DES

# Tablas
# Permutacion inicial
tabla_ip = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]
# Inversa permutacion inicial
tabla_ip_inv = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]
# Expansion
tabla_expansion = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
# Cajas S
cajas_s = [
    # S_1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S_2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S_3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S_4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S_5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S_6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S_7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S_8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
# Permutacion P
tabla_p = [
    16, 7, 20, 21, 
    29, 12, 28, 17,
    1, 15, 23, 26, 
    5, 18, 31, 10,
    2, 8, 24, 14, 
    32, 27, 3, 9,
    19, 13, 30, 6, 
    22, 11, 4, 25
]
# PC-1 permutacion
tabla_pc1 = [
    57, 49, 41, 33, 25, 17, 9, 
    1, 58, 50, 42, 34, 26, 18, 
    10, 2, 59, 51, 43, 35, 27, 
    19, 11, 3, 60, 52, 44, 36, 
    63, 55, 47, 39, 31, 23, 15, 
    7, 62, 54, 46, 38, 30, 22, 
    14, 6, 61, 53, 45, 37, 29, 
    21, 13, 5, 28, 20, 12, 4
]
# PC-2 permutacion
tabla_pc2 = [
    14, 17, 11, 24, 1, 5, 
    3, 28, 15, 6, 21, 10, 
    23, 19, 12, 4, 26, 8, 
    16, 7, 27, 20, 13, 2, 
    41, 52, 31, 37, 47, 55, 
    30, 40, 51, 45, 33, 48, 
    44, 49, 39, 56, 34, 53, 
    46, 42, 50, 36, 29, 32
]

# Metodos

# Metodo para aplicar recorrimiento a la izquierda
# Si i es 1, 2, 9 o 16, se recorre 1 bit
# En otro caso, se recorre 2 bits
def left_shift_i(bits, i):
    if i in [1, 2, 9, 16]:
        return bits[1:] + bits[:1]
    return bits[2:] + bits[:2]

# Metodo para generar las 16 subllaves, dada una llave de 64 bits
def calcular_subllaves(llave):
    if len(llave) != 64:
        raise ValueError("La llave debe tener 64 bits")
    subllaves = []
    # Aplicar PC-1
    k_0 = ""
    for i in tabla_pc1:
        k_0 += llave[i - 1]
    c_0 = k_0[:28]
    d_0 = k_0[28:]
    # Generar las otras 16 subllaves
    c_i_1 = c_0
    d_i_1 = d_0
    for i in range(1, 17):
        c_i = left_shift_i(c_i_1, i)
        d_i = left_shift_i(d_i_1, i)
        k_i = ""
        c_i_d_i = c_i + d_i
        for j in tabla_pc2:
            k_i += c_i_d_i[j - 1]
        subllaves.append(k_i)
        c_i_1 = c_i
        d_i_1 = d_i
    return subllaves

# Metodo para realizar la funcion f, dada una cadena de 32 bits y una subllave de 48 bits
def funcion_f(bits, subllave):
    if len(bits) != 32:
        raise ValueError("La cadena debe tener 32 bits")
    if len(subllave) != 48:
        raise ValueError("La subllave debe tener 48 bits")
    # Aplicar expansion
    expansion = ""
    for i in tabla_expansion:
        expansion += bits[i - 1]
    # Hacer XOR de la expansion con la subllave
    e_xor_j = ""
    for i in range(48):
        digito_i_expansion = int(expansion[i])
        digito_i_subllave = int(subllave[i])
        digito_i_e_xor_j = digito_i_expansion ^ digito_i_subllave
        e_xor_j += str(digito_i_e_xor_j)
    # Dividir en 8 grupos de 6 bits
    grupos = []
    for i in range(0, 48, 6):
        grupos.append(e_xor_j[i:i + 6])
    # Aplicar la Caja S_i al grupo i para formar C
    c = ""
    for i in range(8):
        b_i = grupos[i]
        fila = int(b_i[0] + b_i[5], 2)
        columna = int(b_i[1:5], 2)
        c_i = cajas_s[i][fila][columna]
        c += f"{c_i:04b}"
    # Aplicar permutacion P a C
    f_a_j = ""
    for i in tabla_p:
        f_a_j += c[i - 1]
    return f_a_j

# Metodo para obtener L_i y R_i, usando L_{i-1} y R_{i-1}
def obtener_X_i(L_i_1, R_i_1, subllave):
    # Aplicar la de la funcion f a R_{i-1} y la subllave
    f_r_k = funcion_f(R_i_1, subllave)
    # Hacer XOR de L_{i-1} con f(R_{i-1}, K_i)
    r_i = ""
    for i in range(32):
        digito_i_L_i_1 = int(L_i_1[i])
        digito_i_f_r_k = int(f_r_k[i])
        digito_i_r_i = digito_i_L_i_1 ^ digito_i_f_r_k
        r_i += str(digito_i_r_i)
    # Pasar R_{i-1} como L_i
    l_i = R_i_1
    return l_i, r_i

# Metodo para obtener L_0 y R_0, usando una cadena de 64 bits
def paso_1(cadena_bits):
    if len(cadena_bits) != 64:
        raise ValueError("La cadena debe tener 64 bits")
    x_0 = ""
    for i in tabla_ip:
        x_0 += cadena_bits[i - 1]
    l_0 = x_0[:32]
    r_0 = x_0[32:]
    return l_0, r_0

# Metodo para obtener L_16 y R_16, usando L_0, R_0 y las 16 subllaves
def paso_2(l_0, r_0, subllaves):
    if len(l_0) != 32 or len(r_0) != 32:
        raise ValueError("L_0 y R_0 deben tener 32 bits")
    if len(subllaves) != 16:
        raise ValueError("Debe haber 16 subllaves")
    l_i = l_0
    r_i = r_0
    for i in range(16):
        l_i, r_i = obtener_X_i(l_i, r_i, subllaves[i])
    return l_i, r_i

# Metodo para aplicar la inversa de la permutacion inicial a L_16 y R_16
def paso_3(l_16, r_16):
    if len(l_16) != 32 or len(r_16) != 32:
        raise ValueError("L_16 y R_16 deben tener 32 bits")
    x_16 = r_16 + l_16
    cadena_bits = ""
    for i in tabla_ip_inv:
        cadena_bits += x_16[i - 1]
    return cadena_bits

# Metodo para cifrar un mensaje de 64 bits, usando una llave de 64 bits
def cifrar(mensaje, llave):
    if len(mensaje) != 64:
        raise ValueError("El mensaje debe tener 64 bits")
    if len(llave) != 64:
        raise ValueError("La llave debe tener 64 bits")
    subllaves = calcular_subllaves(llave)
    l_0, r_0 = paso_1(mensaje)
    l_16, r_16 = paso_2(l_0, r_0, subllaves)
    y = paso_3(l_16, r_16)
    return y

"""
mensaje_1 = "0000000100100011010001010110011110001001101010111100110111101111"
llave_1 = "0001001100110100010101110111100110011011101111001101111111110001"
mensaje_cifrado_1 = cifrar(mensaje_1, llave_1)
print(mensaje_cifrado_1)
print("------")
mensaje_c_real = "1000010111101000000100110101010000001111000010101011010000000101"
print(mensaje_c_real)
print("------")
print(mensaje_cifrado_1 == mensaje_c_real)
mensaje_cifrado_2 = cifrar(mensaje_cifrado_1, llave_1)
print(mensaje_cifrado_2)
print("------")
"""

# Metodo para pasar una cadena en hexadecimal a una cadena en bits
def hex_a_bits(hex):
    return bin(int(hex, 16))[2:].zfill(len(hex) * 4)

# Metodo para probar llaves debiles, las llaves estan en hexadecimal
def probar_llave_debil(mensaje, llave):
    cadena = ""
    llave_binario = hex_a_bits(llave)
    subllaves = calcular_subllaves(llave_binario)
    mensaje_cifrado = cifrar(mensaje, llave_binario)
    cadena += "Llave en hexadecimal: " + llave + "\n"
    cadena += "Llave en binario: " + llave_binario + "\n"
    cadena += "Texto original: " + mensaje + "\n"
    cadena += "Texto cifrado: " + mensaje_cifrado + "\n"
    cadena += "Subllaves:\n"
    for i in range(16):
        cadena += f"K_{i + 1}:\t{subllaves[i]}\n"
    return cadena

# Mensaje para probar llaves 0000000100100011010001010110011110001001101010111100110111101111
mensaje_prueba = "0000000100100011010001010110011110001001101010111100110111101111"

# Llave debil 1 0101010101010101
llave_debil_1 = "0101010101010101"
# Llave debil 2 fefefefefefefefe
llave_debil_2 = "fefefefefefefefe"
# Llave debil 3 1f1f1f1f1f1f1f1f
llave_debil_3 = "1f1f1f1f1f1f1f1f"
# Llave debil 4 e0e0e0e0e0e0e0e0
llave_debil_4 = "e0e0e0e0e0e0e0e0"

# Probar llaves debiles
"""
cadena = ""
for llave in [llave_debil_1, llave_debil_2, llave_debil_3, llave_debil_4]:
    cadena += probar_llave_debil(mensaje_prueba, llave)
    cadena += "------\n"
with open("llaves_debiles.txt", "w") as archivo:
    archivo.write(cadena)
"""

# Llave semidebil 1 01fe01fe01fe01fe
llave_semidebil_1 = "01fe01fe01fe01fe"
# Llave semidebil 2 1fe01fe01fe01fe0
llave_semidebil_2 = "1fe01fe01fe01fe0"
# Llave semidebil 3 01e001e001e001e0
llave_semidebil_3 = "01e001e001e001e0"
# Llave semidebil 4 1ffe1ffe1ffe1ffe
llave_semidebil_4 = "1ffe1ffe1ffe1ffe"
# Llave semidebil 5 011f011f011f011f
llave_semidebil_5 = "011f011f011f011f"
# Llave semidebil 6 e0fee0fee0fee0fe
llave_semidebil_6 = "e0fee0fee0fee0fe"
# Llave semidebil 7 fe01fe01fe01fe01
llave_semidebil_7 = "fe01fe01fe01fe01"
# Llave semidebil 8 e01fe01fe01fe01f
llave_semidebil_8 = "e01fe01fe01fe01f"
# Llave semidebil 9 e001e001e001e001
llave_semidebil_9 = "e001e001e001e001"
# Llave semidebil 10 fe1ffe1ffe1ffe1f
llave_semidebil_10 = "fe1ffe1ffe1ffe1f"
# Llave semidebil 11 1f011f011f011f01
llave_semidebil_11 = "1f011f011f011f01"
# Llave semidebil 12 fee0fee0fee0fee0
llave_semidebil_12 = "fee0fee0fee0fee0"

# Probar llaves semidebiles
"""
cadena = ""
for llave in [llave_semidebil_1, llave_semidebil_2, llave_semidebil_3, llave_semidebil_4, llave_semidebil_5, llave_semidebil_6, llave_semidebil_7, llave_semidebil_8, llave_semidebil_9, llave_semidebil_10, llave_semidebil_11, llave_semidebil_12]:
    cadena += probar_llave_debil(mensaje_prueba, llave)
    cadena += "------\n"
with open("llaves_semidebiles.txt", "w") as archivo:
    archivo.write(cadena)
"""

# Llave posiblemente debil 1 1f1f01010e0e0101
llave_posible_debil_1 = "1f1f01010e0e0101"
# Llave posiblemente debil 2 011f1f01010e0e01
llave_posible_debil_2 = "011f1f01010e0e01"
# Llave posiblemente debil 3 1f01011f0e01010e
llave_posible_debil_3 = "1f01011f0e01010e"
# Llave posiblemente debil 4 01011f1f01010e0e
llave_posible_debil_4 = "01011f1f01010e0e"
# Llave posiblemente debil 5 e0e00101f1f10101
llave_posible_debil_5 = "e0e00101f1f10101"
# Llave posiblemente debil 6 fefe0101fefe0101
llave_posible_debil_6 = "fefe0101fefe0101"
# Llave posiblemente debil 7 fee01f01fef10e01
llave_posible_debil_7 = "fee01f01fef10e01"
# Llave posiblemente debil 8 e0fe1f01f1fe0e01
llave_posible_debil_8 = "e0fe1f01f1fe0e01"
# Llave posiblemente debil 9 fee0011ffef1010e
llave_posible_debil_9 = "fee0011ffef1010e"
# Llave posiblemente debil 10 e0fe011ff1fe010e
llave_posible_debil_10 = "e0fe011ff1fe010e"
# Llave posiblemente debil 11 e0e01f1ff1f10e0e
llave_posible_debil_11 = "e0e01f1ff1f10e0e"
# Llave posiblemente debil 12 fefe1f1ffefe0e0e
llave_posible_debil_12 = "fefe1f1ffefe0e0e"

# Probar llaves posiblemente debiles parte 1
"""
cadena = ""
for llave in [llave_posible_debil_1, llave_posible_debil_2, llave_posible_debil_3, llave_posible_debil_4, llave_posible_debil_5, llave_posible_debil_6]:
    cadena += probar_llave_debil(mensaje_prueba, llave)
    cadena += "------\n"
with open("llaves_posiblemente_debiles_1.txt", "w") as archivo:
    archivo.write(cadena)
"""

# Llave posiblemente debil 13 fe1fe001fe0ef101
llave_posible_debil_13 = "fe1fe001fe0ef101"
# Llave posiblemente debil 14 e01ffe01f10efe01
llave_posible_debil_14 = "e01ffe01f10efe01"
# Llave posiblemente debil 15 fe01e01ffe01f10e
llave_posible_debil_15 = "fe01e01ffe01f10e"
# Llave posiblemente debil 16 e001fe1ff101fe0e
llave_posible_debil_16 = "e001fe1ff101fe0e"
# Llave posiblemente debil 17 01e0e00101e1e101
llave_posible_debil_17 = "01e0e00101e1e101"
# Llave posiblemente debil 18 1ffee0010efef001
llave_posible_debil_18 = "1ffee0010efef001"
# Llave posiblemente debil 19 1ffee0010ef1fe01
llave_posible_debil_19 = "1ffee0010ef1fe01"
# Llave posiblemente debil 20 01fefe0101fefe01
llave_posible_debil_20 = "01fefe0101fefe01"
# Llave posiblemente debil 21 1fe0e0f10ef1f10e
llave_posible_debil_21 = "1fe0e0f10ef1f10e"
# Llave posiblemente debil 22 01fee01f01fef10e
llave_posible_debil_22 = "01fee01f01fef10e"
# Llave posiblemente debil 23 01e0fe1f01f1fe0e
llave_posible_debil_23 = "01e0fe1f01f1fe0e"
# Llave posiblemente debil 24 1ffefe1f0efefe0e
llave_posible_debil_24 = "1ffefe1f0efefe0e"

# Probar llaves posiblemente debiles parte 2
"""
cadena = ""
for llave in [llave_posible_debil_13, llave_posible_debil_14, llave_posible_debil_15, llave_posible_debil_16, llave_posible_debil_17, llave_posible_debil_18, llave_posible_debil_19, llave_posible_debil_20, llave_posible_debil_21, llave_posible_debil_22, llave_posible_debil_23, llave_posible_debil_24]:
    cadena += probar_llave_debil(mensaje_prueba, llave)
    cadena += "------\n"
with open("llaves_posiblemente_debiles_2.txt", "w") as archivo:
    archivo.write(cadena)
"""

# Llave posiblemente debil 25 e00101e0f10101f1
llave_posible_debil_25 = "e00101e0f10101f1"
# Llave posiblemente debil 26 fe1f01e0fe0e01f1
llave_posible_debil_26 = "fe1f01e0fe0e01f1"
# Llave posiblemente debil 27 fe011fe0fe010ef1
llave_posible_debil_27 = "fe011fe0fe010ef1"
# Llave posiblemente debil 28 e01f1fe0f10e0ef1
llave_posible_debil_28 = "e01f1fe0f10e0ef1"
# Llave posiblemente debil 29 fe0101fefe0101fe
llave_posible_debil_29 = "fe0101fefe0101fe"
# Llave posiblemente debil 30 e01f01fef10e01fe
llave_posible_debil_30 = "e01f01fef10e01fe"
# Llave posiblemente debil 31 e0011ffef1010efe
llave_posible_debil_31 = "e0011ffef1010efe"
# Llave posiblemente debil 32 fe1f1ffefe0e0efe
llave_posible_debil_32 = "fe1f1ffefe0e0efe"
# Llave posiblemente debil 33 1ffe01e00efe01f1
llave_posible_debil_33 = "1ffe01e00efe01f1"
# Llave posiblemente debil 34 01fe1fe001fe0ef1
llave_posible_debil_34 = "01fe1fe001fe0ef1"
# Llave posiblemente debil 35 1fe001fe0ef101fe
llave_posible_debil_35 = "1fe001fe0ef101fe"
# Llave posiblemente debil 36 01e01ffe01f10efe
llave_posible_debil_36 = "01e01ffe01f10efe"

# Probar llaves posiblemente debiles parte 3
"""
cadena = ""
for llave in [llave_posible_debil_25, llave_posible_debil_26, llave_posible_debil_27, llave_posible_debil_28, llave_posible_debil_29, llave_posible_debil_30, llave_posible_debil_31, llave_posible_debil_32, llave_posible_debil_33, llave_posible_debil_34, llave_posible_debil_35, llave_posible_debil_36]:
    cadena += probar_llave_debil(mensaje_prueba, llave)
    cadena += "------\n"
with open("llaves_posiblemente_debiles_3.txt", "w") as archivo:
    archivo.write(cadena)
"""

# Llave posiblemente debil 37 0101e0e00101f1f1
llave_posible_debil_37 = "0101e0e00101f1f1"
# Llave posiblemente debil 38 1f1fe0e00e0ef1f1
llave_posible_debil_38 = "1f1fe0e00e0ef1f1"
# Llave posiblemente debil 39 1f01fee00e0ef1f1
llave_posible_debil_39 = "1f01fee00e0ef1f1"
# Llave posiblemente debil 40 011ffee0010efef1
llave_posible_debil_40 = "011ffee0010efef1"
# Llave posiblemente debil 41 1f01e0fe0e01f1fe
llave_posible_debil_41 = "1f01e0fe0e01f1fe"
# Llave posiblemente debil 42 011fe0fe010ef1fe
llave_posible_debil_42 = "011fe0fe010ef1fe"
# Llave posiblemente debil 43 0101fefe0101fefe
llave_posible_debil_43 = "0101fefe0101fefe"
# Llave posiblemente debil 44 1f1ffefe0e0efefe
llave_posible_debil_44 = "1f1ffefe0e0efefe"
# Llave posiblemente debil 45 fefee0e0fefef1f1
llave_posible_debil_45 = "fefee0e0fefef1f1"
# Llave posiblemente debil 46 e0fefee0f1fefef1
llave_posible_debil_46 = "e0fefee0f1fefef1"
# Llave posiblemente debil 47 fee0e0fefef1f1fe
llave_posible_debil_47 = "fee0e0fefef1f1fe"
# Llave posiblemente debil 48 e0e0fefef1f1fefe
llave_posible_debil_48 = "e0e0fefef1f1fefe"

# Probar llaves posiblemente debiles parte 4
"""
cadena = ""
for llave in [llave_posible_debil_37, llave_posible_debil_38, llave_posible_debil_39, llave_posible_debil_40, llave_posible_debil_41, llave_posible_debil_42, llave_posible_debil_43, llave_posible_debil_44, llave_posible_debil_45, llave_posible_debil_46, llave_posible_debil_47, llave_posible_debil_48]:
    cadena += probar_llave_debil(mensaje_prueba, llave)
    cadena += "------\n"
with open("llaves_posiblemente_debiles_4.txt", "w") as archivo:
    archivo.write(cadena)
"""

# Probar dos veces con la misma llave
"""
print(mensaje_prueba)
cadena = cifrar(mensaje_prueba, hex_a_bits(llave_debil_1))
print(cadena)
cadena2 = cifrar(cadena, hex_a_bits(llave_debil_1))
print(cadena2)
"""

# Probar dos veces con un par de llaves
"""
print(mensaje_prueba)
cadena = cifrar(mensaje_prueba, hex_a_bits(llave_semidebil_1))
print(cadena)
cadena2 = cifrar(cadena, hex_a_bits(llave_semidebil_7))
print(cadena2)
"""