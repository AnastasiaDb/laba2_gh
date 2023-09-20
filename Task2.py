from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.image as mpimg

def task2():
    image = Image.open("color.jpg")
    w, h = image.size
    image.convert("RGB")
    ImageR= Image.new("RGB", (w, h))
    ImageG= Image.new("RGB", (w, h))
    ImageB= Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            r, g, b = image.getpixel((x, y))
            ImageR.putpixel((x,y),(int(r),0,0, 255) )
            ImageG.putpixel((x,y),(0,int(g),0, 255) )
            ImageB.putpixel((x,y),(0,0,int(b), 255) )
    rgbIm = np.concatenate((ImageR,ImageG,ImageB), axis=0)
    plt.figure()

# �������� ������ �����������
    plt.subplot(3, 1, 1)  # 1 ������, 2 �������, ������ ������
    plt.imshow(ImageR)
    plt.axis('off')
# �������� ������ �����������
    plt.subplot(3, 1, 2)  # 1 ������, 2 �������, ������ ������
    plt.imshow(ImageG)
    plt.axis('off')

    plt.subplot(3, 1, 3)  # 1 ������, 2 �������, ������ ������
    plt.imshow(ImageB)
    plt.axis('off')
    plt.show()
    #red_channel = ImageR
    #green_channel = ImageG
    #blue_channel = ImageB
    #hist_red, bins_red = np.histogram(red_channel, bins=256, range=(0, 256))
    #hist_green, bins_green = np.histogram(green_channel, bins=256, range=(0, 256))
    #hist_blue, bins_blue = np.histogram(blue_channel, bins=256, range=(0, 256))
# �������� ����� ������ ��� ����������
    #plt.figure()
# ��������� ����������� ��� ������� ������
    #plt.subplot(1, 3, 1)
    #plt.hist(red_channel.flatten(), bins=256, range=(0, 256), color='red', alpha=0.7)
    #plt.subplot(1, 3, 2)
    #plt.hist(green_channel.flatten(), bins=256, range=(0, 256), color='green', alpha=0.7)
    #plt.subplot(1, 3, 3)
    #plt.hist(blue_channel.flatten(), bins=256, range=(0, 256), color='blue', alpha=0.7)
task2()
