import gmpy2
from Crypto.Util.number import *

bits = 512
gbits = 234


def proof_of_work():
    random.seed(os.urandom(8))
    proof = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"sha256(XXXX+{proof[4:]}) == {_hexdigest}".encode())
    x = input('Plz tell me XXXX: ')
    if len(x) != 4 or sha256(x + proof[4:].encode()).hexdigest() != _hexdigest:
        return False
    return True


def getN():
    g = getPrime(gbits)
    n = 1
    p,q = 0,0
    while True:
        a = getPrime(bits - gbits - 1)
        if gmpy2.is_prime(2 * g * a + 1):
            n *= (2 * a * g + 1)
            p = (2 * a * g + 1)
            break
    while True:
        b = getPrime(bits - gbits - 1)
        if gmpy2.is_prime(2 * g * b + 1):
            n *= (2 * b * g + 1)
            q = (2 * b * g + 1)
            break
    return n, g, p, q


if not roof_of_work():
    print('[!] Wrong!')
    exit(0)

print(b"So much has been leaked, can't be done ? 1997")
print(b"plz wait...")

n, leak, p, q = getN()

n, leak = getN()

e = 65537
m = bytes_to_long(flag)
c = pow(m, e, n)

print('n=', n)
print('g=', leak)
print('c=', c)
