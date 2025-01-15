import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../Ejercicio5'))
from poli import mcd_poli, div_poli

# Encontrar el maximo comun divisor de los polinomios
# f(x) = x^6 + x^5 + x^4 + 1
# g(x) = x^5 + x^3 + x^2 + 1
# en Z_2[x]

# Usaremos los metodos de div_poli y mcd_poli, que se encuentran en poli.py

# Primero transformamos los polinomios a su representacion en listas para poder usar las funciones
f = [1, 1, 1, 0, 0, 0, 1]
g = [1, 0, 1, 1, 0, 1]
# Usamos mcd_poli para encontrar el maximo comun divisor
#print(mcd_poli(f, g, 2)) # [1, 1]
# Transformamos el resultado a su representacion en polinomios
# x + 1
# Entonces el maximo comun divisor de f y g en Z_2[x] es x + 1
# Ahora para verificar vamos a dividir f entre g
# Usamos div_poli para encontrar el cociente y el residuo
#print(div_poli(f, g, 2)) # ([1, 1], [1, 1, 0])
# Entonces el cociente es x + 1 y el residuo es x^2 + x
# Ahora dividimos g entre x^2 + x
#print(div_poli(g, [1, 1, 0], 2)) # ([1, 1, 0, 1], [1, 1])
# Entonces el cociente es x^3 + x^2 + 1 y el residuo es x + 1
# Ahora dividimos x^2 + x entre x + 1
#print(div_poli([1, 1, 0], [1, 1], 2)) # ([1, 0], [0])
# Entonces el cociente es x y el residuo es 0
# Por lo que el maximo comun divisor de f y g es x + 1
