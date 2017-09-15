#Ilya Chaban
import random

class Color(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, value):
        self._r = value

    @property
    def g(self):
        return self._g

    @g.setter
    def g(self, value):
        self._g= value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def color(self):
        return (self.r, self.g, self.b)

    def get_str(self):
        return "#%02X%02X%02X" % self.color

    def __str__(self):
        return self.get_str()

    def to_dict(self):
        new_dict = {}
        new_dict["r"] = self.r
        new_dict["g"] = self.g
        new_dict["b"] = self.b
        return new_dict

    def from_dict(self, dict_source):
        self.r = dict_source["r"]
        self.g = dict_source["g"]
        self.b = dict_source["b"]


class Coeff(object):
    def __init__(self):
        self._c = random.randint(-150, 150) / 100
        self._f = random.randint(-150, 150) / 100
        self._color = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.random()
        while not self.good_coeffs():
            self.random()

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, value):
        self._d = value

    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, value):
        self._e = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    def random(self):
        self._a = random.randint(-150, 150) / 100
        self._b = random.randint(-150, 150) / 100
        self._d = random.randint(-150, 150) / 100
        self._e = random.randint(-150, 150) / 100

    def good_coeffs(self):
        sum1 = self.a ** 2 + self.d ** 2
        sum2 = self.b ** 2 + self.e ** 2
        condition1 =  sum1 < 1
        condition2 =  sum2 < 1
        condition3 = sum1 + sum2 < 1 + (self.a * self.e - self.b * self.d) ** 2
        if (not condition1) or (not condition2) or (not condition3):
            return False
        return True

    def to_dict(self):
        new_dict = {}
        new_dict["a"] = self.a
        new_dict["b"] = self.b
        new_dict["d"] = self.d
        new_dict["e"] = self.e
        new_dict["c"] = self.c
        new_dict["f"] = self.f
        new_dict["color"] = self.color.to_dict()
        return new_dict

    def from_dict(self, dict_source):
        self.a = dict_source["a"]
        self.a = dict_source["b"]
        self.a = dict_source["d"]
        self.a = dict_source["e"]
        self.a = dict_source["c"]
        self.a = dict_source["f"]
        self.color.from_dict(dict_source["color"])



class PixelInfo():
    def __init__(self):
        self.counter = 0
        self.color = Color(0, 0, 0)
        self.normal = 0.

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, value):
        self._counter = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def normal(self):
        return self._normal

    @normal.setter
    def normal(self, value):
        self._normal = value



