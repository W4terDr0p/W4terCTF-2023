import os

placeholder = b"W4terCTF{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}"

flag = os.environ['GZCTF_FLAG'].encode()

assert len(flag) == len(placeholder)

origin = open("/home/ctf/origin", "rb").read()

open("/home/ctf/app/lazy", "wb").write(origin.replace(placeholder, flag))
