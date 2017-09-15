#Ilya Chaban
import json
import random
import math
from helpclasses import Coeff, PixelInfo
from predifinedfunctionsset import pfs
from tkinter import Tk, Button, Canvas, PhotoImage
import numpy as np


def create_and_write_into_file(filename):
    coeff = np.array([Coeff() for i in range(10)])
    data = json.dumps([c.to_dict() for c in coeff])
    with open("coeffs.json", "w") as f:
        f.write(data)
    return coeff


def read_from_file(filename):
    with open("coeffs.json") as f:
        data = f.read()
    coeff = []
    for dc in json.loads(data):
        co = Coeff()
        co.from_dict(dc)
        coeff.append(co)
    coeff = np.array(coeff)
    return coeff


def correction(res_x, res_y):
    max = 0.0
    gamma = 2.2
    x = 0
    while x < res_x:
        y = 0
        while y < res_y:
            if pixels[x][y].counter != 0:
                pixels[x][y].normal =  math.log10(pixels[x][y].counter)
                if pixels[x][y].normal > max:
                    max = pixels[x][y].normal
            y += 1
        x += 1
    x = 0
    while x < res_x:
        y = 0
        while y < res_y:
            pixels[x][y].normal /= max
            pixels[x][y].color.r = int(pixels[x][y].color.r * pixels[x][y].normal ** (1 / gamma))
            pixels[x][y].color.g = int(pixels[x][y].color.g * pixels[x][y].normal ** (1 / gamma))
            pixels[x][y].color.b = int(pixels[x][y].color.b * pixels[x][y].normal ** (1 / gamma))
            y += 1
        x += 1


def render():
    if input("Read from file?(y/n) Otherwise, will be created and written in file: ") == "y":
        coeff = read_from_file("coeffs.json")
    else:
        coeff = create_and_write_into_file("coeffs.json")
    res_x = 800
    res_y = 600
    x_min = -0.40
    x_max = 0.4
    y_min = -0.3
    y_max = 0.3
    choices = [i for i in pfs.keys()]
    for p_count in range(10000):
        new_x = random.randint(-150, 150) / 1000
        new_y = random.randint(-100, 100)  / 1000
        for step in range(-20, 1000):

            choice = random.choice(choices)
            rand = random.randint(0, 9)
            new_x = coeff[rand].a * new_x + coeff[rand].b * new_y + coeff[rand].c;
            new_y = coeff[rand].d * new_x + coeff[rand].e * new_y + coeff[rand].f;
            (new_x, new_y) = pfs[choice](new_x, new_y)

            if step >= 0 and new_x > x_min and new_x < x_max and new_y > y_min and new_y < y_max:
                x = int(res_x - ((x_max - new_x) / (x_max - x_min) * res_x))
                y = int(res_y - ((y_max - new_y) / (y_max - y_min) * res_y))
                if(x < res_x and y < res_y):
                    pixel_info = pixels[x][y]
                    if pixel_info.counter == 0:
                        pixel_info.color.r = coeff[rand].color.r
                        pixel_info.color.g = coeff[rand].color.g
                        pixel_info.color.b = coeff[rand].color.b
                    else:
                        pixel_info.color.r = (pixel_info.color.r + coeff[rand].color.r) // 2
                        pixel_info.color.g = (pixel_info.color.g + coeff[rand].color.g) // 2
                        pixel_info.color.b = (pixel_info.color.b + coeff[rand].color.b) // 2
                    pixel_info.counter += 1
    correction(res_x, res_y)
    x = 0
    while x < res_x:
        y = 0
        while y < res_y:
            if pixels[x][y].counter != 0:
                image.put(str(pixels[x][y].color), to=[x, y])
            y += 1
        x += 1

pixels = np.array([np.array([PixelInfo() for i in range(600)]) for i in range(800)])
root = Tk()
canvas = Canvas(root, width=800, height=600, background="black")
image = PhotoImage(width=800, height=600)
canvas.create_image(0, 0, image=image, anchor="nw")
canvas.pack()
button = Button(root, text="Draw", command=render)
button.pack()
root.mainloop()

