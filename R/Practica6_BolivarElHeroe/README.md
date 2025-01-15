# Practica 6 - Redes de computadoras

Equipo:

- Bonilla Reyes Dafne - 319089660
- García Ponce José Camilo - 319210536
- González Peñaloza Arturo - 319091193
- Main Cerezo Asahel Said - 319260658
- Raudry Rico Emilio Arsenio - 318289276

# Explicación

Decidimos construir el juego de **serpientes y escaleras**. Los archivos consisten en:
- Cliente.java y Servidor.java para modelar respectivamente dichos objetos.
- Player.java objeto que modela al jugador y guarda su posición en el tablero
- Board.java objeto que modela el tablero y se encarga de manejar las casillas especiales, imprimir el
tablero, entre otras.
 
## Modo de ejecución

Compilamos todos los archivos Java:

```bash
javac *.java
```

Ejecutamos primero Servidor.java

```bash
java Servidor
```
Ejecutamos ahora Cliente.java

```bash
java Cliente
```

## Modo de juego

En cada turno se mostrará en la terminal el tablero con el estado actual del juego. 

Presiona enter para lanzar los dados y avanzar en el tablero. 

Las casillas Ei y Si representan escaleras y serpientes respectivamente. 

Llega a la casilla de la esquina superior izquierda para ganar! :D

