n = 256961
e = 59029


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def Rho_Pollard(n):
    #Paso 1 - Declarar a=2 y b=2
    a = 2 
    b = 2
    #Paso 2 - Desde 1 hasta que ya no se pueda (xd) hacer lo siguiemte
    for i in range(1,100000000):
    #2.1- Calcular a = a^2+1 mod n, b = b^2+1 mod n y otra vez b = b^2+1 mod n 
        a = (pow(a,2)+1) % n
        print(f"Calculando a={a}^2+1 mod {n}={a}")
        b = (pow(b,2)+1) % n
        print(f"Calculando b={b}^2+1 mod {n}={b}") 
        b = (pow(b,2)+1) % n
        print(f"Calculando b={b}^2+1 mod {n}={b}") 
        # 2.2 Calcular d = gcd(a-b,n)
        d = gcd(a-b,n)
        print(f"\n gcd({a}-{b},{n}) = {d}")
        #2.3 Si 1<d<n regresar d y terminar con éxito
        if(1<d<n):
            print(f"Se cumple que 1 < {d} < {n} \n Tenemos un factor d = {d}")
            e = n//d
            print(f" El otro factor es e = {n} / {d} = {e}")
            print(f"\n ÉXITO, se contraron los factores de {n}\n Los factores son es d = {d}, e = {e}\n n = d*e = {d * e}")
            break
        #2.4 Si d =n terminar el algoritmo con fracaso
        if(d == n):
            print(f"FRACASO\n No se encontraron factores para {n}")
            break

#print(Rho_Pollard(n)) #293, 877

phi= (292)*(876)
#print(phi) #255792


def d(e,phi):
    """
    Fucnion que encuentra el valor de D siguiendo la siguiente formula
    d*e=1 mod phi(n)
    No es el mas eficiente pero es el mas sencillo de implementar, 
    con número muy grandes puede tardar mucho tiempo en encontrar el valor de d
    """
    d=0
    while True:
        if (d*e)%phi==1: #Vamos revisando si d*e cumple con la condicion
            break
        d+=1 # Si no cumple, aumentamos el valor de d
    return d

print(d(e,phi)) #13

def decipher(c,d,n):
    """
    Funcion que desencripta un mensaje cifrado en RSA
    """
    return (c**d)%n

def decipherWholeMessage(cipheredMessage,d,n):
    """
    Funcion que desencripta un mensaje completo
    """
    return [decipher(c,d,n) for c in cipheredMessage] 

message = [ 138527, 171279, 138664, 242409, 103298, 171279, 27261
,103786, 0, 103298, 0, 103298, 242409, 224525, 188808, 171279, 27261
]

print(decipherWholeMessage(message,13,256961))

# El ayudanete nos dijo que  el mensaje no tenia un cifrado extra
# por lo que podemos asumir que los numeros resultantes coinciden con 
# las letras del alfabeto, es decir 0=A, 1=B, 2=C, 3=D, etc.

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def numberTostring(numbers):
    """
    Funcion que convierte una lista de numeros en una cadena de texto
    """
    return "".join([alfabeto[n] for n in numbers])

print(numberTostring(decipherWholeMessage(message,13,256961)))