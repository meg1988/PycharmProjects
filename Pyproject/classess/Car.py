
class Car(object):

    wheels = 4

    def __init__(self, make, model="Centra"):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car " + self.make)
        print("Model of the car " + self.model)

c1 = Car("Nissan")

c2 = Car('bmw', 'i550')

c1.info()
c2.info()
print(Car.wheels)




