import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../Ejercicio5'))
from raices import raiz_cuadrada_p, raiz_3, raiz_cuadrada_n, raiz_cuadrada_n_gen

# Usar las implementaciones para calcular las raices de a modulo n

# Ejercicio 1
# a = 55, n = 103 (primo)
# Usaremos el metodo de raiz_cuadrada_p
#print(raiz_cuadrada_p(55, 103)) # 63, 40
# Verificamos que 63^2 es congruente con 55 modulo 103
#print(pow(63, 2, 103)) # 55
# Verificamos que 40^2 es congruente con 55 modulo 103
#print(pow(40, 2, 103)) # 55
# Entonces 55 tiene las raices 63 y 40 en modulo 103
# Tambien notamos que 103 es congruente con 3 modulo 4, por lo que podemos usar el metodo de raiz_3
#print(raiz_3(55, 103)) # 63, 40
# Regresando los mismos resultados


# Ejercicio 2
# a = 76, n = 102
# Usaremos el metodo de raiz_cuadrada_n_gen, ya que 102 se factoriza en 2 * 3 * 17
#print(raiz_cuadrada_n_gen(76, 102)) # 56, 80, 46, 22
# Verificamos que 56^2 es congruente con 76 modulo 102
#print(pow(56, 2, 102)) # 76
# Verificamos que 80^2 es congruente con 76 modulo 102
#print(pow(80, 2, 102)) # 76
# Verificamos que 46^2 es congruente con 76 modulo 102
#print(pow(46, 2, 102)) # 76
# Verificamos que 22^2 es congruente con 76 modulo 102
#print(pow(22, 2, 102)) # 76
# Entonces 76 tiene las raices 22, 46, 56 y 80 en modulo 102


# Ejercicio 3
# a = 161, n = 211 (primo)
# Usaremos el metodo de raiz_cuadrada_p
#print(raiz_cuadrada_p(161, 211)) # 43, 168
# Verificamos que 43^2 es congruente con 161 modulo 211
#print(pow(43, 2, 211)) # 161
# Verificamos que 168^2 es congruente con 161 modulo 211
#print(pow(168, 2, 211)) # 161
# Entonces 161 tiene las raices 43 y 168 en modulo 211


# Ejercicio 4
# a = 133,  = 177
# Usaremos el metodo de raiz_cuadrada_n
#print(raiz_cuadrada_n(133, 177)) # 88, 89, 148, 29
# Verificamos que 88^2 es congruente con 133 modulo 177
#print(pow(88, 2, 177)) # 133
# Verificamos que 89^2 es congruente con 133 modulo 177
#print(pow(89, 2, 177)) # 133
# Verificamos que 148^2 es congruente con 133 modulo 177
#print(pow(148, 2, 177)) # 133
# Verificamos que 29^2 es congruente con 133 modulo 177
#print(pow(29, 2, 177)) # 133
# Entonces 133 tiene las raices 29, 88, 89 y 148 en modulo 177

