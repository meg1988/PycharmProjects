
car = {"make":"Nissan" , "model":"centra" , "year":2015}
print(car)

try:
    print(car["color"])
except:
    print("this is an exception")
finally:
    print("it will always be printed")