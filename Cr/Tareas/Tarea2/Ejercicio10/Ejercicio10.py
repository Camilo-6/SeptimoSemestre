import random

def Es_Multiplo(n,m):
    es_multiplo = False
    if ((n%m) == 0):
        es_multiplo = True
    return es_multiplo

# Test de Fermat 1
def Fermat_Test(p):
    es_primo = True
    print("--------TEST DE FERMAT--------")
    print(f"Determinar si {p} es primo.")
    # Paso 1, iteramos a de 1 a p-1
    for a in range(1,p): 
        # Paso 1.1, calculamos resultado = a^p-a mod p
        resultado = (pow(a,p,p)-a)% p
        # Paso 1.2, si resultado es 0, entonces a^p-a es congruente a 0 mod p
        if(resultado == 0):
            print(f"{a}^{p}-{a} es congruente a 0 mod {p}")
        # Paso 1.3, si resultado es distinto de 0, entonces p es compuesto
        else: es_primo = False
        if (es_primo == False):
            print(f"{a}^{p}-{a} mod {p} = {resultado} es distinto a 0 por lo que {p} es un número compuesto")
            break
    # Paso 2, entonces p es primo
    if(es_primo):
        print(f"Todos los valores de 1 a {p-1} cumplen con la propiedad por tanto {p} es primo") 

def Jacobi_Symbol(a,n):
    s=0
    #Paso 1 - si a=0 regresa 0 
    if(a == 0):
        return 0
    #Paso 2 - si a=1 regresa 1
    if(a == 1):
        return 1
    #Paso 3 - decribimos a = 2^e * a_1 con a_1 impar
    ai, e = descomponer(a)
    #Paso 4 - Si es es par entonces s = 1
    if(e % 2 == 0):
        s = 1
    #En otro caso s = 1 si n congruente 1 o 7 módulo 8 
    # O s = -1 si n congruente a 3 o 5 mod 8
    else:
        if(n%8 == 1 or n%8 == 7):
            s = 1
        if(n%8 == 3 or n%8 == 5):
            s = -1
    #Paso 5 -si a_1 congruente a n concuentre a 3 mod 4 entonces s=-s
    if( n%4 == 3 and ai%4 ==3):
        s = -s
    #Paso 6 - Hacemos n_1= n mod a_1
    ni = n % ai
    #Paso 7 - Si a_1 entonces return s, en otro caso return s * jacobi (n1, a1)
    if(ai == 1):
        return(s)
    else: 
        return(s * Jacobi_Symbol(ni,ai))

# Test de Solovay-Strassen
def Solovay_Test(n,t):
    print("--------TEST DE SOLOVAY-TRASSEN --------\n")
    es_Primo=True
    # Paso 1, iteramos i de 1 a t
    for i in range(1,t):
        # Paso 1.1, seleccionamos un a aleatorio entre 2 y n-2
        a = random.randrange(2,n-2)
        print(f"a={a}")
        # Paso 1.2, calculamos  r = a^((n-1)/2) mod n
        r = pow(a,(n-1)//2 , n)
        print(f"r = {a}^(({n-1})/2) mod {n} = {r}")
        # Paso 1.3, si r != 1 y r != n-1, entonces n es compuesto
        if(r !=1 and r != (n-1)):
            print(f"{r} distinto de 1 y {n-1}")
            es_Primo = False
            print(f"{n} es compuesto ")
            break
        print("\nCalculando Símbolo de Jacobi")
        # Paso 1.4, calculamos el símbolo de Jacobi s = (a/n)
        s = Jacobi_Symbol(a,n)
        print(f" Símbolo de Jacobi s = {s}")
        # Paso 1.5, si r no es congruente con s, entonces n es compuesto
        if((r % n) != (s % n)):
            print(f"{r%n}---s = {s}--{n} es compuesto 2")
            es_Primo = False
            break
    # Paso 2, entonces n es primo
    if(es_Primo):
        print(f"{n} es primo")

def descomponer(n):
    print("Encontrar n-1=2^sr")
    bandera = True
    i = 1
    r=0
    while(bandera):
        div = n / pow(2,i)
        print(f"{n}/2^{i}={div}")
        if((div % 1) == 0 ):      
            i = i+1
        else:
            print("La división ya no es entera, así que los valores son")
            r = n // pow(2,i-1)
            bandera = False
        
    s = i-1
    print(f" r = {r} \n s = {s}\n") 
    return r, s

# Test de Miller-Rabin
def Miller_Test(n,t):
    print("--------TEST DE MILLER-RABIN--------\n")
    # Paso 1, escribimos a n-1 = 2^s * r con r impar
    r, s = descomponer(n-1)
    es_Primo = True
    # Paso 2, iteramos i de 1 a t
    for i in range (1,t):
        # Paso 2.1, seleccionamos un a aleatorio entre 2 y n-2
        a = random.randrange(2,n-2)
        # Paso 2.2, calculamos y = a^r mod n
        y =  pow(a,r,n)
        print(f" a = {a}")
        print(f"y = {a}^{r} mod {n} = {y}")
        # Paso 2.3, si y != 1 y y != n-1, entonces hacemos lo siguiente
        if((y !=1)and(y!=(n-1))):
            print(f"{y} distinto de 1 y {n}-1")
            # Paso 2.3.1, hacemos j = 1
            j = 1
            # Paso 2.3.2, mientras j <= s-1 y y != n-1, hacemos lo siguiente
            while((j <= (s-1))and(y != n-1)):
                # Paso 2.3.2.1, calculamos y = y^2 mod n
                y = pow(y,2,n)
                print(f"y = {y}")
                # Paso 2.3.2.2, si y = 1, entonces n es compuesto
                if(y==1):
                    print(f"{n} es compuesto")
                    es_Primo=False
                    break
                # Paso 2.3.2.3, incrementamos j en 1
                j=j+1
            # Paso 2.3.3, si y != n-1, entonces n es compuesto
            if(y!=n-1):
                print(f"{n} es compuesto")
                es_Primo = False
                break
    # Paso 3, entonces n es primo
    if(es_Primo):
        print(f"\n{n} es primo")

# Test de Fermat 2
def Fermat_Test2(n, t):
    # Paso 1, iteramos i de 1 a t
    for i in range(1,t):
        # Paso 1.1, seleccionamos un a aleatorio entre 2 y n-2
        a = random.randrange(2,n-2)
        # Paso 1.2, calculamos r = a^(n-1) mod n
        r = pow(a,n-1,n)
        # Paso 1.3, si r != 1, entonces n es compuesto
        if(r != 1):
            print(f"{n} es compuesto")
            return
    # Paso 2, entonces n es primo
    print(f"{n} es primo")

if __name__== "__main__":
    #Fermat_Test(131317)
    #Fermat_Test2(131317,100)
    #Solovay_Test(193394587, 10)
    Miller_Test(1346459137,479)
