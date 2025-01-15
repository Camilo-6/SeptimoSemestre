from des import *
from colorama import Fore, Back, Style

# Colores
# pip install colorama
verde = Fore.GREEN
azul = Fore.BLUE
magenta = Fore.MAGENTA
reset = Fore.RESET

# Síndrome - Mario Benedetti
mensaje= """
Todavia tengo casi todos mis dientes

casi todos mis cabellos y poquísimas canas

puedo hacer y deshacer el amor

trepar una escalera de dos en dos

y correr cuarenta metros detrás del ómnibus

o sea que no debería sentirme viejo

pero el grave problema es que antes

no me fijaba en estos detalles.
"""
llave = hex_a_bin("e0e0fefef1f1fefe")
mensaje_cifrado = cifrar(mensaje, llave)
print(magenta+'\nMensaje cifrado: '+reset, '\n')
print(verde+f'{mensaje_cifrado}'+reset,'\n\n')
mensaje_descifrado = descifrar(mensaje_cifrado, llave)
print(magenta+'Mensaje descifrado:'+reset)
print(azul+f'{mensaje_descifrado}'+reset)

# Prueba de las llaves
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
    mensaje_cifrado = cifrar(mensaje, k)
    mensaje_descifrado = descifrar(mensaje_descifrado, k)

# Prueba llaves semidebiles
for k in llaves_semidebiles:
    mensaje_cifrado = cifrar(mensaje, k)
    mensaje_descifrado = descifrar(mensaje_descifrado, k)

# Prueba llaves posiblemente debiles
for k in llaves_posiblemente_debiles:
    mensaje_cifrado = cifrar(mensaje, k)
    mensaje_descifrado = descifrar(mensaje_descifrado, k)
