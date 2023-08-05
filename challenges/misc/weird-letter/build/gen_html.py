import sys
import hashlib
import random
import string

flag = sys.argv[1]
assert len(flag) > 0

def get_vigenere_key(seed):
    random.seed(seed)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(16))

def vigenere_encrypt(plaintext, key):
    # support both uppercase and lowercase
    encrypted = ''
    num_key = [ord(c) - ord('a') for c in key]
    count = 0
    for char in plaintext:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + num_key[count % len(num_key)]) % 26 + ord('A'))
            count += 1
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + num_key[count % len(num_key)]) % 26 + ord('a'))
            count += 1
        else:
            encrypted += char
    return encrypted

key = get_vigenere_key(hashlib.sha256(f"{flag}^2023W4terCTF".encode()).hexdigest())
worded_flag = flag.replace('_', ' underline ').replace('{', ' open brace ').replace('}', ' close brace')

letter = f"""Dear CTFer,

    I hope this message finds you well and that you're enjoying the excitement of CTF challenges. As you know, cryptography is a crucial component of many CTF challenges, and it's important to have a good understanding of the different encryption techniques that are used.

    In classic cryptography, the Vigenere and Caesar ciphers are popular choices. The Vigenere cipher is a polyalphabetic substitution cipher that uses a repeating keyword to encipher plaintext messages. It's a powerful encryption tool, but it can be cracked using frequency analysis. The Caesar cipher is a simpler substitution cipher that shifts each letter in the plaintext by a fixed number of positions down the alphabet. Modern cryptography offers more advanced encryption techniques such as the Advanced Encryption Standard (AES). AES is a symmetric encryption algorithm that uses a key to encrypt and decrypt data. It's designed to resist attacks from even the most advanced computers and is widely used to encrypt sensitive data. Asymmetric encryption is another important encryption technique that's used in CTF challenges. Asymmetric encryption uses two keys, a public key and a private key, to encrypt and decrypt data. It's commonly used in digital signatures and secure communication protocols.

    In conclusion, cryptography is a fascinating and challenging subject that's critical to CTF challenges. Whether you're new to CTF or an experienced CTFer, understanding the different encryption techniques is essential to succeed in these challenges. Keep exploring and have fun cracking those ciphers!

    Your flag is {worded_flag}.

Best regards,
Dr. 0p"""

encrypted_flag = vigenere_encrypt(letter, key).replace('    ', '&nbsp;&nbsp;&nbsp;&nbsp;').replace('\n', '<br/>')

html = open('template.html').read()
open('index.html', 'w').write(html.replace('{content}', encrypted_flag))

# print(f"key: {key}")
# print(f"worded_flag: {worded_flag}")
# print(f"letter: \n{letter}\n\n")
# print(f"enc: \n{encrypted_flag}")
