import os
from Crypto.Util.number import *
from secret import getGZprime

with open("flag", "rb") as f:
    flag = f.read()

pbits = 1024
p = getGZprime(pbits)
q = getGZprime(pbits)
n = p * q

while True:
    e = bytes_to_long(os.urandom(pbits // 4)) % n
    if GCD(e, (p - 1) * (q - 1)) == 1:
        break

c = pow(bytes_to_long(flag), e, n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
