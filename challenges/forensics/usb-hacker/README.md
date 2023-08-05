# USB Hacker

**Author:** GZTime

**Difficulty:** Medium

**Category:** Forensics

## 题目描述

为了获取到藏在 GZ 大脑中的 flag，你偷偷在他的键盘上安装了监听程序，并成功拿到了一段 USB 流量。

——那么就只剩从流量中获取 flag 了！

## 题目解析

解析流量：

```py
os.system("tshark -r %s -T fields -e usb.capdata | sed '/^\s*$/d' > %s" %
          (pcapFilePath, DataFileName))
```

解析按键：

```py
normalKeys = {
    "04": "a", "05": "b", "06": "c", "07": "d", "08": "e", "09": "f", "0a": "g", "0b": "h",
    "0c": "i", "0d": "j", "0e": "k", "0f": "l", "10": "m", "11": "n", "12": "o", "13": "p",
    "14": "q", "15": "r", "16": "s", "17": "t", "18": "u", "19": "v", "1a": "w", "1b": "x",
    "1c": "y", "1d": "z", "1e": "1", "1f": "2", "20": "3", "21": "4", "22": "5", "23": "6",
    "24": "7", "25": "8", "26": "9", "27": "0",
    "28": "<RET>", "29": "<ESC>", "2a": "<DEL>", "2b": "\t", "2c": "<SPACE>", "2d": "-",
    "2e": "=", "2f": "[", "30": "]", "31": "\\", "32": "<NON>", "33": ";", "34": "'",
    "35": "<GA>", "36": ",", "37": ".", "38": "/", "39": "<CAP>", "3a": "<F1>", "3b": "<F2>",
    "3c": "<F3>", "3d": "<F4>", "3e": "<F5>", "3f": "<F6>", "40": "<F7>",
    "41": "<F8>", "42": "<F9>", "43": "<F10>", "44": "<F11>", "45": "<F12>"
}

shiftKeys = {
    "04": "A", "05": "B", "06": "C", "07": "D", "08": "E", "09": "F", "0a": "G", "0b": "H",
    "0c": "I", "0d": "J", "0e": "K", "0f": "L", "10": "M", "11": "N", "12": "O", "13": "P",
    "14": "Q", "15": "R", "16": "S", "17": "T", "18": "U", "19": "V", "1a": "W", "1b": "X",
    "1c": "Y", "1d": "Z", "1e": "!", "1f": "@", "20": "#", "21": "$", "22": "%", "23": "^",
    "24": "&", "25": "*", "26": "(", "27": ")",
    "28": "<RET>", "29": "<ESC>", "2a": "<DEL>", "2b": "\t", "2c": "<SPACE>", "2d": "_",
    "2e": "+", "2f": "{", "30": "}", "31": "|", "32": "<NON>", "33": '"', "34": ":",
    "35": "<GA>", "36": "<", "37": ">", "38": "?", "39": "<CAP>", "3a": "<F1>", "3b": "<F2>",
    "3c": "<F3>", "3d": "<F4>", "3e": "<F5>", "3f": "<F6>", "40": "<F7>",
    "41": "<F8>", "42": "<F9>", "43": "<F10>", "44": "<F11>", "45": "<F12>"
}

presses = []
with open(DataFileName, "r") as f:
    for line in f:
        presses.append(line)

result = ""
processed_result = ""
caps_lock = False
last_shift = False

for press in presses:
    if len(press.strip()) == 0:
        continue

    if press.strip() == "00" * 8:
        continue

    Bytes = [press[i:i+2] for i in range(0, len(press), 2)]

    if last_shift:
        last_shift = False
        continue

    if Bytes[2] != "00":
        shift_flag = Bytes[0] == "02" or Bytes[0] == "20"
        normal_flag = Bytes[0] == "00"

        if not last_shift and shift_flag:
            last_shift = True

        key = shiftKeys[Bytes[2]] if shift_flag else normalKeys[Bytes[2]]
        result += key

        if Bytes[2] == "39":    # <CAP>
            caps_lock = not caps_lock
        elif Bytes[2] == "2a":  # <DEL>
            processed_result = processed_result[:-1]
        else:
            if int(Bytes[2], 16) <= 0x1d:
                shift = (caps_lock and normal_flag) or (not caps_lock and shift_flag)
            else:
                shift = shift_flag

            processed_result += shiftKeys[Bytes[2]] if shift else normalKeys[Bytes[2]]

print(processed_result)
```
