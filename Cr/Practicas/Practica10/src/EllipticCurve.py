from Point import Point
from tools import *

class EllipticCurve:
    '''Clase que crea una curva elíptica usando un campo finito modulo p > 3'''

    # Punto al infinito siempre será None. Ignorar esta prueba unitaria
    inf_p = None

    def __init__(self, prime = 3, a = 1, b = 1):
        '''Construimos la curva elíptica a partir de los parámetros a, b modulo p'''
        self.prime = prime
        self.a = a
        self.b = b
        self.points = self.get_points()

    def __str__(self):
        '''La curva debe ser representada como: y^2 = x^3 + ax + b mod p'''
        return f'y^2 = x^3 + {self.a}x + {self.b} mod {self.prime}'

    def isInCurve(self, point):
        '''Nos dice si un punto "point" pertenece a esta curva'''
        # Verificamos si el punto es el punto al infinito
        if point == None:
            return True
        # Verificamos si es un punto
        if not isinstance(point, Point):
            return False
        x = point.x
        y = point.y
        # Verificamos si y^2 = x^3 + ax + b mod p
        return (y**2)%self.prime == (x**3 + self.a*x + self.b)%self.prime

    def get_points(self):
        '''Nos da todos los puntos que pertenecen a la curva elíptica'''
        puntos = [None]
        for x in range(self.prime):
            for y in range(self.prime):
                if self.isInCurve(Point(x, y)):
                    puntos.append(Point(x, y))
        return puntos

    def sum(self, p, q):
        '''Suma p + q  regresando un nuevo punto modulo prime
        como está definido en las curvas elípticas. Recuerda que el punto al
        infinito funciona como neutro aditivo'''
        # Si p o q son el punto al infinito regresamos el otro punto
        if p == None:
            return q
        if q == None:
            return p
        lamb = 0
        if p == q:
            # Si p == q, lambda es (3x_p^2 + a) / 2y_p mod prime
            parte1 = 3*p.x**2 + self.a
            parte2 = inv_mult(2*p.y, self.prime)
            if parte2 == None:
                return None
            lamb = parte1*parte2
        else:
            # Si p != q, lambda es (y_q - y_p) / (x_q - x_p) mod prime
            parte1 = q.y - p.y
            parte2 = inv_mult(q.x - p.x, self.prime)
            if parte2 == None:
                return None
            lamb = parte1*parte2
        # x_r = lambda^2 - x_p - x_q mod prime
        x = (lamb**2 - p.x - q.x)%self.prime
        # y_r = lambda(x_p - x_r) - y_p mod prime
        y = (lamb*(p.x - x) - p.y)%self.prime
        return Point(x, y)

    def mult(self, k, p):
        '''Suma  k veces el punto p (o k(P)).
        Si k < 0 entonces se suma el inverso de P k veces'''
        if p == None:
            return None
        # Si k < 0, entonces sumamos el inverso de p k veces
        if k < 0:
            p = self.inv(p)
            k = -k
        # Si k = 0, regresamos el punto al infinito
        if k == 0:
            return None
        # Si k = 1, regresamos el punto p
        if k == 1:
            return p
        # Si k > 1, sumamos k veces el punto p
        q = p
        for i in range(k-1):
            q = self.sum(q, p)
            if q == None:
                return None
        return q

    def order(self, p):
        '''Dado el punto p que pertenece a la curva elíptica, nos regresa el mínimo entero k 
        tal que  k(P) = punto al infinito.'''
        k = 1
        actual = p
        # Mientras k(P) != punto al infinito, sumamos el punto actual con p
        while actual != None:
            actual = self.sum(actual, p)
            k += 1
        return k

    def cofactor(self, p):
        '''Dado el punto p de la curva, regresa el total de puntos de la curva entre el orden
        de ese punto'''
        return len(self.points)//self.order(p)

    def inv(self, p):
        '''Regresa el inverso aditivo de este punto. Recuerda que es el mismo punto reflejado
        en el eje x'''
        if p == None:
            return None
        return Point(p.x, -p.y%self.prime)
