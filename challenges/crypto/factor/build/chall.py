from Crypto.Util.number import *
from hashlib import sha256
import gmpy2

import socketserver
import signal
import string
import random
import os

with open("flag", "rb") as f:
    flag = f.read()

class Task(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'[-] '):
        self.send(prompt, newline=False)
        return self._recvall()

    def timeout_handler(self, signum, frame):
        raise TimeoutError

    def proof_of_work(self):
        random.seed(os.urandom(8))
        proof = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
        _hexdigest = sha256(proof.encode()).hexdigest()
        self.send(f"sha256(XXXX+{proof[4:]}) == {_hexdigest}".encode())
        x = self.recv(prompt=b'Plz tell me XXXX: ')
        if len(x) != 4 or sha256(x + proof[4:].encode()).hexdigest() != _hexdigest:
            return False
        return True


    def handle(self):
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

        self.send('n={}'.format(n).encode())
        self.send('c={}'.format(c).encode())


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10002
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
