#PYTHON- OBJECT ORIENTED PROGRAMMING(OOP):

#question1

class devices:

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def turn_on(self):
        print(f"turning on {self.brand} ")

    def reset(self):
        print(f"Resetting {self.brand} ")


class PC:

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def turn_on(self):
        print(f"turning on {self.brand} ")

    def reset(self):
        print(f"Resetting {self.brand} ")
pc = PC('dell','white')

class PHONE:

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def turn_on(self):
        print(f"turning on {self.brand} ")

    def reset(self):
        print(f"Resetting {self.brand} ")
phone = PHONE('apple','black')


class CAR:

    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

    def turn_on(self):
        print(f"turning on {self.brand} ")

    def reset(self):
        print(f"Resetting {self.brand} ")
car = CAR('audi','blue')
pc.brand = 'lenovo'
car.color = 'brown'


print(pc.brand)
print(car.color)


#question2


        

