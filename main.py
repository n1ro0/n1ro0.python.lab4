#Ilya Chaban
import json
import random
from helpclasses import Color, Coeff
from predifinedfunctionsset import pfs
from tkinter import Tk, Button, Canvas, PhotoImage





"""data = {"name": "Ilya",
        "surname": "Chaban",
        "age": 23}
jsom_pack = json.dumps(data)

with open("file.json", "w") as f:
    f.write(jsom_pack)

new_dict = {}
with open("file.json") as f:
    text = f.read()
    new_dict = json.loads(text)

print(new_dict["surname"])"""

def render():
    res_x = 500
    res_y = 500
    x_min = -1.777
    x_max = 1.777
    y_min = -1.
    y_max = 1.
    choices = [i for i in pfs.keys()]
    coeff = Coeff()
    for p_count in range(10000):
        new_x = random.randint(-1777, 1777) / 1000
        new_y = random.randint(-1000, 1000)  / 1000
        for step in range(-20, 4):

            choice = random.choice(choices)

            new_x, new_y = pfs["sinusoidal"](new_x, new_y)
            new_x = coeff.a * new_x + coeff.b * new_y + coeff.c;
            new_y = coeff.d * new_x + coeff.e * new_y + coeff.f;
            if step>=0 and new_x > x_min and new_x < x_max and new_y > y_min and new_y < y_max:
                x = res_x - ((x_max - new_x) / (x_max - x_min) * res_x);
                y = res_y - ((y_max - new_y) / (y_max - y_min) * res_y);
                if(x < res_x and y < res_y):
                    image.put(str(coeff.color), to=[int(x), int(y)])



root = Tk()
canvas = Canvas(root, width=500, height=500, background="black")
image = PhotoImage(width=500, height=500)
canvas.create_image(0, 0, image=image, anchor="nw")
canvas.pack()
button = Button(root, text="Draw", command=render)
button.pack()
root.mainloop()

