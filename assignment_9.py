#question1
for numbers in range(6):
    print(numbers)

#question2
for numbers in range(10,20,2):
 
 print(numbers)

#question3
# user = input("enter 3 names:")

# a = list(user)

# for use in user:
#    print(f"i like {use}") 

#question4
a = [2,3,4]

for i in a:
   print(i**2)

#question5
a = [{
   "name" : "alice",
   "age" : 35
},
{
   "name" : "bob",
   "age" : 34
}]
for i in a:
   print(f"{i["name"]}, {i["age"]}")

#question6
fruits = [["apple","banana"],["grape","mango"]]
for fruit in fruits:
   print(fruits)

#question7
message = input("enter a message:")
for character in message:
   print(character)

#question8
for numbers in range(5,0,-1):
   print(numbers)

#question10
a = [("pen",10),("pencil",5)]
for product,price in a:
   print(f"product: {product},price: {price}")

#question9

subjects = [{
   "subjects" : input("enter subjects:"),
   "marks" : input("enter marks:")
}
 for _ in range(3)]
for subject in subjects:
   print(f"{subject["subjects"]}: {subject["marks"]}")
   


