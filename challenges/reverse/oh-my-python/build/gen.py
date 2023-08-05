import os
import random
import py_compile

flag   = os.environ['GZCTF_FLAG'].encode()

nums   = [int.from_bytes(os.urandom(40), 'big') for _ in range(18)]

ans    = int.from_bytes(flag, 'big')
random.seed(ans)

for i in random.choices(nums, k = 5):
    ans ^= i

code   = f'''
import random

nums = {nums}

if __name__ == '__main__':
    flag = input('Input your flag: ').strip().encode()
    num = int.from_bytes(flag, 'big')

    random.seed(num)
    for i in random.choices(nums, k = 5):
        num ^= i

    if num == {ans}:
        print('Correct!')
    else:
        print('Wrong!')
'''

with open('code.py', 'w') as f:
    f.write(code)

py_compile.compile(file = "code.py", cfile = "app/ohmy.pyc", doraise = True)
