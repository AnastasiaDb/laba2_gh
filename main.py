import tkinter as tk
from Task1 import task1
from Task2 import task2
from Task3 import task3
from Task3 import hsv_to_rgb
from Task3 import rgb_to_hsv
from PIL import Image as PILImage, ImageTk
from tkinter import Scale, Label, Button
from PIL import Image
import numpy as np


def button1_click():
    task1()


def button2_click():
    task2()


def open_slider_window():
    global slider_h, slider_s, slider_v, updated_photo, updated_image_label, original_photo, slider_window
    slider_window = tk.Toplevel(root)
    slider_window.title("Слайдеры")
    # slider_window.geometry("300x500")

    slider_h = Scale(slider_window, from_=0, to=360, orient="horizontal", label="H")
    slider_s = Scale(slider_window, from_=-50, to=50, orient="horizontal", label="S")
    slider_v = Scale(slider_window, from_=-50, to=50, orient="horizontal", label="V")

    button = Button(slider_window, text="Применить", command=update_image)
    button_back = Button(slider_window, text="Назад", command=show_main)

    button_back.pack(anchor="nw")
    slider_h.pack()
    slider_s.pack()
    slider_v.pack()
    button.pack()

    pil_image = PILImage.open("col.jpg")
    original_photo = ImageTk.PhotoImage(pil_image)

    # отображение исходного изображения
    original_image_label = tk.Label(slider_window, image=original_photo)
    original_image_label.pack()

    # отображение измененного изображения
    updated_photo = ImageTk.PhotoImage(PILImage.new("RGB", (width, height)))  # Пустое изображение
    updated_image_label = tk.Label(slider_window, image=updated_photo)
    updated_image_label.pack()

    root.iconify()


def show_main():
    global slider_window
    slider_window.destroy()
    root.deiconify()


def update_image():
    h = slider_h.get()
    s = slider_s.get()
    v = slider_v.get()

    for x in range(width):
        for y in range(height):
            h_cur, s_cur, v_cur = hsv_arr_original[x][y]
            h_new = h_cur + h
            s_new = s_cur + s
            v_new = v_cur + v

            h_new = max(0, min(360, h_new))
            s_new = max(-50, min(50, s_new))
            v_new = max(-50, min(50, v_new))

            hsv_arr_updated[x][y] = (h_new, s_new, v_new)

    update_display()


def update_display():
    for x in range(width):
        for y in range(height):
            h, s, v = hsv_arr_updated[x][y]
            r, g, b = hsv_to_rgb(h, s, v)
            myImage1.putpixel((x, y), (r, g, b))

    updated_image = PILImage.fromarray(np.uint8(myImage1))
    updated_photo = ImageTk.PhotoImage(updated_image)
    updated_image_label.config(image=updated_photo)
    updated_image_label.image = updated_photo


root = tk.Tk()
root.geometry("400x200")
root.title("Выберите задание:")

# Создаем кнопки
button1 = tk.Button(root, text="Задание 1", width=20, height=2, padx=10, pady=10, command=button1_click)
button2 = tk.Button(root, text="Задание 2", width=20, height=2, padx=10, pady=10, command=button2_click)
button3 = tk.Button(root, text="Задание 3", width=20, height=2, padx=10, pady=10, command=open_slider_window)

# Размещаем кнопки на экране
button1.pack()
button2.pack()
button3.pack()

image = Image.open("col.jpg")
width, height = image.size
myImage1 = Image.new("RGB", (width, height))
hsv_arr_original = np.zeros((width, height, 3), dtype=int)
hsv_arr_updated = np.zeros((width, height, 3), dtype=int)

for x in range(width):
    for y in range(height):
        r, g, b = image.getpixel((x, y))
        h, s, v = rgb_to_hsv(r, g, b)
        hsv_arr_original[x][y] = (h, s, v)

root.mainloop()
