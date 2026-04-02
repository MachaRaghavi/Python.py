#Arrays
cars=["Ford","Telsa","BMW"]
print(cars)
x=cars[0]
print(x)

#Adding element
cars.append("Honda")
print(cars)

# Modify the element
cars[0]="Benz"
print(cars)

#length of an array
print(len(cars))

# Removing element
cars.pop(1)
print(cars)

cars.remove("Benz")
print(cars)
