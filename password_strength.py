#Password criteria
#one uppercase,one loweer case, one special character, one number.

# a = ["A","s","@",6]

# password = input("enter a password:")

# for sentence in password:
#     if sentence in a:
#         print("strong password")
#     else:
#         print("weak password")

# print("your password is :" , {password})    

def validate_password(password):
    is_number = False
    is_uppercase = False
    is_lowercase = False

    for character in password:
        if character.isupper():
            is_uppercase = True
        elif character.islower():
            is_lowercase = True
        elif character.isdigit():
            is_number = True


    return is_uppercase and is_lowercase and is_number
password = input("enter your password:")

                        