# #C LEVEL 1 & LEVEL 2 PROBLEMS
# #question1
# #a = [1,2]
# #print(max(a))
# #def max_of_two(a,b):
# #     if a > b:
# #         return a
# #     else:
# #         return b


# # #question
# # print(bool(6))

# # x = 'python'
# # print(x[0:3]+ x[-1:-4:-1])

# #question
# for i in range(1,6):
#     print('x' * i)

# #question
# n = 5
# for i in range(1,n+1):
#     print(" " * (n - i)+ "*" * (2*i - 1))
# for i in range(n-1,0,-1):
#     print(" " * (n - i)+ "*" * (2*i - 1))

# #question1
# def max_of_two(a,b):
#     if a > b:
#         return a
#     else:
#         return b

# #question2
# def max_of_three(a,b,c):
#     if a > b:
#         return a
#     elif b > c:
#         return b
#     elif c > a:
#         return c
    

# #question3
# def if_pos_not(num):
#     if num > 0:
#         return "positive"
#     if num < 0:
#         return "negative"
    
# #question 4
# def if_even_odd(num):
#     if num // 2 == 0:
#         return "even"
#     else:
#         return "odd"
# if_even_odd()
# #question5
# def if_leap_year(num):
#     if num == 365:
#         return "leap year"
#     else:
#         return " not a leap year"

# if_leap_year()
# #question6
# def is_alpha(character):
#     if character.isalpha():
#         return "alphabet"
#     else:
#         return "not an alphabet"
# is_alpha() 

# #question7
# text = input("enter an alphabet")
# def if_vowel_consonant():
#     if text == 'aeiou':
#         return "vowel"
#     else:
#         return "consonant"
# if_vowel_consonant()

# #question8
# text =  input("enter a character")
# def alpha_digi_spe():
#     if text.isalpha():
#         return "alphabet"
#     elif text.isdigit():
#         return "digit"
#     else:
#         return "special character"
# alpha_digi_spe()
    
# #question9
# character = input()
# def lower_upper():
#     if character.isupper():
#         return "uppercase alphabet"
#     else:
#         return "lowercase alphabet"
# lower_upper()
    
# #question10
# a = input("enter week number(1-7)")
# def week_day(num):
#     if num == 1:
#         return "monday"
#     elif num == 2:
#         return "tuesday"
#     elif num == 3:
#         return "wednesday"
#     elif num  == 4:
#         return "thursday"
#     elif num == 5:
#         return "friday"
#     elif num == 6:
#         return "saturday"
#     elif num == 7:
#         return "sunday"
#     else:
#         return "invalid week no"
# print(week_day(a))

# #question11
# b = input("enter month number(1-12)")
# def month_number(month):
#     if month == 2:
#         return "28 or 29 days feb"
#     elif month in [1,3,5,7,8,10,12]:
#         return "31days"
#     elif month in [4,6,9,11]:
#         return "30days"
#     else:
#         return "invalid month number"
# print(month_number(b))

# #question12
# def count_notes(amount):
#     notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
#     note_count = {}

#     for note in notes:
#         count = amount // note
#         if count > 0:
#             note_count[note] = count
#             amount = amount % note

#     return note_count

# print("Note breakdown:")
# for note, count in notes_used.items():
#     print(f"₹{note}: {count} notes")

#question13
A = int(input("enter angle A"))
B = int(input("enter angle B"))
C = int(input("enter angle C"))
def check():
    if A+B+C == 180:
        print("Is a Triangle")
    else:
        print("Not  a triangle")

check()






    



