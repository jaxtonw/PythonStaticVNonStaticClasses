# Helper functions
def viewCar(car):
    print(f"\tYour car is {car.color}.")
    print(f"\tYour car is a {car.make}.")
    print(f"\tYour car is a {car.model}.")
    print(f"\tYour car has {car.numWheels} wheels.")
    print(f"\tDoes your car have a spare tire? {car.hasSpare}")

# Demo Static Car
import staticCar

myCar = staticCar.Car
yourCar = staticCar.Car

print("Viewing `myCar`...")
viewCar(myCar)

myCar.numWheels -= 1
print("Viewing `myCar` after hitting the pothole...")
viewCar(myCar)

myCar.hasSpare = False
myCar.numWheels += 1

print("Viewing `myCar` after fixing the tire...")
viewCar(myCar)

print("Viewing `yourCar`...")
viewCar(yourCar)

print("Oh no! Looks like we've been driving the same car this whole time...")

print("How do we fix this? Let's make it so we all get our own cars!")
print("\t(Imagine Oprah Winfrey saying \"You get a car!\" here)")

# Demo Non-Static Car
import nonstaticCar

myCar = nonstaticCar.Car()
yourCar = nonstaticCar.Car()

print("Viewing `myCar`...")
viewCar(myCar)

myCar.numWheels -= 1
print("Viewing `myCar` after hitting the pothole...")
viewCar(myCar)

myCar.hasSpare = False
myCar.numWheels += 1

print("Viewing `myCar` after fixing the tire...")
viewCar(myCar)

print("Viewing `yourCar`...")
viewCar(yourCar)
