import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import pad

from secret import a_chat, Weber_chat, Marcuse_chat

print('God helps you choose the parameters')

n, k = 10, 4
pbits = 1024
p = getPrime(pbits)
print(f'p={p}')

key = bytes_to_long(os.urandom(pbits // 8)) % p

# shamir secret sharing
a = [bytes_to_long(os.urandom(pbits // 8)) % p for _ in range(k - 1)]
shadow = []
x0 = bytes_to_long(os.urandom(pbits // 8)) % p
x = x0
for _ in range(n):
    p1, p2 = getRandomRange(11, 17), getRandomRange(11, 17)
    fx = key + sum((a[i] * pow(x, i + 1, p)) % p for i in range(0, k - 1))
    x = (p1 * x + p2) % p
    shadow.append(fx)

print(f'Xiaoming, this is yours {x0, shadow[0]}')
print(f'Weber, this is yours (x1, {shadow[1]})')
print(f'Marcuse, this is yours (x2, {shadow[2]})')
print(f'I think you may use this {shadow[3:]}')

# After opening the secret

# generate AES key with session key
shared_key_a = hashlib.sha256(long_to_bytes(key)).digest()[16:]
iv_a = hashlib.sha256(long_to_bytes(key)).digest()[:16]

shared_key_b = hashlib.sha256(long_to_bytes(key)).digest()[16:]
iv_b = hashlib.sha256(long_to_bytes(key)).digest()[:16]

shared_key_c = hashlib.sha256(long_to_bytes(key)).digest()[16:]
iv_c = hashlib.sha256(long_to_bytes(key)).digest()[:16]

aes_a = AES.new(shared_key_a, AES.MODE_CBC, iv_a)

aes_b = AES.new(shared_key_b, AES.MODE_CBC, iv_b)

aes_c = AES.new(shared_key_c, AES.MODE_CBC, iv_c)

# begin to chat

print("Xiaoming's chat")

a_enc = aes_a.encrypt(
    pad(
        b"Hello, Mr. Weber and Mr. Marcuse. "
        b"I've been feeling empty lately and don't know what to do.",
        16)).hex()
print(a_enc)

for sentence in a_chat:
    a_enc = aes_a.encrypt(pad(sentence, 16)).hex()
    print(a_enc)

print("Weber's chat")
for sentence in Weber_chat:
    b_enc = aes_b.encrypt(pad(sentence, 16)).hex()
    print(b_enc)

print("Marcuse's chat")
for sentence in Marcuse_chat:
    c_enc = aes_c.encrypt(pad(sentence, 16)).hex()
    print(c_enc)
