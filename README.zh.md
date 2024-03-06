# W4terCTF 2023

本仓库用于存储和构建 W4terCTF 2023 的题目镜像。

所有题目均为原创，可以从 [Packages](https://github.com/orgs/W4terDr0p/packages?repo_name=W4terCTF-2023) 中获取可以被 GZCTF 直接使用的题目镜像。

Powered by [GZCTF](https://github.com/GZTimeWalker/GZCTF) and [GZTime](https://github.com/GZTimeWalker/)

NOTE: 部分题目因保密原因不公开，请各位谅解。

## 出题规范

- 题目应遵循 GZCTF 的题目规范，题目的 Dockerfile 应放置在 `challenges` 目录下。
- 对于每道题目，应创建一个单独的 branch，命名为 `<分类>/<题目名>`，并在该 branch 中进行相关操作，最后 squash merge 到 main 分支。
- 对于能够共用的题目基础镜像，应放置在 `base` 目录下。如 `xinetd`、`python`、`php` 等。
- 如有必要，可以开启一个 issue 来追踪题目的出题进度。

## 题目列表

| Re  | 题目名                                                                  | 分类      | 难度    | 标签                  | 出题人          |
| :-: | :---------------------------------------------------------------------- | :-------- | :------ | :-------------------- | :-------------- |
|  0  | [NC Test](challenges/pwn/nc-test/)                                      | Pwn       | Baby    |                       | GZTime          |
|  0  | [Tic-Tac-Toe Level 0](challenges/pwn/tic-tac-toe-level-0/)              | Pwn       | Easy    | Stack overflow        | ConanC          |
|  0  | [Nimgame Level 1](challenges/pwn/nimgame-level-1/)                      | Pwn       | Easy    | Stack overflow        | Xia0o0o0o       |
|  0  | [Nimgame Level 2](challenges/pwn/nimgame-level-2/)                      | Pwn       | Normal  | Stack overflow        | Xia0o0o0o       |
|  0  | [2048](challenges/pwn/2048/)                                            | Pwn       | Normal  | fmtstr                | Xia0o0o0o       |
|  1  | [Dictionary](challenges/pwn/dictionary/)                                | Pwn       | Medium  | integer overflow, UaF | Xia0o0o0o       |
|  2  | [ELF Parser](challenges/pwn/elf-parser/)                                | Pwn       | Medium  | ELF, strcpy           | Xia0o0o0o       |
|  1  | [Cherry Lab](challenges/pwn/cherry-lab/)                                | Pwn       | Hard    | JS Engine             | Xia0o0o0o       |
|  0  | [Weird Letter](challenges/misc/weird-letter/)                           | Misc      | Trivial | Vigenère              | GZTime          |
|  1  | [Shadow](challenges/misc/shadow/)                                       | Misc      | Easy    | Op Char               | GZTime          |
|  1  | [Chisato](challenges/misc/chisato/)                                     | Misc      | Normal  | PRNG                  | TonyCrane(AAA)  |
|  0  | [Spam 2023](challenges/misc/spam-2023/)                                 | Misc      | Normal  | Codec                 | GZTime          |
|  1  | [Good QRCode](challenges/misc/good-qrcode/)                             | Misc      | Normal  | QRCode, Mask          | GZTime          |
|  0  | [W4ter Disk](challenges/misc/w4ter-disk/)                               | Misc      | Medium  | RAID, btrfs           | GZTime          |
|  2  | [Bad QRCode](challenges/misc/bad-qrcode/)                               | Misc      | Hard    | QRCode, RS            | GZTime          |
|  1  | [Dark Maze](challenges/misc/dark-maze/)                                 | Misc      | Expert  | Maze, Revomaze        | GZTime          |
|  0  | [Evil Traffic](challenges/forensics/evil-traffic/)                      | Forensics | Normal  | SQL Injection         | GZTime          |
|  1  | [USB Hacker](challenges/forensics/usb-hacker)                           | Forensics | Medium  | USB Traffic           | GZTime          |
|  0  | [GZ RSA](challenges/crypto/gz-rsa/)                                     | Crypto    | Trivial | RSA                   | peigong         |
|  0  | [Middleman](challenges/crypto/middleman/)                               | Crypto    | Trivial | DH Middleman          | peigong         |
|  0  | [Factor](challenges/crypto/factor/)                                     | Crypto    | Easy    | RSA                   | peigong         |
|  0  | [Chat with Philosophers 1](challenges/crypto/chat-with-philosophers-1/) | Crypto    | Easy    | ECC                   | peigong         |
|  1  | [Chat with Philosophers 2](challenges/crypto/chat-with-philosophers-2/) | Crypto    | Easy    | RSA                   | peigong         |
|  2  | [Chat with Philosophers 3](challenges/crypto/chat-with-philosophers-3/) | Crypto    | Normal  | Shamir secret share   | peigong         |
|  1  | [NGG Smooth Prime](challenges/crypto/never-gonna-give-smooth-prime/)    | Crypto    | Medium  | Discrete logarithm    | ZMJ             |
|  1  | [Special RSA](challenges/crypto/special-rsa/)                           | Crypto    | Medium  | RSA                   | peigong         |
|  0  | [Login](challenges/crypto/login/)                                       | Crypto    | Medium  | AES padding oracle    | peigong         |
|  0  | [The Moment of Token](challenges/web/the-moment-of-token/)              | Web       | Easy    | JWT, Cookie           | GZTime          |
|  0  | [One Number SQL](challenges/web/one-number-sql/)                        | Web       | Normal  | SQL                   | tel             |
|  2  | [Feedback Box](challenges/web/feedback-box/)                            | Web       | Normal  | XSS                   | gbljdgb(Xp0int) |
|  0  | [Deser Plus](challenges/web/deser-plus/)                                | Web       | Medium  | PHP, deserialize      | tel             |
|  1  | [Nodejs Bypass](challenges/web/nodejs-bypass/)                          | Web       | Medium  | JS, prototype         | tel             |
|  0  | [Help Newnew Find Flag](challenges/web/help-new-new-find-flag/)         | Web       | Medium  | flask, pin            | Rieß(Xp0int)    |
|  1  | [Secure Password Generator](challenges/web/secure-password-generator/)  | Web       | Hard    | SQL                   | tel             |
|  1  | [Unfinished Website](challenges/web/unfinished-website/)                | Web       | Hard    | Java SSTI             | tel             |
|  0  | [Lazy Puts](challenges/reverse/lazy-puts/)                              | Reverse   | Trivial |                       | GZTime          |
|  0  | [Oh My Python](challenges/reverse/oh-my-python/)                        | Reverse   | Trivial | Python                | GZTime          |
|  1  | [Maze Digger](challenges/reverse/maze-digger/)                          | Reverse   | Hard    | WebAssembly, Rust     | GZTime          |
|  0  | [Quiz For PyGZ](challenges/ppc/quiz-for-pygz/)                          | PPC       | Easy    | Python                | GZTime          |
|  0  | [GGOS](challenges/ppc/ggos/)                                            | PPC       | Medium  | GGOS, Rust            | GZTime          |

## 难度与分值

| 题目难度         | Baby | Trivial | Easy | Normal | Medium | Hard | Expert | Insane |
| :--------------- | ---- | ------- | ---- | ------ | ------ | ---- | ------ | ------ |
| 题目分值         | 200  | 500     | 1000 | 1000   | 1000   | 1000 | 1000   | 1000   |
| 题目最低分值比例 | 50%  | 20%     | 20%  | 20%    | 20%    | 20%  | 30%    | 30%    |
| 题目最低分值     | 100  | 100     | 200  | 200    | 200    | 200  | 300    | 300    |
| 难度系数         | 5.0  | 5.0     | 7.0  | 10.0   | 13.0   | 20.0 | 20.0   | 25.0   |
| 50% 分值次数     | -    | 6       | 7    | 10     | 14     | 20   | 25     | 30     |

## 项目结构

```
.github/workflows/                      # github actions
    └── chal.<category>.<name>.yml      # 每个题目的编译脚本
base/                                   # 基础镜像
challenges/                             # 题目目录
    ├── challenge1/
    │   ├── build/                      # 题目构建目录
    │   │   ├── Dockerfile
    │   │   └── more...
    │   ├── attachments/                # 题目附件目录
    │   └── README.md
    ├── challenge2/
    └── more...
```

## 文件目录

编写 `Dockerfile` 并放置在 `challenges` 目录下，然后在 `.github/workflows` 中添加对应的构建任务。命名应该遵循 `chal.<题目名>.yml` 的格式，题目需要遵循 GZCTF 的题目规范。

- `base` 目录

`base` 目录下存放了部分题目所需的基础镜像，包括 `xinetd`、基于 `xinetd` 暴露的 `python` 镜像。

- `challenges` 目录

`challenges` 目录下存放了题目的 Dockerfile，以及题目的相关文件。
