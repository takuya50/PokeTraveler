import sys
from PIL import Image

charcode = {
    "A":  0,
    "B":  1,
    "C":  2,
    "D":  3,
    "E":  4,
    "F":  5,
    "G":  6,
    "H":  7,
    "I":  8,
    "J":  9,
    "K":  10,
    "L":  11,
    "M":  12,
    "N":  13,
    "O":  14,
    "P":  15,
    "Q":  16,
    "R":  17,
    "S":  18,
    "T":  19,
    "U":  20,
    "V":  21,
    "W":  22,
    "X":  23,
    "Y":  24,
    "Z":  25,
    ":":  28,
    ";":  29,
    "[":  30,
    "]":  31,
    "a":  32,
    "b":  33,
    "c":  34,
    "d":  35,
    "e":  36,
    "f":  37,
    "g":  38,
    "h":  39,
    "i":  40,
    "j":  41,
    "k":  42,
    "l":  43,
    "m":  44,
    "n":  45,
    "o":  46,
    "p":  47,
    "q":  48,
    "r":  49,
    "s":  50,
    "t":  51,
    "u":  52,
    "v":  53,
    "w":  54,
    "x":  55,
    "y":  56,
    "z":  57,
    " ":  58,
    "'m": 67,
    "'r": 68,
    "'s": 69,
    "'t": 70,
    "'v": 71,
    "'":  72,
    "-":  75,
    "?":  76,
    "!":  77,
    ".":  78,
    "♂":  84,
    "/":  87,
    "♀":  89,
    "0":  90,
    "1":  91,
    "2":  92,
    "3":  93,
    "4":  94,
    "5":  95,
    "6":  96,
    "7":  97,
    "8":  98,
    "9":  99,
    "_":  1000,
    "@":  1001,
    ":L": 1002,
}

# 文字データを画像に打ち込む
def typewrite(target_path, x, y, text):
    target = Image.open(target_path).copy()

    for i in range(len(text)):
        char_str = text[i]
        char_img_path = "asset/char/{}.png".format(charcode.get(char_str))
        char_img = Image.open(char_img_path)
        target.paste(char_img, (x+8*i, y), mask=char_img)

    target.save("result.png")

def main():
    args = sys.argv

    if len(args) < 5:
        print("typewriter.py <target> <x> <y> <text>")
        return

    target = args[1]
    x = int(args[2])
    y = int(args[3])
    text = args[4]
    typewrite(target, x, y, text)


if __name__ == "__main__":
    main()
