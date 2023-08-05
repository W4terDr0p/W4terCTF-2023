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
        try:
            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(60)
            if not self.proof_of_work():
                self.send(b'[!] Wrong!')
                self.request.close()
                return

            self.send(b"So much has been leaked, can't be done ? 1997")
            self.send(b"plz wait...")

            bits = 512
            gbits = 234

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

            n, leak, p, q = getN()

            e = 65537
            m = bytes_to_long(flag)
            c = pow(m, e, n)

            self.send('n={}'.format(n).encode())
            self.send('g={}'.format(leak).encode())
            self.send('c={}'.format(c).encode())

            self.request.close()
        except TimeoutError:
            self.send('Timeout!')
            self.request.close()
        except:
            self.send('???')
            self.request.close()

class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10001
    server = ForkedServer((HOST, PORT), Task)
    # server = ThreadedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    print(HOST, PORT)
    server.serve_forever()
