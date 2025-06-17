#question1 
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("akshar")

#question2
def check_temperature(temp):
 result = None
 if temp > 99:
    return "fever"
 else:
    return "normal"
a = check_temperature(120)
print(a) 

#question3
def get_last_fruits(a):
   a = ["mango","orange","watermelon"]
   return a[-1]
b = get_last_fruits(a)
print(b)

#question4
def get_price_tag(price):
   result = None
   if price > 1000:
      return "expensive"
   else:
      return "affordable"
   
a = get_price_tag(999)
print(a)

#question5
def format_user_info(name,age):
   print(f"Name: {name},Age: {age}")

a = format_user_info("akshar", 45)
print(a)

#question6
#def uppercase_if_string(a):
   

#question7
def safe_divide(num,den):
   result = None
   if den != 0 :
      return result
   else:
      return "cannot divide"
   
a = safe_divide(47,38)
print(a)

#question8
def check_login(details):
   if details.get('password'):
      return "login succesful"
   else:
      return "login unsuccesful"
   
user_information = {
   "username" : "akshar_123",
   "password" : "damn123"
}
print(check_login(user_information))

#question9
def get_full_name(first,last):
   return f"{first} {last}".title()
print(get_full_name(first="siddu",last="daram"))

#question10
def get_discounted_price(price,is_member):
   if is_member :
      return price * 0.9
   else:
      return price
   
print(get_discounted_price(100,True))




   
   

 
 

