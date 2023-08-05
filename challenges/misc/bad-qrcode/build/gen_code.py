import hashlib
import math
import qrcode
import sys
import numpy as np
from PIL import Image, ImageDraw

PIXEL_SIZE = 13
BORDER_SIZE = 2
MOSAIC_SIZE = 23
MOSAIC_NUM = 24
MOSAIC_X = BORDER_SIZE + 53
MOSAIC_Y = BORDER_SIZE + 223

def hash_padding(flag):
    hash_code = hashlib.sha256(f"5185cae744_{flag}_W4terCTF2023".encode()).hexdigest()
    return f"{hash_code[:32]}__{flag}__{hash_code[32:]}"

def gen_qrcode(flag):
    qr = qrcode.QRCode(version=11,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       box_size=PIXEL_SIZE,
                       border=BORDER_SIZE)
    qr.add_data(hash_padding(flag))
    img = qr.make_image(fill_color="black", back_color="white").convert('L')
    return img

def dirty_qrcode(img):
    ar = np.asarray(img, dtype='uint8').copy()

    # cut first 8 rows
    ar = ar[8 * PIXEL_SIZE:, :]
    ar[:2 * PIXEL_SIZE, :] = 255

    # do mosaic with average color
    for i, j in np.ndindex(MOSAIC_NUM, MOSAIC_NUM):
        x1 = MOSAIC_X + i * MOSAIC_SIZE
        x2 = MOSAIC_X + (i + 1) * MOSAIC_SIZE
        y1 = MOSAIC_Y + j * MOSAIC_SIZE
        y2 = MOSAIC_Y + (j + 1) * MOSAIC_SIZE
        mean = math.floor(ar[x1:x2, y1:y2].mean())
        ar[x1:x2, y1:y2] = mean

    # cut the upper left beveled corner
    img = Image.fromarray(ar, mode='L')

    corner_size = (15 + BORDER_SIZE) * (PIXEL_SIZE + 1)
    draw = ImageDraw.Draw(img)
    draw.polygon([(0, 0), (corner_size, 0), (0, corner_size)], fill=255)

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
    img = dirty_qrcode(img)
    img.save('qrcode.png')
