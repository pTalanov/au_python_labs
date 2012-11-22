class Car:

    def who(self):
        print("I'm a car")

class SuperCar(Car):

    def who(self):
        print("I'm a better car")

class SportCar(Car):

    def who(self):
        print("I attract chicks")


cars = (Car(), SuperCar(), SportCar())

for car in cars:
    car.who()