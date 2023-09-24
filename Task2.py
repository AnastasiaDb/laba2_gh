from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.image as mpimg

def task2():
    arr_r = [0] * 256
    arr_g = [0] * 256
    arr_b = [0] * 256
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
            arr_r[int(r)] += 1;
            arr_g[int(g)] += 1;
            arr_b[int(b)] += 1;

    plt.imshow(image);
    plt.axis('off')
    plt.show();


    plt.subplot(2, 3, 1)
    plt.imshow(ImageR)
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(ImageG)
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.imshow(ImageB)
    plt.axis('off')
    #plt.show()

    plt.subplot(2, 3, 4)
    plt.plot(arr_r, color='red')
    plt.subplot(2, 3, 5)
    plt.plot(arr_g, color='green')
    plt.subplot(2, 3, 6)
    plt.plot(arr_b, color='blue')

    plt.show();

#task2()
