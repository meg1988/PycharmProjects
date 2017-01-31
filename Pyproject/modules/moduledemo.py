import math
from controlstructure.methods import add_number
from math import sqrt
from math import fabs


class ModuleDemo(object):

    def builtin_modules(self):
        print(sqrt(100))
        print(fabs(-100))

    def add_number(self):
        a = 10
        b = 20
        add_number(a,b)


m = ModuleDemo()
m.add_number()