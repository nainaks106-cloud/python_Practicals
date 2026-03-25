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

Type Casting (converting types)
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
2name = "error"       # cannot start with number
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

