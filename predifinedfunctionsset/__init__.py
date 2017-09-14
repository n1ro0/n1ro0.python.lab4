#Ilya Chaban
import math


def linear(x, y):
    return (x, y)


def sinusoidal(x, y):
    return (math.sin(x), math.sin(y))


def spherical(x, y):
    divider = x ** 2 + y **2
    return (x/divider, y/divider)


def polar(x, y):
    return (math.sin(math.atan(y/x)/math.pi), math.sqrt(x**2+y**2)-1)


def heart(x, y):
    pass


def disk(x, y):
    pass


def register():
    pfs["linear"] = linear
    pfs["sinusoidal"] = sinusoidal
    pfs["spherical"] = spherical
    pfs["polar"] = polar


pfs = {}
register()