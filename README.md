# W4terCTF 2023

[English](./README.md), [简体中文](./README.zh.md)

Repository for maintaining and building challenge images for W4terCTF 2023.

All challenges here are original. You can get the challenge images that can be directly used by GZ::CTF from [Packages](https://github.com/orgs/W4terDr0p/packages?repo_name=W4terCTF-2023).

Powered by [GZCTF](https://github.com/GZTimeWalker/GZCTF) and [GZTime](https://github.com/GZTimeWalker/)

NOTE: Some challenges are not publicly available for confidentiality reasons. Please understand.

## Challenge Designing Specification

- All challengs should follow the challenge specification of GZCTF. Dockerfile of the challenge should be placed to `challenges` directory.
- For each challenge, please create a specific branch with name `catagory/challenge_name` and develop in that branch. Finally squash merge to `main`.
- For those base images that can be shared and reused by different challengs, please place then in the `base` directory. For example, `xinetd`, `python`, `php`, etc.
- Please open an issue to track the developing progress of a challenge if it’s necessary.

## Challenges List

| Re  | Challenge                                                               | Catagory  | Difficulty | Tags                  | Author          |
| :-: | :---------------------------------------------------------------------- | :-------- | :--------- | :-------------------- | :-------------- |
|  0  | [NC Test](challenges/pwn/nc-test/)                                      | Pwn       | Baby       |                       | GZTime          |
|  0  | [Tic-Tac-Toe Level 0](challenges/pwn/tic-tac-toe-level-0/)              | Pwn       | Easy       | Stack overflow        | ConanC          |
|  0  | [Nimgame Level 1](challenges/pwn/nimgame-level-1/)                      | Pwn       | Easy       | Stack overflow        | Xia0o0o0o       |
|  0  | [Nimgame Level 2](challenges/pwn/nimgame-level-2/)                      | Pwn       | Normal     | Stack overflow        | Xia0o0o0o       |
|  0  | [2048](challenges/pwn/2048/)                                            | Pwn       | Normal     | fmtstr                | Xia0o0o0o       |
|  1  | [Dictionary](challenges/pwn/dictionary/)                                | Pwn       | Medium     | integer overflow, UaF | Xia0o0o0o       |
|  2  | [ELF Parser](challenges/pwn/elf-parser/)                                | Pwn       | Medium     | ELF, strcpy           | Xia0o0o0o       |
|  1  | [Cherry Lab](challenges/pwn/cherry-lab/)                                | Pwn       | Hard       | JS Engine             | Xia0o0o0o       |
|  0  | [Weird Letter](challenges/misc/weird-letter/)                           | Misc      | Trivial    | Vigenère              | GZTime          |
|  1  | [Shadow](challenges/misc/shadow/)                                       | Misc      | Easy       | Op Char               | GZTime          |
|  1  | [Chisato](challenges/misc/chisato/)                                     | Misc      | Normal     | PRNG                  | TonyCrane(AAA)  |
|  0  | [Spam 2023](challenges/misc/spam-2023/)                                 | Misc      | Normal     | Codec                 | GZTime          |
|  1  | [Good QRCode](challenges/misc/good-qrcode/)                             | Misc      | Normal     | QRCode, Mask          | GZTime          |
|  0  | [W4ter Disk](challenges/misc/w4ter-disk/)                               | Misc      | Medium     | RAID, btrfs           | GZTime          |
|  2  | [Bad QRCode](challenges/misc/bad-qrcode/)                               | Misc      | Hard       | QRCode, RS            | GZTime          |
|  1  | [Dark Maze](challenges/misc/dark-maze/)                                 | Misc      | Expert     | Maze, Revomaze        | GZTime          |
|  0  | [Evil Traffic](challenges/forensics/evil-traffic/)                      | Forensics | Normal     | SQL Injection         | GZTime          |
|  1  | [USB Hacker](challenges/forensics/usb-hacker)                           | Forensics | Medium     | USB Traffic           | GZTime          |
|  0  | [GZ RSA](challenges/crypto/gz-rsa/)                                     | Crypto    | Trivial    | RSA                   | peigong         |
|  0  | [Middleman](challenges/crypto/middleman/)                               | Crypto    | Trivial    | DH Middleman          | peigong         |
|  0  | [Factor](challenges/crypto/factor/)                                     | Crypto    | Easy       | RSA                   | peigong         |
|  0  | [Chat with Philosophers 1](challenges/crypto/chat-with-philosophers-1/) | Crypto    | Easy       | ECC                   | peigong         |
|  1  | [Chat with Philosophers 2](challenges/crypto/chat-with-philosophers-2/) | Crypto    | Easy       | RSA                   | peigong         |
|  2  | [Chat with Philosophers 3](challenges/crypto/chat-with-philosophers-3/) | Crypto    | Normal     | Shamir secret share   | peigong         |
|  1  | [NGG Smooth Prime](challenges/crypto/never-gonna-give-smooth-prime/)    | Crypto    | Medium     | Discrete logarithm    | ZMJ             |
|  1  | [Special RSA](challenges/crypto/special-rsa/)                           | Crypto    | Medium     | RSA                   | peigong         |
|  0  | [Login](challenges/crypto/login/)                                       | Crypto    | Medium     | AES padding oracle    | peigong         |
|  0  | [The Moment of Token](challenges/web/the-moment-of-token/)              | Web       | Easy       | JWT, Cookie           | GZTime          |
|  0  | [One Number SQL](challenges/web/one-number-sql/)                        | Web       | Normal     | SQL                   | tel             |
|  2  | [Feedback Box](challenges/web/feedback-box/)                            | Web       | Normal     | XSS                   | gbljdgb(Xp0int) |
|  0  | [Deser Plus](challenges/web/deser-plus/)                                | Web       | Medium     | PHP, deserialize      | tel             |
|  1  | [Nodejs Bypass](challenges/web/nodejs-bypass/)                          | Web       | Medium     | JS, prototype         | tel             |
|  0  | [Help Newnew Find Flag](challenges/web/help-new-new-find-flag/)         | Web       | Medium     | flask, pin            | Rieß(Xp0int)    |
|  1  | [Secure Password Generator](challenges/web/secure-password-generator/)  | Web       | Hard       | SQL                   | tel             |
|  1  | [Unfinished Website](challenges/web/unfinished-website/)                | Web       | Hard       | Java SSTI             | tel             |
|  0  | [Lazy Puts](challenges/reverse/lazy-puts/)                              | Reverse   | Trivial    |                       | GZTime          |
|  0  | [Oh My Python](challenges/reverse/oh-my-python/)                        | Reverse   | Trivial    | Python                | GZTime          |
|  1  | [Maze Digger](challenges/reverse/maze-digger/)                          | Reverse   | Hard       | WebAssembly, Rust     | GZTime          |
|  0  | [Quiz For PyGZ](challenges/ppc/quiz-for-pygz/)                          | PPC       | Easy       | Python                | GZTime          |
|  0  | [GGOS](challenges/ppc/ggos/)                                            | PPC       | Medium     | GGOS, Rust            | GZTime          |

## Difficulty and Points

| Difficulty                             | Baby | Trivial | Easy | Normal | Medium | Hard | Expert | Insane |
| :------------------------------------- | ---- | ------- | ---- | ------ | ------ | ---- | ------ | ------ |
| Initial Points                         | 200  | 500     | 1000 | 1000   | 1000   | 1000 | 1000   | 1000   |
| Minimum Points Ratio for Challenge     | 50%  | 20%     | 20%  | 20%    | 20%    | 20%  | 30%    | 30%    |
| Minimum Points for Challenge           | 100  | 100     | 200  | 200    | 200    | 200  | 300    | 300    |
| Difficulty Factor                      | 5.0  | 5.0     | 7.0  | 10.0   | 13.0   | 20.0 | 20.0   | 25.0   |
| Number of solves when reaching 50% pts | -    | 6       | 7    | 10     | 14     | 20   | 25     | 30     |

## Repository Structure

```
.github/workflows/                      # github actions
    └── chal.<category>.<name>.yml      # Building script for each challenge
base/                                   # Base image
challenges/                             # Challenges directory
    ├── challenge1/
    │   ├── build/                      # Challenge building directory
    │   │   ├── Dockerfile
    │   │   └── more...
    │   ├── attachments/                # Challenge attachment
    │   └── README.md
    ├── challenge2/
    └── more...
```

## File Directory

Please write the `Dockerfile` and place it in `challenges` then add corresponding building task action to `.github/workflows`. The naming should follow the format of chal.<challenge_name>.yml. The challenge needs to follow the GZCTF question specification.

- `base` directory

`base` contains the base images that can be shared and reused by some challenges, including `xinetd`, `python` image exposed based on `xinetd`.

- `challenges` directory

`challenges` contains Dockerfile of challenge and other files related to the challenges.
