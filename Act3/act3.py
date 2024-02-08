import random
import hashlib

# Parámetros Diffie-Hellman
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
g = 2

# Generación de llaves privadas aleatorias
alice_private_key = random.randint(0, p)
bob_private_key = random.randint(0, p)  
eve_private_key = random.randint(0, p)

# Intercambio de claves públicas
alice_public_key = pow(g, alice_private_key, p)
bob_public_key = pow(g, bob_private_key, p)
eve_public_key = pow(g, eve_private_key, p)

# Cálculo de llaves compartidas
alice_eve_key = pow(alice_public_key, eve_private_key, p)
eve_bob_key = pow(eve_public_key, bob_private_key, p)
bob_eve_key = pow(bob_public_key, eve_private_key, p)
eve_alice_key = pow(eve_public_key, alice_private_key, p)

print("\nLlave compartida Alice-Eve:", alice_eve_key)
print("\nLlave compartida Eve-Bob:", bob_eve_key)

if bob_eve_key == eve_bob_key and alice_eve_key == eve_alice_key:
  print("\nMITM exitoso! Las llaves coinciden.")
  
# Aplicar hash a la llave  
key_hash = hashlib.sha256(str(alice_eve_key).encode()).hexdigest() 
print("\nLlave hash:", key_hash)

# Intercambio de mensajes
message_a = "Hola Bob, soy Alice"  
message_b = "Hola Alice, aquí Bob"

print("\nMensaje de Alice:", message_a)
print("\nMensaje interceptado por Eve:", message_a) 

print("\nMensaje de Bob:", message_b)
print("\nMensaje interceptado por Eve:", message_b)