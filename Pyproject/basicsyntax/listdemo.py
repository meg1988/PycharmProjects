cars = ["bmw","honda","nissan",""]
print(cars)

a=[]
print(a)

print(cars[0])

cars[3]="benz"
print(cars)

cars.append("cooper")
print(cars)

cars.insert(1,"Jeep")
print(cars)

print(cars.index("cooper"))

print(cars.pop())
print(cars.pop(0))
print(cars.remove("benz"))
print(cars)

print(cars[0:2])
print(cars[1:])
print(cars[::-1])

cars.sort()
print(cars)