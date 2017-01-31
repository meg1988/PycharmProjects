class Fruit(object):

    def __init__(self):
        print("this is a fruit")

    def nutrition(self):
        print("it is very nutritious")

    def fruit_shape(self):
        print ("shape of the fruit is round")

class Apple(Fruit):

    def __init__(self):
        super(Apple, self).__init__()
        print("this fruit is apple")

    def nutrition(self):
        super(Apple, self).nutrition()
        print("It is rich in antioxidants")

    def color(self):
        print("it is red in color")

f = Fruit()
f.nutrition()
f.fruit_shape()

a = Apple()
a.nutrition()
a.color()
a.fruit_shape()

