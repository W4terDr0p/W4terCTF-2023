import os
import socketserver

flag = os.environ['GZCTF_FLAG']

class Term:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    LIGHT = '\033[2m'

    TOP_LEFT = '\033[1;1H'
    TOP_CENTER = '\033[1;40H'

    CLEAR = '\033[2J'
    BACKSPACE = '\033[1D \033[1D'


BANNER = f"""{Term.BOLD}{Term.LIGHT}{Term.GREEN}
       _____  __                __
      / ___/ / /_   ____ _ ____/ /____  _      __
      \__ \ / __ \ / __ `// __  // __ \| | /| / /
     ___/ // / / // /_/ // /_/ // /_/ /| |/ |/ /
    /____//_/ /_/ \__,_/ \__,_/ \____/ |__/|__/

"""

PROMPT = f"{Term.LIGHT}{Term.WHITE}{Term.BOLD}>>> {Term.RESET}"

TALKS = [
    "Hello, Traveller.",
    "You have entered the realm of the shadow, where nothing is as it seems.",
    "You seek the flag, but you will not find it easily.",
    "It is hidden in plain sight, but only for those who can see beyond the surface.",
    "The flag is a fleeting glimpse, a momentary flash, a whisper in the dark.",
    "You must be quick and attentive, or you will miss it.",
    "The flag is here, but it is also gone.",
    "Can you catch it before it disappears?",
    "Good luck, Traveller."
]

part_len = len(flag) // len(TALKS)

if part_len * len(TALKS) < len(flag):
    part_len += 1

parts = [flag[i:i + part_len] for i in range(0, len(flag), part_len)]

class Task(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def recv_line(self):
        data = b''
        while True:
            part = self.request.recv(1)
            data += part
            if part == b'\n':
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += '\n'
            self.request.sendall(msg.encode())
        except:
            pass

    def handle(self):
        try:
            self.send(Term.CLEAR + Term.TOP_LEFT + BANNER)

            for i in range(len(TALKS)):
                self.send(PROMPT + Term.GREEN + Term.BOLD + TALKS[i], newline=False)
                part = parts[i]
                for j in range(len(part)):
                    self.send(part[j] + Term.BACKSPACE, newline=False)
                self.recv_line()
        except:
            pass

        self.request.close()

class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    print("Parts:", parts)
    HOST, PORT = '0.0.0.0', 70
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()
