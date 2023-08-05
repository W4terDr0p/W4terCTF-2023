import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import pad

from secret import a_chat, b_chat

# Sartre's key
while True:
    p = getPrime(1024)
    if (p - 1) % 3 == 0:
        continue
    q = getPrime(1024)
    if (q - 1) % 3 == 0:
        continue
    n = p * q
    e = 3
    d = inverse(e, (p - 1) * (q - 1))
    break

print(f'n = {n}')
print(f'e = 3')

# xiaoming generate session key
k1 = getPrime(691)
k2 = bytes_to_long(os.urandom(256)) % n
leak = k2 >> 600

c1 = pow(k1, e, n)
c2 = pow(k2, e, n)
print(f'c1 = {c1}')
print(f'c2 = {c2}')
print(f'leak={leak}')

# Sartre's decrypt c and get session key
m1 = pow(c1, d, n)
m2 = pow(c2, d, n)

# generate AES key with session key
shared_key_a = hashlib.sha256(long_to_bytes(k1 * k2)).digest()[16:]
iv_a = hashlib.sha256(long_to_bytes(k1 * k2)).digest()[:16]

shared_key_b = hashlib.sha256(long_to_bytes(m1 * m2)).digest()[16:]
iv_b = hashlib.sha256(long_to_bytes(m1 * m2)).digest()[:16]

aes_a = AES.new(shared_key_a, AES.MODE_CBC, iv_a)

aes_b = AES.new(shared_key_b, AES.MODE_CBC, iv_b)

# begin to chat

print("Xiaoming's chat")

a_enc = aes_a.encrypt(
    pad(
        b"Hello, Mr. Sartre. I have always admired your thinking, "
        b"especially your contribution to existentialism. "
        b"But I've been feeling empty lately and don't know what to do.",
        16)).hex()
print(a_enc)

for sentence in a_chat:
    a_enc = aes_a.encrypt(pad(sentence, 16)).hex()
    print(a_enc)

print("Sartre's chat")
for sentence in b_chat:
    b_enc = aes_b.encrypt(pad(sentence, 16)).hex()
    print(b_enc)
