import random
import hashlib

# Paso 1: Definir los parámetros
g = 2  # generador
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF  # un primo grande en hexadecimal

# Paso 2: Generar las llaves privadas de Alice y Bob
a = random.getrandbits(256)  # clave privada de Alice
b = random.getrandbits(256)  # clave privada de Bob

# Paso 3: Simular el intercambio de números entre Alice y Bob
A = pow(g, a, p)  # Alice calcula A
B = pow(g, b, p)  # Bob calcula B

# Paso 4: Calcular la clave secreta s
s_Alice = pow(B, a, p)  # Alice calcula la clave secreta
s_Bob = pow(A, b, p)    # Bob calcula la clave secreta

# Paso 5: Verificar que las claves secretas sean iguales
hash_s_Alice = hashlib.sha256(str(s_Alice).encode()).hexdigest()
hash_s_Bob = hashlib.sha256(str(s_Bob).encode()).hexdigest()

if hash_s_Alice == hash_s_Bob:
    print("Las claves secretas son iguales y válidas.")
    print("Clave secreta generada:", hash_s_Alice)
else:
    print("Las claves secretas no coinciden.")
