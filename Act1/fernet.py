# Hecho por: Victor Batarse y Jesús Mendoza
from cryptography.fernet import Fernet

# Generamos la clave
FeKey = Fernet.generate_key()
print("clave: ", FeKey, "\n")
# Creamos el objeto
f = Fernet(FeKey)
# Encryptamos el mensaje
token = f.encrypt(b"Secret message!")

print(token)


# decryptamos el mensaje
d = f.decrypt(token)

print("\n", d)

clave_2 = input("Ingrese la clave para descifrar el mensaje: ")
f_2 = Fernet(clave_2)
input_2 = input("Ingrese el mensaje cifrado: ")
token_2 = f_2.decrypt(input_2)

print(token_2)