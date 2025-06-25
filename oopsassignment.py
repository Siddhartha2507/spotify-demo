#PYTHON- OBJECT ORIENTED PROGRAMMING(OOP):

#question1
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
class CAR:

    def __init__(self,model,speed,fuel_type):
        self.model = model
        self.speed = speed
        self.fuel_type = fuel_type

    def accerlate(self):
        print(f"accerlating {self.model} car ")

    def stop(self):
        print(f"stopping {self.model} car ")
    
    def honk(self):
        print(f"honking {self.model} car")

class BIKE:

    def __init__(self,model,speed,fuel_type):
        self.model = model
        self.speed = speed
        self.fuel_type = fuel_type

    def accerlate(self):
        print(f"accerlating {self.model} bike ")

    def stop(self):
        print(f"stopping {self.model} bike ")
    
    def honk(self):
        print(f"honking {self.model} bike")

class TRUCK:

    def __init__(self,model,speed,fuel_type):
        self.model = model
        self.speed = speed
        self.fuel_type = fuel_type

    def accerlate(self):
        print(f"accerlating {self.model} truck ")

    def stop(self):
        print(f"stopping {self.model} truck ")
    
    def honk(self):
        print(f"honking {self.model} truck")

car = CAR('audi',90,'petrol')
bike = BIKE('royalenfield',100,'petrol')
truck = TRUCK('mahindra',60,'diesel')

print(car)
print(truck)
print(bike)

print(car.model)
print(truck.fuel_type)
print(bike.speed)


#question3
class STUDENT:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def read(self):
        print(f"{self.name} is reading ")

    def write(self):
        print(f" {self.name} is writing ")


class TEACHER:

    def __init__(self,name,subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching ")

    def explain(self):
        print(f" {self.name} is explaining ")

class CLASSROOM:

    def __init__(self,room_number,board):
        self.room_number = room_number
        self.board = board

    def room(self):
        print(f"{self.room_number} is in ground floor")

    def board(self):
        print(f" {self.board} has white board ")

student = STUDENT('akshar',15)
teacher = TEACHER('kamlesh','chemistry')
classroom = CLASSROOM(401,"white")

teacher.teach()
student.read()


#question4
class BOOK:

    def __init__(self,title,author):
        self.title = title
        self.author = author

    def name(self):
        print(f" name of the book is {self.title} ")

    def author_name(self):
        print(f" name of the author is {self.author} ")

class LIBRANIAN:

    def __init__(self,title,manager):
        self.title = title
        self.manager = manager

    def issue(self):
        print(f"the libranian, {self.manager} manages the whole library ")

    def read(self):
        print(f"the libranian is reading the name of the book, {self.title} ")

class MEMBER:

    def __init__(self,title,member):
        self.title = title
        self.member = member

    def new(self):
        print(f"the new member knows about {self.title} ")

    def Return(self):
        print(f" {self.member} has returned the book named , {self.title} ")   

book = BOOK('jersey', 'gautam tinnanuri')    
libranian = LIBRANIAN('devara','siddharth')
member = MEMBER('bahubali','rithvik')


libranian.issue()
member.Return()

#question4
class PRODUCT:

    def __init__(self,brand,price,color,product_id):
        self.brand = brand
        self.price = price
        self.color = color
        self.product_id = product_id



    def view_details(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Description: {self.description}")


    def function(self):
        print(f" {self.brand} is fucntioning well and its price is {self.price} ")

class CART:

    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color
        self.products = product

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} added to cart.")

    def mobile(self):
        print(f"{self.brand} mobile is added to the cart ")

    def identification(self):
        print(f" the item added to the cart has {self.color} ")



class USER:

    def __init__(self,name,address,total_bill):
        self.name = name
        self.total_bill = total_bill
        self.address = address
        self.cart = cart


    def total(self):
        print(f"The total of Mr/Mrs {self.name} s cart is {self.total_bill} ")

    def location(self):
        print(f" Address of Mr/Mrs {self.name} is {self.address} ")

    def add_to_cart(self, product):
        self.cart.add_product(product)

product = PRODUCT('crocs',1599,'black')
cart  = CART('apple',80000,'white')
user = USER('siddhartha', '12-1-169/p8 nagole', 19999)

product.view_details()





a = ["cat","dog","donkey","monkey"]
for animals in a:
    a.append([0],"do")
    print(a)


        

