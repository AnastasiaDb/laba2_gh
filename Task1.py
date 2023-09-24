import math
from time import sleep

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


def task1():
    arr_im1 = [0] * 256
    arr_im2 = [0] * 256
    max_diff = -1
    min_diff = 256
    image = Image.open("color.jpg")
    w, h = image.size
    myImage1 = Image.new("RGB", (w, h))
    myImage2 = Image.new("RGB", (w, h))
    diffImage = Image.new("RGB", (w, h))
    matrix = np.zeros((w, h), dtype=int)  # Создание двумерного массива с нулевыми значениями

    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))

            val1 = int(0.299 * r + 0.587 * g + 0.114 * b)
            val2 = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            myImage1.putpixel((x, y), (val1,val1,val1))
            myImage2.putpixel((x, y), (val2,val2,val2))
            arr_im1[val1] += 1
            arr_im2[val2] += 1
            # diffImage.putpixel((x, y), abs(val1-val2))
            diff = val1 - val2
            matrix[x][y] = diff
            if diff > max_diff:
                max_diff = diff
            if diff < min_diff:
                min_diff = diff
    #print (max_diff,'  ',min_diff)
    for x in range(w):
        for y in range(h):
            pix_diff = int(matrix[x][y] * 255 / (max_diff - min_diff))
            diffImage.putpixel((x, y), (pix_diff,pix_diff,pix_diff))
    #myImage1.show()  # save("1.jpg")
    # sleep(3)
    #myImage2.show()  # save("2.jpg")
    # sleep(3)
    #diffImage.show()  # save("3.jpg")

  #   rgbIm = np.concatenate((myImage1, myImage2, diffImage), axis=0)
  #   plt.figure()
  #   plt.imshow(rgbIm)
  #   plt.axis('off')
  #   plt.show()
  #
  #   plt.plot(arr_im1, color='black')
  # #  plt.show()
  #   plt.plot(arr_im2, color='blue')
  #   plt.show()

    plt.subplot(3, 2, 1)
    plt.imshow(myImage1)
    plt.axis('off')

    # Второй график - изображение myImage2
    plt.subplot(3, 2, 2)
    plt.imshow(myImage2)
    plt.axis('off')

    # Третий график - изображение diffImage
    plt.subplot(2, 2, 3)
    plt.imshow(diffImage)
    plt.axis('off')

    # Четвертый график - гистограммы
    plt.subplot(2, 2, 4)
    plt.plot(arr_im1, color='black', label='Type 1')
    plt.plot(arr_im2, color='blue', label='Type 2')
    plt.legend()
    plt.grid()

    plt.show()
task1()
