import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.number import *
from Crypto.Util.Padding import pad
from secret import gz_chat, mm_chat

pbits = 1024
p = getStrongPrime(pbits)
g = bytes_to_long(os.urandom(pbits // 8)) % p
print(f'p={p}')
print(f'g={g}')

# GZTime
gz_sk = bytes_to_long(os.urandom(pbits // 8)) % p
gz_exc = pow(g, gz_sk, p)
print(f'gz_exc={gz_exc}')

# Mystery man
mm_sk = bytes_to_long(os.urandom(pbits // 8)) % p
mm_exc = pow(g, mm_sk, p)
print(f'mm_exc={mm_exc}')

gz_exc = int(input('>'))
if gz_exc > p or gz_exc < 2:
    print('Something Wrong!')
mm_share = hashlib.sha256(long_to_bytes(pow(gz_exc, mm_sk, p))).digest()

# GZTime
mm_exc = int(input('>'))
if mm_exc > p or mm_exc < 2:
    print('Something Wrong!')
gz_share = hashlib.sha256(long_to_bytes(pow(mm_exc, gz_sk, p))).digest()

# generate AES key with session key
shared_key_gz = gz_share[16:]
iv_gz = gz_share[:16]

shared_key_mm = mm_share[16:]
iv_mm = mm_share[:16]

aes_gz = AES.new(shared_key_gz, AES.MODE_CBC, iv_gz)
aes_mm = AES.new(shared_key_mm, AES.MODE_CBC, iv_mm)

# begin to chat

for i in range(len(gz_chat)):
    gz_enc = aes_gz.encrypt(pad(gz_chat[i], 16)).hex()
    print(f'GZTime: {gz_enc}\n')

    mm_enc = aes_mm.encrypt(pad(mm_chat[i], 16)).hex()
    print(f'Mystery man: {mm_enc}\n')
