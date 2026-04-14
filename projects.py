# Topic - 1 : 
#Project: Personal Info Card (Console)
#👉 https://github.com/Tech-With-Tim/Python-Beginner-Projects
#Look for the "Personal Details" or "Bio Card" type project. The idea is simple — store your personal details in variables and print a formatted card

name = "Naina Yadav"
age = 25
city = "Mumbai"
profession = "Student"
is_employed = False

print("===== MY INFO CARD =====")
print(f"Name       : {name}")
print(f"Age        : {age}")
print(f"City       : {city}")
print(f"Profession : {profession}")
print(f"Employed   : {is_employed}")
print("========================")


#  Topic 2 :
# Project: Simple Calculator
# Build a calculator that takes two numbers and performs all arithmetic operations and displays results neatly.

a = float(input("Enter First Number : "))
b = float(input("Enter Secound Number : "))

print(f"Addition       :{a+b}")
print(f"Subtraction    :{a-b}")
print(f"multiplication :{a*b}")
print(f"Division       :{a/b}")
print(f"floor Division :{a//b}")
print(f"Modulus        :{a%b}")
print(f"Power          :{a**b}")


# topic 3 :
# number gussing game

import random

secrect = random.randint(1,100)
guess = int(input("Enter a Number between 1 to 100 : " ))

if guess > secrect :
    print("too high guess")
elif guess < secrect:
    print("too low guess ")
else:
    print("correct guess")

    

    