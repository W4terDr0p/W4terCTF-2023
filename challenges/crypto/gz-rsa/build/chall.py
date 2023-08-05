import os
import socketserver
from Crypto.Util.number import *
from secret import getGZprime

with open("flag", "rb") as f:
    flag = f.read()

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
            pbits = 1024
            p = getGZprime(pbits)
            q = getGZprime(pbits)
            n = p * q

            while True:
                e = bytes_to_long(os.urandom(pbits // 4)) % n
                if GCD(e, (p - 1) * (q - 1)) == 1:
                    break

            c = pow(bytes_to_long(flag), e, n)

            self.send(f'n = {n}'.encode())
            self.send(f'e = {e}'.encode())
            self.send(f'c = {c}'.encode())

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
    HOST, PORT = '0.0.0.0', 10008
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
