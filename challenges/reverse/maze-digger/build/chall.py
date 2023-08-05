from hashlib import sha256
import string
import random
import os

maze_source = open('/home/ctf/maze.txt').readlines()
maze = [[int(i[k], 16) for k in range(0, 64)] for i in maze_source]


def proof_of_work():
    random.seed(os.urandom(8))
    proof = ''.join([
        random.choice(string.ascii_letters + string.digits) for _ in range(20)
    ])
    _hexdigest = sha256(proof.encode()).hexdigest()
    print(f"sha256(XXXX+{proof[4:]}) == {_hexdigest}")
    x = input('Plz tell me XXXX: ')
    if len(x) != 4 or sha256(
        (x + proof[4:]).encode()).hexdigest() != _hexdigest:
        return False
    return True


def passable(x, y, _dir):
    if _dir == 'w':
        return maze[x][y] & 1 == 0
    elif _dir == 'a':
        return maze[x][y] & 8 == 0
    elif _dir == 's':
        return maze[x][y] & 4 == 0
    elif _dir == 'd':
        return maze[x][y] & 2 == 0
    else:
        print(f"Invalid input: {_dir}")
        exit()


BANNER = '''
    ___  ___                    _ _
    |  \/  |                   | (_)
    | .  . | __ _ _______    __| |_  __ _  __ _  ___ _ __
    | |\/| |/ _` |_  / _ \  / _` | |/ _` |/ _` |/ _ \ '__|
    | |  | | (_| |/ /  __/ | (_| | | (_| | (_| |  __/ |
    \_|  |_/\__,_/___\___|  \__,_|_|\__, |\__, |\___|_|
                                     __/ | __/ |
                                    |___/ |___/

    Find the way to the (63, 63) to get the flag!
'''

if __name__ == '__main__':
    if not proof_of_work():
        print(b'[!] Wrong!')
        exit()

    print(BANNER)

    print(
        "Please give me the path from (0, 0) to (63, 63), use following keys to move:"
    )
    print("w: up, a: left, s: down, d: right, e.g. 'wasd'")
    print("Input your path:")

    path = input().strip()
    print()

    x, y = 0, 0

    for i in path:
        if not passable(x, y, i):
            print("Oops! You hit a wall!")
            exit()

        if i == 'w':
            x -= 1
        elif i == 'a':
            y -= 1
        elif i == 's':
            x += 1
        elif i == 'd':
            y += 1
        else:
            # unreachable
            exit()

        if x < 0 or x > 63 or y < 0 or y > 63:
            # unreachable
            print("Out of range!")
            exit()

        if x == 63 and y == 63:
            print("Congrats! You found the way to escape the maze!")
            flag = open('/home/ctf/flag.txt').read()
            print("Here is your flag: " + flag)
