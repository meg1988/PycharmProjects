
class Car(object):

    def __init__(self):
        print("you just created an instance of car")

    def drive(self):
        print("car started")

    def stop(self):
        print("car stop")

class Bmw(Car):

    def __init__(self):
        super(Bmw, self).__init__()
        print("this is bmw")

    def drive(self):
        super(Bmw, self).drive()
        print("you are driving a bmw")

    def headup_display(self):
        print("this is unique feature")


c1=Car()
c1.drive()
c1.stop()


c2=Bmw()
c2.drive()
c2.stop()
c2.headup_display()
