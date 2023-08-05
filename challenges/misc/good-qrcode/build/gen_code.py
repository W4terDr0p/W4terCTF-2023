import hashlib
import qrcode
import random
import sys

PIXEL_SIZE = 13
BORDER_SIZE = 2
RAND_MASK = random.randint(0, 7)

def hash_padding(flag):
    hash_code = hashlib.sha256(
        f"aehpvsvq0_{flag}_W4terCTF2023".encode()).hexdigest()
    return f"{hash_code[:32]}__{flag}__{hash_code[32:]}"


try:
    original_mask_func
except NameError:
    original_mask_func = qrcode.util.mask_func


def mask_func(pattern):
    if pattern == RAND_MASK:
        print(f"Hack: Mask {RAND_MASK} is means no mask")
        return lambda i, j: False
    return original_mask_func(pattern)


if qrcode.util.mask_func is not mask_func:
    qrcode.util.mask_func = mask_func


def gen_qrcode(flag):
    qr = qrcode.QRCode(version=9,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=PIXEL_SIZE,
                       mask_pattern=RAND_MASK,
                       border=BORDER_SIZE)
    qr.add_data(hash_padding(flag))
    img = qr.make_image(fill_color="black", back_color="white").convert('L')
    return img


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python gen_code.py <flag>")
        sys.exit(1)

    flag = sys.argv[1]
    if flag.strip() == '':
        flag = 'W4terCTF{a_test_flag}'

    print(f"Running with flag: {flag}")
    img = gen_qrcode(flag)
    img.save('qrcode.png')
