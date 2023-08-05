from Crypto.Util.number import *

with open("flag", "rb") as f:
    flag = f.read()

def gen_primes(nbit, balance):
    p = 2
    while len(bin(p)[2:]) < nbit - 2 * balance:
        factor = getPrime(balance)
        p *= factor
    left_bit = (nbit - len(bin(p)[2:])) // 2

    while True:
        r, s = [getPrime(left_bit) for _ in '01']
        _p = p * r * s
        if len(bin(_p)[2:]) < nbit: 
            left_bit += 1
        if len(bin(_p)[2:]) > nbit: 
            left_bit -= 1
        if isPrime(_p + 1):
            p = _p + 1
            break

    return p


nbit = 2048
balance = 22

p = gen_primes(nbit//2, balance)
q = gen_primes(nbit//2, balance)

n = p*q
e = 65537
m = bytes_to_long(flag)
c = pow(m, e, n)

print('n={}'.format(n).encode())
print('c={}'.format(c).encode())
