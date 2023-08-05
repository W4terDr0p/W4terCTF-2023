import os
import signal
import hashlib
import socketserver

from Crypto.Cipher import AES
from Crypto.Util.number import *

from secret import a_chat, Weber_chat, Marcuse_chat

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

            self.send('God helps you choose the parameters'.encode())

            n, k = 10, 4
            pbits = 1024
            p = getPrime(pbits)
            self.send(f'p={p}'.encode())

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

            self.send(f'Xiaoming, this is yours {x0, shadow[0]}'.encode())
            self.send(f'Weber, this is yours (x1, {shadow[1]})'.encode())
            self.send(f'Marcuse, this is yours (x2, {shadow[2]})'.encode())
            self.send(f'I think you may use this {shadow[3:]}'.encode())

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

            self.send("Xiaoming's chat".encode())

            a_enc = aes_a.encrypt(pad(b"Hello, Mr. Weber and Mr. Marcuse. "
                                      b"I've been feeling empty lately and don't know what to do.")).hex()
            self.send(a_enc.encode())

            for sentence in a_chat:
                a_enc = aes_a.encrypt(pad(sentence)).hex()
                self.send(a_enc.encode())

            self.send("Weber's chat".encode())
            for sentence in Weber_chat:
                b_enc = aes_b.encrypt(pad(sentence)).hex()
                self.send(b_enc.encode())

            self.send("Marcuse's chat".encode())
            for sentence in Marcuse_chat:
                c_enc = aes_c.encrypt(pad(sentence)).hex()
                self.send(c_enc.encode())

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
    HOST, PORT = '0.0.0.0', 10006
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
