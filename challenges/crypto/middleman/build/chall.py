import os
import hashlib
import socketserver
import signal

from Crypto.Util.number import *
from Crypto.Cipher import AES
from secret import gz_chat, mm_chat

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

    def recv(self, prompt=b'>'):
        self.send(prompt, newline=False)
        return self._recvall()

    def timeout_handler(self, signum, frame):
        raise TimeoutError

    def handle(self):
        try:
            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(300)

            pbits = 1024
            p = getStrongPrime(pbits)
            g = bytes_to_long(os.urandom(pbits // 8)) % p
            self.send(f'p={p}'.encode())
            self.send(f'g={g}'.encode())

            # GZtime
            gz_sk = bytes_to_long(os.urandom(pbits // 8)) % p
            gz_exc = pow(g, gz_sk, p)
            self.send(f'gz_exc={gz_exc}'.encode())

            # Mystery man
            mm_sk = bytes_to_long(os.urandom(pbits // 8)) % p
            mm_exc = pow(g, mm_sk, p)
            self.send(f'mm_exc={mm_exc}'.encode())

            gz_exc = int(self.recv())
            if gz_exc > p or gz_exc < 2:
                raise Exception("must in range")

            mm_share = hashlib.sha256(long_to_bytes(pow(gz_exc, mm_sk,
                                                        p))).digest()

            # Gztime
            mm_exc = int(self.recv())
            if mm_exc > p or mm_exc < 2:
                raise Exception("must in range")
            gz_share = hashlib.sha256(long_to_bytes(pow(mm_exc, gz_sk,
                                                        p))).digest()

            # generate AES key with session key
            shared_key_gz = gz_share[16:]
            iv_gz = gz_share[:16]

            shared_key_mm = mm_share[16:]
            iv_mm = mm_share[:16]

            aes_gz = AES.new(shared_key_gz, AES.MODE_CBC, iv_gz)
            aes_mm = AES.new(shared_key_mm, AES.MODE_CBC, iv_mm)

            # begin to chat

            for i in range(len(gz_chat)):
                gz_enc = aes_gz.encrypt(pad(gz_chat[i])).hex()
                self.send(f'GZTime: {gz_enc}\n'.encode())

                mm_enc = aes_mm.encrypt(pad(mm_chat[i])).hex()
                self.send(f'Mystery man: {mm_enc}\n'.encode())

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
    HOST, PORT = '0.0.0.0', 10007
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
