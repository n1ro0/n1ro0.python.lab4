#Ilya Chaban
import math


def linear(x, y):
    return (x, y)


def sinusoidal(x, y):
    return (math.sin(x), math.sin(y))


def spherical(x, y):
    divider = x ** 2 + y ** 2
    return (x / divider, y / divider)


def polar(x, y):
    return (math.sin(math.atan(y / x) / math.pi), math.sqrt(x ** 2 + y ** 2) - 1)


def heart(x, y):
    xy_2 = math.sqrt(x ** 2 + y ** 2)
    sm = xy_2 * math.atan(y / x)
    new_x = xy_2 * math.sin(sm)
    new_y = xy_2 * math.cos(sm)
    return (new_x, new_y)


def disk(x, y):
    xy_2 = math.pi * math.sqrt(x ** 2 + y ** 2)
    fm = 1 / math.pi * math.atan(y / x)
    new_x = fm * math.sin(xy_2)
    new_y = fm * math.cos(xy_2)
    return (new_x, new_y)


def register():
    pfs["linear"] = linear
    pfs["sinusoidal"] = sinusoidal
    pfs["spherical"] = spherical
    pfs["polar"] = polar
    pfs["heart"] = heart
    pfs["disk"] = disk


pfs = {}
register()