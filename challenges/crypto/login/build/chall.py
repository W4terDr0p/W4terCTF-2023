import string, binascii
import random, os
import socketserver
import signal
from os import urandom
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.number import *


with open("flag", "rb") as f:
    FLAG = f.read()

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

    def proof_of_work(self):
        random.seed(os.urandom(8))
        proof = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(20)])
        _hexdigest = sha256(proof.encode()).hexdigest()
        self.send(f"sha256(XXXX+{proof[4:]}) == {_hexdigest}".encode())
        x = self.recv(prompt=b'Plz tell me XXXX: ')
        if len(x) != 4 or sha256(x + proof[4:].encode()).hexdigest() != _hexdigest:
            return False
        return True

    def timeout_handler(self, signum, frame):
        raise TimeoutError

    def handle(self):
        try:
            signal.signal(signal.SIGALRM, self.timeout_handler)
            signal.alarm(60)

            if not self.proof_of_work():
                self.send(b'\nWrong!')
                self.request.close()
                return

            self.send(b"Can you login?")

            key = urandom(16)
            iv = urandom(16)
            admin_creden = sha256(urandom(16)).digest()
            # print(admin_creden[:16], admin_creden[16:])

            clients = {}

            signal.alarm(600)

            while True:
                choice = self.recv()
                if (choice == b'1'):
                    try:
                        if len(clients) > 10:
                            self.send(b'[+] Too many clients')
                            break
                        self.send(b'[+] Please input your name')
                        name = self.recv()
                        associate_data = b'from client' + urandom(5)
                        aes = AES.new(key, AES.MODE_CBC, iv=iv)
                        ciphertext = aes.encrypt(associate_data + pad(sha256(name).digest())).hex().encode()
                        clients[name] = sha256(name).digest() + associate_data
                        self.send(b"[+] This is your credential: " + ciphertext)
                    except:
                        self.send(b"[!] ERROR!")
                elif (choice == b'2'):
                    try:
                        self.send(b'[+] Oh! I get the credential of the admin.')
                        associate_data = b'from admin' + urandom(6)
                        aes = AES.new(key, AES.MODE_CBC, iv=iv)
                        ciphertext = aes.encrypt(pad(associate_data + admin_creden)).hex().encode()
                        self.send(b"[+] Don't let the admin know that you got it : " + ciphertext)
                    except:
                        self.send(b"[!] ERROR!")
                elif (choice == b'3'):
                    try:
                        self.send(b'[+] Client login. Plz give me your name!')
                        name = self.recv()
                        self.send(b'[+] Client login. Plz give me the credential to login!')
                        client_credential = binascii.unhexlify(self.recv().strip())
                        aes = AES.new(key, AES.MODE_CBC, iv=iv)
                        if clients[name] == unpad(aes.decrypt(client_credential)):
                            self.send(b'[!] Login successful.')
                        else:
                            self.send(b'[!] Client not exist or your credential is wrong!')
                    except:
                        self.send(b"[!] ERROR!")
                elif (choice == b'4'):
                    self.send(b'[+] Admin login. Plz give me the credential to login!')
                    cred = binascii.unhexlify(self.recv())
                    if admin_creden == cred:
                        self.send(b'[!] You are admin, here is your flag: ' + FLAG)
                        break
                    else:
                        self.send(b'[!] Hey! You are not admin!')
                        self.send(b'[!] Go away!')
                        break
                elif (choice == b'5'):
                    self.send(b'[+] Bye~')
                    self.send(b'[+] See you next time!')
                    break
                else:
                    self.send(b'[!] What are you doing???')
                    self.send(b'[!] Go away!')
                    break

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
    HOST, PORT = '0.0.0.0', 10003
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
