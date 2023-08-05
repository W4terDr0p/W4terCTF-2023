import hashlib
import subprocess

FLAG = open('/flag.txt', 'r').read().strip()

BANNER = '''

 ______            _                     _____        _
(_____ \      _   | |                   / ___ \      (_)
 _____) )   _| |_ | | _   ___  ____    | |   | |_   _ _ _____
|  ____/ | | |  _)| || \ / _ \|  _ \   | |   |_| | | | (___  )
| |    | |_| | |__| | | | |_| | | | |   \ \____| |_| | |/ __/
|_|     \__  |\___)_| |_|\___/|_| |_|    \_____)\____|_(_____)
       (____/

'''

QUESTION_ID = 1


def put_question(question):
    global QUESTION_ID
    print(f'[+] Question {QUESTION_ID}')
    print(f'    {question}')
    print()

    QUESTION_ID += 1

    return input('[-] Answer: ').strip()


def run_code(code):
    if not 0 < len(code) < 1024:
        print('[!] Code is too long!')
        return False

    p = subprocess.run(
        [
            "su", "nobody", "-s", "/bin/sh", "-c",
            "/usr/local/bin/python -c 'exec(input())'"
        ],
        input=code.encode(),
        stdout=subprocess.PIPE,
    )

    if p.returncode != 0:
        print('[!] Code failed to run!')
        return False

    output = p.stdout.decode().strip()

    print('[+] Output: ' + output)

    return output


def check(ret):
    if not ret:
        print('[!] You failed to pass this question!')
        exit()


print(BANNER)
print('Welcome to the quiz for PyGZ!')
print(
    'In following questions, you will be asked to write some one-line answers.'
)

answer = put_question('Write a python program that prints "Hello World!"')
output = run_code(answer)
check(output == 'Hello World!')

answer = put_question(
    'Write a python program that prints the answer to the life, the universe, and everything'
)
output = run_code(answer)
check(output == '42')

answer = put_question(
    'Give me three numbers so they satisfy x^3 + y^3 + z^3 is the answer to the previous question (split by space)'
)
ret = answer.split()
check(len(ret) == 3)
x, y, z = map(int, answer.split())
check(x**3 + y**3 + z**3 == 42)

answer = put_question('Write a python program that prints its own source code')
output = run_code(answer)
check(output == answer)

answer = put_question('Write a python program that prints its own sha256 hash')
output = run_code(answer)
check(hashlib.sha256(answer.encode()).hexdigest() == output)

print('''
[+] Congratulations! You have passed all the questions in the PyGZ quiz!
[+] Here is your flag: {0}
'''.format(FLAG))
