from skimage.io import imread, imsave
import math

# Equipo Pinguicoders
# Arrieta Mancera Luis Sebastian - 318174116
# Cruz Cruz Alan Josue - 319327133
# Garcia Ponce Jose Camilo - 319210536
# Matute Canton Sara Lorena - 319331622

# Funcion para extraer el mensaje de una imagen
# Para este proceso usaremos los ultimos n bits de cada canal de cada pixel
# Primero se obtiene la longitud del mensaje, esta se encuentra en los primeros 16 bits
# Despues se extrae el mensaje en binario
# Revisar que los ultimos 8 bits sean 0, si no es asi, se arroja un error
# Finalmente se convierte el mensaje a texto y se imprime
def descifrar_imagen(imagen, n):
    if n < 1 or n > 8:
        raise ValueError("n debe ser un numero entre 1 y 8")
    # Obtenemos la imagen
    img = imread(imagen)
    altura, ancho, canal = 0, 0, 0
    altura_max, ancho_max = img.shape[0], img.shape[1]
    # Obtenemos la longitud del mensaje
    longitud_binario = ""
    lecturas = math.ceil(16/n)
    for i in range(lecturas):
        if i == math.ceil(16/n)-1:
            if 16 % n == 0:
                a = n
            else:
                a = 16 % n
            bits = obtener_ultimos_n_bits(img[altura, ancho, canal], a)
            longitud_binario = longitud_binario + str(bits)
            altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
        else:
            bits = obtener_ultimos_n_bits(img[altura, ancho, canal], n)
            longitud_binario = longitud_binario + str(bits)
            altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
    longitud = int(longitud_binario, 2)
    longitud = longitud*8
    # Obtenemos el mensaje
    mensaje_binario = ""
    lecturas = math.ceil(longitud/n)
    for i in range(lecturas):
        if i == math.ceil(longitud/n)-1:
            if longitud % n == 0:
                a = n
            else:
                a = longitud % n
            bits = obtener_ultimos_n_bits(img[altura, ancho, canal], a)
            mensaje_binario = mensaje_binario + str(bits)
            altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
        else:
            bits = obtener_ultimos_n_bits(img[altura, ancho, canal], n)
            mensaje_binario = mensaje_binario + str(bits)
            altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
    mensaje = ""
    # Convertimos el mensaje binario a texto
    for i in range(0, len(mensaje_binario), 8):
        byte = mensaje_binario[i:i+8]
        char = chr(int(byte, 2))
        mensaje += char
    # Verificamos que los siguientes 8 bits sean 00000000
    mensaje_final = ""
    lecturas = math.ceil(8/n)
    for i in range(lecturas):
        if i == math.ceil(8/n)-1:
            if 8 % n == 0:
                a = n
            else:
                a = 8 % n
            bits = obtener_ultimos_n_bits(img[altura, ancho, canal], a)
            mensaje_final = mensaje_final + str(bits)
            altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
        else:
            bits = obtener_ultimos_n_bits(img[altura, ancho, canal], n)
            mensaje_final = mensaje_final + str(bits)
            altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
    if mensaje_final != "00000000":
        print(mensaje)
        raise ValueError("El mensaje no termina con 00000000")
    print(f"Mensaje oculto:\n{mensaje}")


# Funcion para ocultar un mensaje en una imagen
# Para este proceso usaremos los ultimos n bits de cada canal de cada pixel
# Primero se inserta la longitud del mensaje en los primeros 16 bits
# Despues se inserta el mensaje en binario
# Finalmente se inserta un byte 00000000
def cifrar_imagen(mensaje, imagen_origen, imagen_destino, n):
    if n < 1 or n > 8:
        raise ValueError("n debe ser un numero entre 1 y 8")
    # Obtenemos la imagen
    img = imread(imagen_origen)
    altura, ancho, canal = 0, 0, 0
    altura_max, ancho_max = img.shape[0], img.shape[1]
    # Obtenemos la longitud del mensaje
    longitud_mensaje = len(mensaje)
    longitud_mensaje_binario = bin(longitud_mensaje)[2:].zfill(16)
    # Partimos la longitud del mensaje en partes de n bits
    longitud_mensaje_binario_partes = [longitud_mensaje_binario[i:i+n] for i in range(0, len(longitud_mensaje_binario), n)]
    # Revisar si la imagen puede ser ocultada en la imagen
    longitud_total = len(longitud_mensaje_binario_partes) + math.ceil(longitud_mensaje*8/n) + math.ceil(8/n)
    if longitud_total > altura_max*ancho_max*3:
        raise ValueError("El mensaje es muy largo para la imagen")
    # Insertamos la longitud del mensaje
    for parte in longitud_mensaje_binario_partes:
        img[altura, ancho, canal] = reemplazar_ultimos_n_bits(img[altura, ancho, canal], int(parte, 2), len(parte))
        altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
    # Obtenemos el mensaje en binario
    mensaje_binario = ''.join(format(ord(char), '08b') for char in mensaje)
    # Partimos el mensaje en partes de n bits
    mensaje_binario_partes = [mensaje_binario[i:i+n] for i in range(0, len(mensaje_binario), n)]
    # Insertamos el mensaje
    for parte in mensaje_binario_partes:
        img[altura, ancho, canal] = reemplazar_ultimos_n_bits(img[altura, ancho, canal], int(parte, 2), len(parte))
        altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
    # Obtenemos el byte 00000000
    mensaje_final = "00000000"
    # Partimos el mensaje en partes de n bits
    mensaje_final_partes = [mensaje_final[i:i+n] for i in range(0, len(mensaje_final), n)]
    # Insertamos el mensaje
    for parte in mensaje_final_partes:
        img[altura, ancho, canal] = reemplazar_ultimos_n_bits(img[altura, ancho, canal], int(parte, 2), len(parte))
        altura, ancho, canal = siguiente(altura, ancho, canal, altura_max, ancho_max)
    # Guardamos la imagen
    imsave(imagen_destino, img)

# Metodo para pasar al siguiente canal o pixel
def siguiente(altura, ancho, canal, altura_max, ancho_max):
    if canal == 2:
        canal = 0
        if altura == altura_max-1:
            altura = 0
            if ancho == ancho_max-1:
                ancho = 0
            else:
                ancho += 1
        else:
            altura += 1
    else:
        canal += 1
    return altura, ancho, canal

# Metodo para reemplazar los ultimos n bits de un numero
def reemplazar_ultimos_n_bits(numero_actual, nuevos_bits, n):
    # Revisar que 'numero_actual' tenga solo 8 bits
    numero_actual &= 0b11111111
    # Solo considerar los ultimos 'n' bits de 'nuevos_bits'
    nuevos_bits &= (1 << n) - 1
    # Crear una mascara con los ultimos 'n' bits en 1
    mascara = (1 << n) - 1
    # Limpiar los ultimos 'n' bits de 'numero_actual'
    numero_limpio = numero_actual & ~mascara
    # Agregar los nuevos bits
    resultado = numero_limpio | nuevos_bits
    return resultado

# Metodo para obtener los ultimos n bits de un numero
def obtener_ultimos_n_bits(numero, n):
    # Crear una mascara con los ultimos 'n' bits en 1
    mascara = (1 << n) - 1
    # Regresar los ultimos 'n' bits
    return bin(numero & mascara)[2:].zfill(n)

"""
Formas de realizar pruebas:
cifrar_imagen("texto", "imagenes/imagen.png", "imagenes/imagen_mensaje_n.png", n)
descifrar_imagen("imagenes/imagen_mensaje_n.png", n)
Para las pruebas se uso la imagen "oh_mai_gotto.png"
Generando una imagen para cada n de 1 a 8
Ejemplo de descifrado:
descifrar_imagen("imagenes/oh_mai_gotto_mensaje_5.png", 5)
Apartir de 3 bits se puede notar que los colores de la imagen cambian
En 1 bit no se nota la diferencia
En 2 bits tal vez se note, pero es mas dificil de notar la diferencia
En 3 bits la diferencia se nota pero con dificultad
En 4 bits tambien se nota la diferencia pero cuesta algo de trabajo
En 5 a 8 bits la diferencia es notable
Notemos que estas observaciones fueron realizadas haciendo zoom a la imagen (todo el zoom que Visual Studio Code permite)
"""

descifrar_imagen("imagenes/oh_mai_gotto_mensaje_5.png", 5)
