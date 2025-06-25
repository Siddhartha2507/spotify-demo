#question1

class TV:

    def __init__(self,brand):
        self.brand = brand
        
    
    def turn_on(self):
        print(f"{self.brand} tv is turning on")

    def turn_off(self):
        print(f"{self.brand} tv is turning off")

class REMOTE:

    def __init__(self):
        self.tv = tv

    def turn_on(self):
        print(f"{self.tv} is turning on")

    def turn_off(self):
        print(f"{self.tv} is turning off")    
        
    
tv = TV("Samsung") 
remote = REMOTE()
remote.tv.turn_on()
remote.tv.turn_off()

#question2

class Car:

    def __init__(self,brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} car is starting")


class Engine:

    def __init__(self):
        self.car = car
    
    def start_engine(self):
        print(f"{self.car} is starting")

car = Car("audi")
engine = Engine()
engine.car.start_engine()


#question3
class Room:

    def __init__(self,room_no):
        self.room_no = room_no

    def switch_on(self):
        print(f"{self.room_no} has light")

class Light:

    def __init__(self):
        self.room = room

    def switch_on(self):
        print(f"{self.room} has light..")

room = Room(69)
light = Light()
light.room.switch_on()


#question4
class Laptop:

    def __init__(self,brand):
        self.brand = brand

    def check_charge(self):
        print(f"checking charging of {self.brand}  ")


class Battery:

    def __init__(self):
        self.laptop = laptop
        
    def check_charge(self):
        print(f"checkinf charging of {self.laptop}")  

laptop = Laptop("dell")
battery = Battery()
battery.laptop.check_charge()  


#question5
class Mobile:

    def __init__(self,brand):
        self.brand = brand

    def take_picture(self):
        print(f"taking picture from {self.brand} mobile")

class Camera:

    def __init__(self):
        self.mobile = mobile 

    def take_picture(self):
        print(f"taking picture from {self.mobile} ")

mobile = Mobile("iphone")
camera = Camera()
camera.mobile.take_picture()

