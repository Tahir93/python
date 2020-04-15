class Car():
    #attributes are variables in programming
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    #behaviour are functions in programming
    def description_car(self):
        print(f"The make of the car is {self.make}")
        print(f"The model of the car is {self.model}")
        print(f"The year of the car is {self.year}")

    def move(self):
        print(f"The {self.make} is moving with speed")

#creating objects of a calss
car1 = Car("Honda", "Civic", 2019)
car2 = Car("Suzuki", "Cultus", 2020)

car1.description_car()