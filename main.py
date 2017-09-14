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
    res_x = 700
    res_y = 700
    x_min = 0
    x_max = 0.700
    y_min = 0.
    y_max = 0.500
    choices = [i for i in pfs.keys()]
    coeff = [Coeff() for i in range(10)]
    for p_count in range(1000):
        new_x = random.randint(1, 700) / 700
        new_y = random.randint(1, 700)  / 500
        for step in range(-20, 1000):

            choice = random.choice(choices)
            rand = random.randint(0, 9)
            new_x = coeff[rand].a * new_x + coeff[rand].b * new_y + coeff[rand].c;
            new_y = coeff[rand].d * new_x + coeff[rand].e * new_y + coeff[rand].f;
            (new_x, new_y) = pfs[choice](new_x, new_y)

            if step>=0 and new_x > x_min and new_x < x_max and new_y > y_min and new_y < y_max:
                x = res_x - ((x_max - new_x) / (x_max - x_min) * res_x);
                y = res_y - ((y_max - new_y) / (y_max - y_min) * res_y);
                if(x < res_x and y < res_y):
                    image.put(str(coeff[rand].color), to=[int(x), int(y)])



root = Tk()
canvas = Canvas(root, width=700, height=500, background="black")
image = PhotoImage(width=700, height=500)
canvas.create_image(0, 0, image=image, anchor="nw")
canvas.pack()
button = Button(root, text="Draw", command=render)
button.pack()
root.mainloop()

