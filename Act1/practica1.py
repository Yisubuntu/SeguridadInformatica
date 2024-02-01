from Crypto.Util import number as n
import random as r

#Ejercicio 1 - Obtener un número aleatorio
print("Ejercicio 1. Obtener un número aleatorio de 256 bits usando la función random: \n", r.getrandbits(256), "\n")

#Ejercicio 2 - Obtener un número primo
i = 0
while(True):
    i = i + 1
    j = r.getrandbits(1024)
    esPrimo = n.isPrime(j)
    if(esPrimo):
        print("En la iteración ", i, " se encontró el número primo: ", j, "\n")
        break

#Ejercicio 3 - Obtener inverso multiplicativo
def inversoMul(x,y):
    print("Ejercicio 3. El inverso multiplicativo del número ",x," y el número ",y," es: \n\n",n.inverse(x,y),"\n")

a = r.getrandbits(1024)
b = r.getrandbits(1024)

inversoMul(a,b)

#Ejercicio 4 - Potencia de un número 2^(e) mod p, donde "e" es un número de 256 y "p" es un primo de 1024 bits
a = 2
b = r.getrandbits(256)
c = j

def potencia(x,y,z):
    print("Ejercicio 4. La potencia de x a la y mod z es: ", pow(x,y,z))