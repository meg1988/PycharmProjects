cars ={"make":"nissan" , "model":"Centra" , "year":2015}
print(cars)

print(cars["year"])

cars["color"]="black"
print(cars)

cars["color"]="white"
print(cars)

print("**"*20)

car_dict ={"bmw" : {"model" : "i550", "year" : 2016} , "nissan" : { "model" : "Centra" , "year" : 2015} }
print(car_dict)

print(car_dict["bmw"]["year"])

print("**"*20)

print(cars.keys())
print(car_dict.keys())

print(cars.values())
print(car_dict.values())

print(cars.items())
cars_copy = cars.copy()

print(cars_copy)
cars_copy.clear()

print(cars_copy)

print(cars.pop("color"))
print(cars)