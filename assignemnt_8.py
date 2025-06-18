#question1
def accept_numbers(*args):
    return sum(args)
a= accept_numbers(1,2)
print(a)

#question2
def keyword_arguments(**kwargs):
    return kwargs
a = keyword_arguments(name = "alice",age=30)
print(a)



#question3
# while True:
#     a = input("enter:")
#     if a == "exit":
#         break

# print(a)

#question4
a = 1
while True:
    print(a)
    if a == 5:
        break
    a += 1

#question5
a = -1

while True:
    a = int(input("enter a number:"))
    if a < 0:
        break

#question6
def random_function(*args):


#question7

 a = []

while True:
    name = input("enter a name:")
    if name == "":
        break
names.append(name)
print("names entered:",names)

#question8
def products(**kwargs):
    prices = list(kwargs.values())
    total = 0.0
    index = 0

while index < len(prices):
    total += prices[index]
    index += 1

    return total

print(products(pen=10,pencil=5))

#question9
count = 10
while count >= 1:
    if count == 5:
        count -= 1
        continue
    print(count)
    count -= 1

#question10
def user_age():
    while True:
        age = input("enter you age:")
        if not age.isdigit():
            print("invalid")
            continue
        a = int(age)
        if age <= 0:
            print("age must be greater than 0")
            continue
        return a
    







    


