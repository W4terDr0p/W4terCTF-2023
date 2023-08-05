import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import pad
from secret import a_chat, b_chat
from ec import genCurve, genPoint

curve = genCurve()
G = genPoint(curve)
print(curve)
print(f'G={G}')

# client1's private key
sk_a = bytes_to_long(os.urandom(16)) % curve.p
pk_a = curve.mul(G, sk_a)
print(f'pk_a={pk_a}')

# client2's key
sk_b = bytes_to_long(os.urandom(16)) % curve.p
pk_b = curve.mul(G, sk_b)
print(f'pk_b={pk_b}')

# client's shared key
shared_key_a = hashlib.sha256(str(curve.mul(pk_b, sk_a)).encode()).digest()[16:]
iv_a = hashlib.sha256(str(curve.mul(pk_b, sk_a)).encode()).digest()[:16]

shared_key_b = hashlib.sha256(str(curve.mul(pk_a, sk_b)).encode()).digest()[16:]
iv_b = hashlib.sha256(str(curve.mul(pk_a, sk_b)).encode()).digest()[:16]

aes_a = AES.new(shared_key_a, AES.MODE_CBC, iv_a)

aes_b = AES.new(shared_key_b, AES.MODE_CBC, iv_b)

# begin to chat

print("xiaoming's chat")
for sentence in a_chat:
    a_enc = aes_a.encrypt(pad(sentence, 16)).hex()
    print(a_enc)

print("Nietzsche's chat")
for sentence in b_chat:
    b_enc = aes_b.encrypt(pad(sentence, 16)).hex()
    print(b_enc)
