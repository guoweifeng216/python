#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/28 11:49
@filename:asic_myself

"""

from PIL import Image
import argparse

parse=argparse.ArgumentParser()

parse.add_argument('file')
parse.add_argument('-o','--output')
parse.add_argument('--width',type=int,default=80)
parse.add_argument('--hight',type=int,default=80)

args=parse.parse_args()

IMG=args.file
WIDTH=args.width
HIGHT=args.hight
OUTPUT=args.output


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def grb_char(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

if __name__=='__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += grb_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)