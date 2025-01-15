# Práctica 08 - Criptografía y Seguridad

## Autores:

+ Arrieta Mancera Luis Sebastián - 318174116
+ Cruz Cruz Alan Josue - 319327133
+ García Ponce José Camilo - 319210536
+ Matute Cantón Sara Lorena - 319331622


## Notas:

+ Hay conflictos con la bandera `-h` ya que `argparse` reserva la opcion `-h` para mostrar la ayuda del programa. Por ello se utiliza la bandera `-hi` para ocultar un mensaje en una imagen.

**Argumentos**

+ `-i` ruta de la imagen
+ `-hi` Ocultar imagen:
  + Mensaje a ocultar
  + Ruta de salida de la imagen
+ `-r` Revelar mensaje

# Ejecución:

Instala las librerias **colorarma**, **pillow** y para la tarea moral **skimage**. 

**Colorama**

```bash
pip install colorama
```

**Pillow**

```bash
pip install pillow
```

**Skimage**

```bash
pip install scikit-image
```

Para probar el programa ejecuta los siguientes comandos con python o python3. Los comandos tienen la siguiente estructura:

Para ocultar un mensaje en una imagen:

```bash
python3 practica08.py -i <Ruta de la imagen> -hi "<Mensaje a ocultar>" <Ruta de salida de la imagen>.png
```

Para revelar el mensaje de una imagen:

```bash
python3 practica08.py -i <Ruta de la imagen> -r
```

## Ejemplo:

Insetar "Hola mundo" en una imagen de perrito:

```bash
python3 practica08.py -i ./imagenes/perrito.jpg -hi "Hola mundo" ./imagenes/perrito_con_mensaje.png
```

Para revelar el mensaje de perrito:

```bash
python3 practica08.py -i ./imagenes/perrito_con_mensaje.png -r
```

# Chessboard

Ejecuta el siguiente comando para mostrar el mensaje oculto de la imagen `Chessboard.png`

```bash
python3 practica08.py -i ./imagenes/chessboard.png -r
```