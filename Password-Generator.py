import string
import random

def generate_password(min_length, numbers=True,special_characters=True):
    letters= string.ascii_letters
    digits= string.digits
    special= string.punctuation

    character= letters
    if numbers:
        character+=digits
    if special_characters:
        character+=special

    meets_criteria= False
    has_number=False
    has_special=False
    pwd=""

    while not meets_criteria or len(pwd)<min_length:
        new_char=random.choice(character)
        pwd+=new_char

        if new_char in digits:
            has_number=True
        if new_char in special:
            has_special=True

        meets_criteria=True
        if numbers:
            meets_criteria=has_number
        if special_characters:
            meets_criteria=meets_criteria and has_special
        
    return pwd
min_length=int(input("Enter min length:"))
pwd=generate_password(min_length)
print(pwd)




