#Topic 1: Variables & Data Types
#What is a Variable?
#A variable is a named container that stores a value in memory. In Python, you don't need to declare the type — Python figures it out automatically 
name = "Arjun"
age = 25
price = 99.99
is_student = True

#Core Data Types
#1. int — whole numbers
x = 10
y = -5
big = 1_000_000  # underscores for readability

#2.float — decimal numbers
pi = 3.14159
temperature = -2.5

#3.str — text (always in quotes)
first_name = "Rahul"
city = 'Mumbai'
message = "I live in Mumbai"

#4.bool — True or False only
is_logged_in = True
has_paid = False

#5. NoneType — represents absence of value
result = None

#Checking the Type
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>

#Type Casting (converting types)
x = "100"
y = int(x)       # str → int → 100
z = float(x)     # str → float → 100.0

a = 3.9
b = int(a)       # float → int → 3 (truncates, doesn't round)

c = 42
d = str(c)       # int → str → "42"

e = 1
f = bool(e)      # 1 → True, 0 → False

#Naming Rules for Variables
# VALID
user_name = "Raj"
age2 = 30
_private = "hidden"
firstName = "Priya"   # camelCase (works but not Pythonic)
first_name = "Priya"  # snake_case (recommended in Python)

# INVALID
#2name = "error"       # cannot start with number
my-var = "error"      # hyphens not allowed
class = "error"       # reserved keyword

#Multiple Assignment
a = b = c = 0          # all three = 0

x, y, z = 10, 20, 30  # unpacking

# swap without temp variable
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

#Practice Exercises 

#Create variables for your name, age, city, and whether you are a student. Print all of them.
name = "Naina yadav"
Age = 25
city = "Mumbai"
is_student = True

#Create a variable with value "123" (string) and convert it to int and float.
value = "123"
x = int(value)      #str → int → 123
y = float(value)    # str → float → 123.0
#Try dividing an int by another int and check the data type of the result.
x = 10
y = 5
z = x/y    
print(z)          #2.0
print(type(z))    #class "float"

#What is the result of bool(0), bool(""), bool(None), bool([]) — guess first, then run
bool(0)     #false
bool("")    #false
bool(None)  #false
bool([])    #false


#Phase 1 — Topic 2: Operators
#Operators are symbols that perform operations on variables and values. Python has 7 types of operators.
#1. Arithmetic Operators
#Used for mathematical calculation

a = 10
b = 3

print(a + b)   # 13  → Addition
print(a - b)   # 7   → Subtraction
print(a * b)   # 30  → Multiplication
print(a / b)   # 3.3333 → Division (always returns float)
print(a // b)  # 3   → Floor Division (removes decimal)
print(a % b)   # 1   → Modulus (remainder)
print(a ** b)  # 1000 → Exponentiation (10 to the power 3)

#Tip — Modulus real use cases:
# Check if number is even or odd
number = 17
print(number % 2 == 0)  # False → odd

# Check if divisible by 5
print(25 % 5 == 0)  # True

#2. Comparison Operators
#Always return True or False
a = 10
b = 20

print(a == b)   # False → equal to
print(a != b)   # True  → not equal to
print(a > b)    # False → greater than
print(a < b)    # True  → less than
print(a >= b)   # False → greater than or equal
print(a <= b)   # True  → less than or equal

#3. Logical Operators
#Combine multiple conditions together.
age = 25
salary = 50000

# and → both conditions must be True
print(age > 18 and salary > 30000)   # True

# or → at least one condition must be True
print(age > 18 or salary > 100000)   # True

# not → reverses the result
print(not(age > 18))                 # False

#Real use case
is_logged_in = True
is_admin = False

# User can view page if logged in
# User can delete only if admin
print("Can view:", is_logged_in)
print("Can delete:", is_logged_in and is_admin)

#4. Assignment Operators
#Shorthand for updating variable values
x = 10
x += 5    # same as x = x + 5  → 15
x -= 3    # same as x = x - 3  → 12
x *= 2    # same as x = x * 2  → 24
x /= 4    # same as x = x / 4  → 6.0
x //= 2   # same as x = x // 2 → 3.0
x **= 3   # same as x = x ** 3 → 27.0
x %= 5    # same as x = x % 5  → 2.0

#5. Identity Operators
#Check if two variables point to the same object in memory (not just equal value)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  → same value
print(a is b)   # False → different objects in memory
print(a is c)   # True  → c points to same object as a

print(a is not b)  # True

# Key difference:
x = 10
y = 10
print(x is y)   # True → Python caches small integers (-5 to 256)

x = 1000
y = 1000
print(x is y)   # False → large integers not cached

#6. Membership Operators
#Check if a value exists inside a sequence.
fruits = ["apple", "mango", "banana"]

print("mango" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# Works on strings too
name = "Rahul"
print("R" in name)      # True
print("z" not in name)  # True

# 7. Bitwise Operators
#Work on binary representation of numbers. (Used in DSA and systems programming)
a = 5   # binary: 0101
b = 3   # binary: 0011

print(a & b)   # 1  → AND  (0001)
print(a | b)   # 7  → OR   (0111)
print(a ^ b)   # 6  → XOR  (0110)
print(~a)      # -6 → NOT
print(a << 1)  # 10 → Left shift  (1010)
print(a >> 1)  # 2  → Right shift (0010)



## Operator Precedence (PEMDAS style)
#Python evaluates in this order — highest to lowest:

#1. ()         → Parentheses
#2. **         → Exponentiation
##3. ~, +, -    → Unary operators
#4. *, /, //, %→ Multiplication, Division
#5. +, -       → Addition, Subtraction
#6. <<, >>     → Bitwise shift
#7. &          → Bitwise AND
#8. ^          → Bitwise XOR
#9. |          → Bitwise OR
#10. ==, !=, >, <, >=, <=, is, in → Comparisons
#11. not        → Logical NOT
#12. and        → Logical AND
#13. or         → Logical OR

#Example:
result = 2 + 3 * 4 ** 2 - 1
# Step 1: 4 ** 2 = 16
# Step 2: 3 * 16 = 48
# Step 3: 2 + 48 = 50
# Step 4: 50 - 1 = 49
print(result)  # 49

# Always use parentheses to be explicit
result = (2 + 3) * (4 ** 2) - 1  # 79

#Practice Exercises

#Write a program that takes your monthly salary and calculates yearly salary, tax (20%), and take-home pay using arithmetic operators.
Monthly_salary = int(input("Enter your monthly salary: "))
Yearly_salary = Monthly_salary * 12
Tax = Yearly_salary * 20/100
Total_salary = Yearly_salary - Tax 
print("Total salary:", Total_salary)


#Check if a number is divisible by both 3 and 5 using logical and modulus operators.
number = int(input("Enter a number"))
if number %3 == 0 and number %5 == 0:
    print("Number is divisible by 3 and 5")
else:
    print("Number not divisible by 3 and 5")

#A user can get a discount if their cart value is above 500 OR they are a premium member. Write the condition using logical operators.
cart_value = float(input("Enter cart value: "))
is_premium = input("Are you a premium member? (yes/no): ").lower() == "yes"

# Condition for discount
if cart_value > 500 or is_premium:
    print("User gets a discount")
else:
    print("User does NOT get a discount")

#What is the result of 10 // 3 * 2 + 1? Solve manually then verify
print(10//3*2+1)

