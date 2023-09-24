import math
from time import sleep

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def rgb_to_hsv(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    if mx == mn:
        h = 0
    elif mx == r and g >= b:
        h = (60 * (g - b) / (mx - mn) + 0)
    elif mx == r and g < b:
        h = (60 * (g - b) / (mx - mn) + 360)
    elif mx == g:
        h = (60 * (b - r) / (mx - mn) + 120)
    elif mx == b:
        h = (60 * (r - g) / (mx - mn) + 240)
    if mx == 0:
        s = 0
    else:
        s = (1 - mn / mx) * 100
    v = mx * 100
    return round(h), round(s), round(v)


def hsv_to_rgb(h, s, v):
    i = math.floor(h / 60) % 6
    vMin = (100 - s) * v / 100
    a = (h % 60) * (v - vMin) / 60
    vInc = vMin + a
    vDec = v - a

    if i == 0:
        return round(v * 255 / 100), round(vInc * 255 / 100), round(vMin * 255 / 100)
    elif i == 1:
        return round(vDec * 255 / 100), round(v * 255 / 100), round(vMin * 255 / 100)
    elif i == 2:
        return round(vMin * 255 / 100), round(v * 255 / 100), round(vInc * 255 / 100)
    elif i == 3:
        return round(vMin * 255 / 100), round(vDec * 255 / 100), round(v * 255 / 100)
    elif i == 4:
        return round(vInc * 255 / 100), round(vMin * 255 / 100), round(v * 255 / 100)
    elif i == 5:
        return round(v * 255 / 100), round(vMin * 255 / 100), round(vDec * 255 / 100)


def task3():
    image = Image.open("color.jpg")
    width, height = image.size

    myImage1 = Image.new("RGB", (width, height))

    hsv_arr = np.zeros((width, height, 3), dtype=int)

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            h, s, v = rgb_to_hsv(r, g, b)

            hsv_arr[x][y][0] = h
            hsv_arr[x][y][1] = s
            hsv_arr[x][y][2] = v
            # myImage1.putpixel((x, y), (h, s, v))

    for x in range(width):
        for y in range(height):
            h, s, v = hsv_arr[x][y][0], hsv_arr[x][y][1], hsv_arr[x][y][2]
            r, g, b = hsv_to_rgb(h, s, v)
            myImage1.putpixel((x, y), (r, g, b))

    myImage1.show()


#task3()