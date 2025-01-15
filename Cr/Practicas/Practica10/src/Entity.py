import random as r

class Entity:
    '''Clase que modela una entidad como Alice o Bob.'''

    def __init__(self, name, curve, generator_point, table):
        '''Construye un nuevo personaje con un mensaje para compartir
        Una entidad tiene:
        1. name: Nombre de la entidad
        2. curve: Una curva elíptica a compartir
        3. generator_point: Un punto generador a compartir
        4. table: Una codificacion de caracteres a puntos de la curva.

        Además, debe inicializar sus llaves, públicas y privadas:
        5. private_key: Un entero aleatorio entre 1 y el orden del punto generador-1
        6. private_point: Un punto aleatorio de la curva que no sea el punto al infinito o el inverso del punto generador
        ## 3 llaves públicas de esta entidad
        7. public_key_1, public_key_2, public_key_3 = None
        ## 3 llaves públicas de la otra entidad
        8. another_entity_public_key_1, another_entity_public_key_2, another_entity_public_key_3 = None'''
        self.name = name
        self.curve = curve
        self.generator_point = generator_point
        self.order = curve.order(generator_point)
        ## Cosas privadas
        self.private_key = r.randint(1, self.order-1)
        self.private_point = self.obtener_punto_aleatorio(curve, generator_point)
        # Cosas publicas
        self.public_key_1 = None #Public key using private point
        self.public_key_2 = None #Public key using only private key
        self.public_key_3 = None

        #Public keys from another entity
        self.another_entity_public_key_1 = None
        self.another_entity_public_key_2 = None
        self.another_entity_public_key_3 = None

        self.table = table

    def __str__(self):
        '''Representacion en cadena de la entidad'''
        return f'{self.name}:\nEC: {self.curve}\nG: {self.generator_point}\nPrivate Key: {self.private_key}\nPrivate Point: {self.private_point}\n'

    def descifrar(self, ciphered_msg):
        '''Descifra un conjunto de parejas de puntos (e1, e2) de una curva elíptica a un texto
        plano legible humanamente'''
        if not ciphered_msg:
            return ""
        values = list(self.table.values())
        keys = list(self.table.keys())
        s = []
        for pareja in ciphered_msg:
            caracter_e1 = pareja[0]
            caracter_e2 = pareja[1]
            i_e1 = 0
            for i in range(len(keys)):
                if keys[i] == caracter_e1:
                    i_e1 = i
                    break
            i_e2 = 0
            for i in range(len(keys)):
                if keys[i] == caracter_e2:
                    i_e2 = i
                    break
            e1 = values[i_e1]
            e2 = values[i_e2]
            # M = e2 - (a(e1) + a(B1) + Be)
            a = self.private_key
            b1 = self.another_entity_public_key_1
            be = self.another_entity_public_key_3
            parte1 = self.curve.mult(a, e1)
            parte2 = self.curve.mult(a, b1)
            parte3 = self.curve.sum(parte1, parte2)
            parte4 = self.curve.sum(parte3, be)
            parte5 = self.curve.inv(parte4)
            m = self.curve.sum(e2, parte5)
            i_m = 0
            for i in range(len(values)):
                if values[i] == m:
                    i_m = i
                    break
            s += keys[i_m]
        #print(f'{self.name} descifro el mensaje! Dice: "{s}"')
        return ''.join(s)

    def cifrar(self, message):
        '''Cifra el mensaje (self.message) a puntos de la curva elíptica. Cada caracter es 
        mapeado a una pareja de puntos (e1, e2) con e1, e2 en EC.'''
        # Se usa un random para cada símbolo
        #print(f'\n{self.name} cifra el mensaje "{message}" como: ')
        if not message:
            return []
        values = list(self.table.values())
        keys = list(self.table.keys())
        self.cipher = []
        # Para cada caracter en el mensaje, calculamos e1 y e2
        for c in message:
            if c not in self.table:
                raise ValueError(f"No se encontró el caracter '{c}' en la tabla")
            # e1 = r(G)
            num_r = r.randint(1, self.order-1)
            e1 = self.curve.mult(num_r, self.generator_point)
            # e2 = M + (B + r)A1 - r(A2) + Ae
            m = self.table[c]
            b = self.private_key
            numerito = (b + num_r) % self.order
            a1 = self.another_entity_public_key_1
            a2 = self.another_entity_public_key_2
            ae = self.another_entity_public_key_3
            parte1 = self.curve.mult(numerito, a1)
            parte2 = self.curve.mult(num_r, a2)
            parte3 = self.curve.inv(parte2)
            parte4 = self.curve.sum(parte1, parte3)
            parte5 = self.curve.sum(parte4, ae)
            e2 = self.curve.sum(m, parte5)
            # Revisamos que los puntos si existan en la curva
            if not self.curve.isInCurve(e1) or not self.curve.isInCurve(e2):
                # Si no, intentamos de nuevo con un nuevo num_r
                continue
            # Revisamos que los puntos tenga un mapeo a un caracter
            tablita = self.table
            caracter_e1 = next((k for k, v in tablita.items() if v == e1), None)
            caracter_e2 = next((k for k, v in tablita.items() if v == e2), None)
            if caracter_e1 == None or caracter_e2 == None:
                # Si no, intentamos de nuevo con un nuevo num_r
                continue
            self.cipher.append((caracter_e1, caracter_e2))
        #print(self.cipher)
        return self.cipher

    def genera_llaves_publicas(self):
        '''Hace las operaciones correspondientes para generar la primera ronda de llaves
        públicas de esta entidad PK1 y PK2.'''
        self.public_key_1 = self.curve.mult(self.private_key, (self.curve.sum(self.generator_point, self.private_point)))
        self.public_key_2 = self.curve.mult(self.private_key, self.private_point)
        # print(f'{self.name} genera sus llaves públicas como \npk1{self.public_key_1}\tpk2{self.public_key_2}')
        #return (self.public_key_1, self.public_key_2, None) # TODO: ver si esta bien regresar None
        return (self.public_key_1, self.public_key_2)

    def recibe_llaves_publicas(self, public_keys):
        '''Recibe la llave publica de otra entidad y las guarda. (primera ronda solo guarda 2)
        o si ya es la segunda ronda, guarda la última llave (pk1, pk2 y pk3 != None)'''
        # print(public_keys) puede ser que alguna llave sea None, pero lo evitaremos por
        # motivos didácticos, pero no pasa nada, sigue funcionando
        #if public_keys[2] != None: # TODO: ver si es !=, si no regresar a ==
        if len(public_keys) == 3:
            # print(f'{self.name} añadió una llave pública más: {public_keys}\n')
            self.another_entity_public_key_3 = public_keys[2]
        else:
            self.another_entity_public_key_1 = public_keys[0]
            self.another_entity_public_key_2 = public_keys[1]
            # print(f'{self.name} recibe las llaves públicas de otra entidad y son: {public_keys}')

    def final_keys(self):
        '''Genera la última llave pública, en combinación con otra llave pública de otra entidad
        Regresa las 3 llaves públicas de esta entidad.'''
        #public_keys = (self.public_key_1, self.public_key_2, None) # TODO: veri si es una lista o una tupla
        public_keys = [self.public_key_1, self.public_key_2, None]
        self.public_key_3 = self.curve.mult(self.private_key, self.another_entity_public_key_2)
        public_keys[2] = self.public_key_3
        # print(f'{self.name} crea su llave final como {self.public_key_3}')
        # print(f'Todas las llaves publicas de {self.name} son: {public_keys}\n')
        return public_keys
    
    # Funcion para obtener un punto aleatorio de la curva, que no sea el punto al infinito o el inverso del punto generador
    def obtener_punto_aleatorio(self, curve, generator_point):
        puntos = curve.get_points()
        punto = None
        while True:
            punto = puntos[r.randint(0, len(puntos)-1)]
            if punto != None and curve.sum(punto, curve.inv(generator_point)) != None:
                #if curve.mult(self.private_key, punto) != None and curve.mult(self.private_key, curve.sum(punto, generator_point)) != None: # TODO: ver si este if es necesario
                    break
        return punto

