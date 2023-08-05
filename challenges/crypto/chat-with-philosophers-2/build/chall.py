import os
import signal
import hashlib
import socketserver

from Crypto.Cipher import AES
from Crypto.Util.number import *

from secret import a_chat, b_chat

BLOCK_SIZE = 16


def pad(s):
    num = BLOCK_SIZE - (len(s) % BLOCK_SIZE)
    return s + bytes([num] * num)


def unpad(s):
    pad = s[-1]
    if pad > BLOCK_SIZE or pad < 1 or not all([_ == pad for _ in s[-pad:]]):
        raise Exception("padding error.")
    return s[:-s[-1]]


class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 1024
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

    def recv(self, prompt=b'> '):
        self.send(prompt, newline=False)
        return self._recvall()

    def timeout_handler(self, signum, frame):
        raise TimeoutError

    def handle(self):
        try:
            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(300)

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

            self.send(f'n = {n}'.encode())
            self.send(f'e = 3'.encode())

            # xiaoming generate session key
            k1 = getPrime(691)
            k2 = bytes_to_long(os.urandom(256)) % n
            leak = k2 >> 600

            c1 = pow(k1, e, n)
            c2 = pow(k2, e, n)
            self.send(f'c1 = {c1}'.encode())
            self.send(f'c2 = {c2}'.encode())
            self.send(f'leak={leak}'.encode())

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

            self.send("Xiaoming's chat".encode())

            a_enc = aes_a.encrypt(
                pad(b"Hello, Mr. Sartre. I have always admired your thinking, "
                    b"especially your contribution to existentialism. "
                    b"But I've been feeling empty lately and don't know what to do."
                    )).hex()
            self.send(a_enc.encode())

            for sentence in a_chat:
                a_enc = aes_a.encrypt(pad(sentence)).hex()
                self.send(a_enc.encode())

            self.send("Sartre's chat".encode())
            for sentence in b_chat:
                b_enc = aes_b.encrypt(pad(sentence)).hex()
                self.send(b_enc.encode())

            self.request.close()

        except TimeoutError:
            self.send(b'\nTimeout!')
        except Exception as err:
            self.send(b'Something Wrong!')
        finally:
            self.request.close()


class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10005
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
