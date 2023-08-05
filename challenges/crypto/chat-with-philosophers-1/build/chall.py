import os
import signal
import socketserver
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.number import *

from ec import genCurve, genPoint
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

            curve = genCurve()
            while True:
                try:
                    G = genPoint(curve)
                    break
                except:
                    continue

            self.send(str(curve).encode())
            self.send(f'G={str(G)}'.encode())
            # print(curve)
            # print(G)

            # client1's private key
            sk_a = bytes_to_long(os.urandom(16)) % curve.p
            pk_a = curve.mul(G, sk_a)
            self.send(f'pk_a={str(pk_a)}'.encode())
            # print(pk_a)

            # client2's key
            sk_b = bytes_to_long(os.urandom(16)) % curve.p
            pk_b = curve.mul(G, sk_b)
            self.send(f'pk_b={str(pk_b)}'.encode())
            # print(pk_b)

            # client's shared key
            shared_key_a = sha256(str(curve.mul(pk_b, sk_a)).encode()).digest()[16:]
            iv_a = sha256(str(curve.mul(pk_b, sk_a)).encode()).digest()[:16]

            shared_key_b = sha256(str(curve.mul(pk_a, sk_b)).encode()).digest()[16:]
            iv_b = sha256(str(curve.mul(pk_a, sk_b)).encode()).digest()[:16]

            # assert shared_key_a == shared_key_b

            aes_a = AES.new(shared_key_a, AES.MODE_CBC, iv_a)

            aes_b = AES.new(shared_key_b, AES.MODE_CBC, iv_b)

            assert shared_key_a == shared_key_b
            assert iv_a == iv_b

            # begin to chat

            self.send(b"Xiaoming's chat")
            for sentence in a_chat:
                a_enc = aes_a.encrypt(pad(sentence)).hex()
                self.send(a_enc.encode())
                # print(a_enc)

            self.send(b"Nietzsche's chat")
            for sentence in b_chat:
                b_enc = aes_b.encrypt(pad(sentence)).hex()
                self.send(b_enc.encode())
                # print(b_enc)

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
    HOST, PORT = '0.0.0.0', 10004
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
