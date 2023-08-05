import os
import base64
import sys

BANNER = """
 _______  _______  _______  _______
|       ||       ||       ||       |
|    ___||    ___||   _   ||  _____|
|   | __ |   | __ |  | |  || |_____
|   ||  ||   ||  ||  |_|  ||_____  |
|   |_| ||   |_| ||       | _____| |
|_______||_______||_______||_______|

Welcome to GGOS!
Upload your executable binary and you can run it on GGOS!

Note: You should use `xz -ze -9 -c <binary> | base64 -w 0` to compress your binary.
Note: Your binary will be stored in /APP/EXE.

Try to get GZTime's flag in /FLAG!"""

print(BANNER)

upload = input("Will you upload your binary? [Y/n] ").strip()

try:
    if upload != "n":
        binary = input("Base64 of binary: ").strip()

        with open("/home/ctf/EXE.xz", "wb") as f:
            f.write(base64.b64decode(binary))

        os.system("xz -d -c /home/ctf/EXE.xz > /home/ctf/esp/APP/EXE")

except:
    print("Cannot upload your binary.")

print("Booting GGOS...")
print("Please wait for a while...")

sys.stdout.flush()

qemu_cmd = [
    "timeout", "300",
    "qemu-system-x86_64",
    "-bios", "/home/ctf/OVMF.fd",
    "-net", "none",
    "-nographic",
    "-m", "48M",
    "-monitor", "/dev/null",
    "-drive", "format=raw,file=fat:rw:/home/ctf/esp",
    "-no-reboot"
]

os.system(" ".join(qemu_cmd))

print("GGOS is down. Bye!")
