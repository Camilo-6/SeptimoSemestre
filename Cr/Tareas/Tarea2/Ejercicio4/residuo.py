import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../Ejercicio3'))
from simbolos import jacobi

# Determinar si un numero a es residuo cuadratico modulo n

# Definicion de residuo cuadratico
# Sea n en Z^+, un entero positivo, decimos que un entero modular a en Z_n (sin el 0) es un residuo cuadratico modulo n
# si y solo si existe x en Z_n tal que x^2 es congruente con a modulo n

# Ejercicio 1
# a = 6007, n = 1902
# Primero usamos el simbolo de Jacobi de 6007/1902, ya que 1902 no es primo
#print(jacobi(6007, 1902))
# Pero 6007 es mayor que 1902, por lo que calculamos el residuo de 6007 mod 1902
#print(6007 % 1902) # 301
# Ahora calculamos el simbolo de Jacobi de 301/1902
#print(jacobi(301, 1902)) # -1
# Como el simbolo de Jacobi es -1, entonces creeriamos que 6007 no es un residuo cuadratico modulo 1902
# Pero notamos que 301 es un residuo cuadratico modulo 1902, ya que 139^2 es congruente con 301 modulo 1902
# 139 lo encontramos de la siguiente manera
#for i in range(0, 1901):
#    if pow(i, 2, 1902) == 301:
#        print(i)
# Por lo tanto tenemos que 139 esta en Z_1902 y 139^2 es congruente con 301 modulo 1902 y como 301 es congruente con 6007 modulo 1902
#print(pow(139, 2, 1902)) # 301
# Entonces 6007 es un residuo cuadratico modulo 1902
    

# Ejercicio 2
# a = 83, n = 593
# Primero usamos el simbolo de Legendre de 83/593, ya que 593 es primo https://byjus.com/maths/prime-numbers-from-1-to-1000/
#print(jacobi(83, 593)) # 1
# Como el simbolo de Legendre es 1, entonces sabemos que 83 esta en Q_593, Q_593 es el conjunto de los residuos cuadraticos modulo 593
# Entonces 83 es un residuo cuadratico modulo 593, pero nos falta encontrar el x tal que x^2 es congruente con 83 modulo 593
# Lo encontramos de la siguiente manera
#for i in range(0, 592):
#    if pow(i, 2, 593) == 83:
#        print(i)
# Por lo tanto tenemos que 26 esta en Z_593 y 26^2 es congruente con 83 modulo 593
#print(pow(26, 2, 593)) # 83
# Entonces 83 es un residuo cuadratico modulo 593


# Ejercicio 3
# a = 3677176, n = 4568731
# Primero usamos el simbolo de Jacobi de 3677176/4568731, ya que 4568731 es primo https://www.bigprimes.net/archive/prime/320401 https://www.bigprimes.net/cruncher/4568731
#print(jacobi(3677176, 4568731)) # 1
# Como el simbolo de Jacobi es 1, entonces sabemos que 3677176 esta en Q_4568731, Q_4568731 es el conjunto de los residuos cuadraticos modulo 4568731
# Entonces 3677176 es un residuo cuadratico modulo 4568731, pero nos falta encontrar el x tal que x^2 es congruente con 3677176 modulo 4568731
# Lo encontramos de la siguiente manera
#for i in range(0, 4568730):
#    if pow(i, 2, 4568731) == 3677176:
#        print(i)
# Por lo tanto tenemos que 23783 esta en Z_4568731 y 23783^2 es congruente con 3677176 modulo 4568731
#print(pow(23783, 2, 4568731)) # 3677176
# Entonces 3677176 es un residuo cuadratico modulo 4568731


# Ejercicio 4
# a = 4568723, n = 4568731
# Primero usamos el simbolo de Jacobi de 4568723/4568731, ya que 4568731 es primo https://www.bigprimes.net/archive/prime/320401 https://www.bigprimes.net/cruncher/4568731
#print(jacobi(4568723, 4568731)) # 1
# Como el simbolo de Jacobi es 1, entonces sabemos que 4568723 esta en Q_4568731, Q_4568731 es el conjunto de los residuos cuadraticos modulo 4568731
# Entonces 4568723 es un residuo cuadratico modulo 4568731, pero nos falta encontrar el x tal que x^2 es congruente con 4568723 modulo 4568731
# Lo encontramos de la siguiente manera
#for i in range(0, 4568730):
#    if pow(i, 2, 4568731) == 4568723:
#        print(i)
# Por lo tanto tenemos que 2237208 esta en Z_4568731 y 2237208^2 es congruente con 4568723 modulo 4568731
#print(pow(2237208, 2, 4568731)) # 4568723
# Entonces 4568723 es un residuo cuadratico modulo 4568731
