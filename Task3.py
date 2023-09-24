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
        s = (1 - mn / mx)
    v = mx
    return round(h), round(s), round(v)


def task3():
    image = Image.open("color.jpg")
    w, h = image.size
    myImage1 = Image.new("RGB", (w, h))
    hsv_arr = np.zeros((w, h), dtype=int)

    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            h, s, v = rgb_to_hsv(r, g, b)
           # hsv_arr[x][y] = ([r, g, b])
            myImage1.putpixel((x, y), (h, s, v))

    myImage1.save("1.jpg")


task3()
