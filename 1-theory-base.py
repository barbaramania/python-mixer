# import module # as mod
 # print(help(module))
# refer to module: mod.pi
# we can create our own module in a separate file


# This is my basic skills
print("Hi")
print("It's really good!")


# Variables
first_name ="Jessica" #string
age = 25 #integer
price = 10.498 #float
status = False #boolean (or True)

print(f"Hello {first_name}") #f-string formating
#print is automathicly as a println, to errase \n we can print(first_name, end =" ") - spece insead of \n

#collection = single "variable" used to store multiple variables

#list[]: ordered, changeable, duplicates are ok
fruits = ["apple", "banana", "orange"] #printed as ['apple','banana','orange']
print(fruits)
# dir(fruits) #list of attributes and methods
# help(fruits) #list of attributes and methods with the description
print("apple" in fruits) #boolean
fruits[1] ="pineapple" # ["apple", "pineapple", "orange"]
fruits.index("pineapple") #1
fruits.count("pineapple") #1
fruits.append("coconut") # ["apple", "pineapple", "orange", "coconut"] as [0,1,2,3]
fruits.remove("apple") # ["pineapple", "orange", "coconut"] as [0,1,2]
fruits.insert(2, "pear") # ["pineapple", "orange", "pear", "coconut"] as [0,1,2,3]
fruits.sort() #return none
print(fruits) # ['coconut', 'orange', 'pear', 'pineapple']
fruits.reverse() #return none
print(fruits) # ['pineapple', 'pear', 'orange', 'coconut']
fruits.clear

#set{}: unordered and immutable, add/remove ok, but no duplicates
fruits = {"apple", "banana", "orange"} 
print(fruits) #unordered ['banana', 'apple', 'orange']
# dir(fruits) #list of attributes and methods
# help(fruits) #list of attributes and methods with the description
# print(fruits[0]) will not work is there are no order
# add, remove, pop - remove the first random element, clear

# tuple(): ordered and unchangable. duplicates ok, faster
fruits = ("apple", "banana", "orange") 
print(fruits) # ('apple', 'banana', 'orange')
# dir(fruits) #list of attributes and methods
# help(fruits) #list of attributes and methods with the description
print(fruits[0]) #apple
# count, index


# 2dlist =[list1, list2, list3] or ([],{},()) and so on like an excel spreadsheet
fruits =     ["apple", "orange", "pineapple"]
vegetables = ["potato", "tomato"]
meats =      ["chicken", "beef", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
print(groceries) # [['apple', 'orange', 'pineapple'], ['potato', 'tomato'], ['chicken', 'beef', 'fish', 'turkey']]
print(groceries[0]) # ['apple', 'orange', 'pineapple']
print(groceries[0][1]) # orange

for collection in groceries:
    print(collection)
    # ['apple', 'orange', 'pineapple']
    # ['potato', 'tomato']
    # ['chicken', 'beef', 'fish', 'turkey']

for collection in groceries:
    for food in collection:
     print(food, end = " ")   
    print()
    # output is element by element:
    # apple orange pineapple
    # potato tomato
    # chicken beef fish turkey
 

# dictionary = a collection of {key:value} pairs. Ordered and changeable. No duplicates

capitals = {"USA":"Washington D. C.", 
            "India":"New Delhi",
            "Belarus":"Minsk"}
# dir/help(capitals)
if capitals.get("USA"):
    print("That capital exists. ")
else:
    print("That capital does not exist. ")

capitals.update({"Germany":"Frankfurt"}) #adds to the end
capitals.update({"Germany":"Berlin"}) #works fine
capitals.pop("India")
capitals.popitem() #remove the latest that was inserted - Germany
# capitals.clear() #clear the whole dictionary
capitals.keys() #retun keys -> dict_keys(['USA', 'Belarus'])
capitals.values() #return values -> dict_values(['Washington D. C.', 'Minsk'])
capitals.items() #return 2dlist of tuple [(),()]
# capitals.get(1)[0] # return a first value of the first evement 



#Typecusting - the process of converting a variable from one type to anither str(), int(), float(), bool()
#concatenation. no str into int OR bool always True is it's not null

print(type(price))
price = int(price)
print(type(price))


#input functions
number = input("What is your age? ") #always as a string
number = int(number)
number += 1
print(f"Wow! You're {number} yrs old!")

# Calculaing the volume of a parallelepiped

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
print(f"The volume is {length * width * height}cm^3")


# math
count = 0
count += 4
count -= 1
count *= 3
count /= 2 #4.5
count **= 2 #4.5^2 = 20.25
count %= 3 #remaidner=2.25 as 20.25/3 = 6 (2.25) 
count //= 4 # = 1 as the oposite of %: 6/4 = 1 - full

print(round(count)) #2
# abs = ||, pow(x,y)=x^y, max(x,y,z), min(x,y,z)
import math    #for
print(math.pi)
print(math.e)
print(math.sqrt(count))

radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius
area = math.pi * pow(radius,2)
print(f"The circumference is: {round(circumference)}cm and the are is {area}cm^2")

#if-else-statement. The logic is horrible and it's just for an exapmle
age2 = int(input("Enter your age: "))
if age2 >= 18 and age2<101: # 18<=age2<101 - same
    if age2 == 100:
        print("Are you real?")
    else:
        print("You are allowed!")
elif age2 < 0:
    print("Who are you?")
else:
    print("Sorry, see you later!")

# while loop
name = input("Enter your name: ")
while name =="":
    name = input("Enter your name: ")
print(f"Hello {name}")

food = input("Enter ypur favorite food (q to quit): ")
while not food =="q":
    print(f"You like {food}")
    food = input("Enter ypur favorite food (q to quit): ")
print("Bye!")


# For Loop. range(), string(), sequence()
for x in range(1,11): #11 is exlusive
    if x ==9:
        continue #skip 9 
        #break if we need to break the whole cycle
    else:
        print(x)
#output is 1 2 3 4 5 6 7 8  10

print("The reversed order with the step 2: ")
for x in reversed(range(1,11,2)): 
    print(x)
#output is 9 7 5 3 1

print("The reversed order by index for string '38190': ")
number = "38190"
for x in number[::-1]: #for number not for x
    print(x)
print(number) # 38190 as we didn't change the number and just gave x all values

#nested loop. outer loop: 
#               inner loop:

for x in range(3):
    for y in range(1,10):
        print(y, end =" ") #all numers are at the same line
    print()



#logical operators
#and, or, not

condition3 = False
age3 = int(input("Enter your age: "))

if age3 >= 18 and age3!=100 and age3!=101: 
    print("You are allowed!")
elif age3 == 100 or age3 == 101 and not condition3:
    print("Congrats!")
else:
    print("Sorry, see you later!")   

#conditional expressions. if-else in one line
num = 4
print ("Positive" if num > 0 else "Negative")
a = 4
b = 5
max_num = a if a<b else b
print(max_num)

# functions and method
name = "ASApi name number"
len(name) #10
    #string
name.find("n") #6
name.rfind("n") #11 - last n. -1 if there are no results
name.capitalize() #Asapi name number
name.upper() #ASAPI NAME NUMBER
name.lower() #asapi name number
name.isdigit() #True or False -> False as not only num
name.isalpha() #True or False -> False as not only alphabethical (" ")
name.count(" ") #2
name.replace(" ", "-") #ASApi-name-number

#helper
#print(help(str))

#indexing [start:end:step] - string
card_number = "123-456-78"
print(card_number[1:6:2]) #2-5
print(card_number[-2]) #7 as it is a second digit from the end. starts from -1
print(card_number[-4:]) #6-78 - as the last 4 digits
print(card_number[::-1]) #87-654-321 - skiped the start and end and now we have a step "-1" representing that we're moving backwards 


# format specifiers. value.flags
#value:.2f= x.00
#value:10 =        x - 10 spaces
#value:02 = 00x - 0-paded
#value:<5 = x    - left-justified
#value:>5 =     x- right-justified
#value:^5 =   x  - centred
#value:-  = -x  - showing "-", same as + or space for +
#value:+  = -x  - showing "+", same as space 
#value:, = -x,0  - changing . into a , 

price1 = 2.14243
price2 = -890.90
price3 = 12
print (f"{price1:+,.2f}\n{price2:+10}\n{price3:>5}")
# output:
# +2.14
#     -890.9
#    12


#Randomizer
import random
# help(random)

random.randint(1,6) #from 1 to 6

a, b = 1,5
random.randint(a, b) #ok if a and b is int

options = ("rock", "paper", "scissors")
random.choice(options)

MyList = ["2", "3", "A", "Number", "12"]
random.shuffle(MyList)


##
# function = a block of reusable code fun()
# the passing order of parametres should be the same
def welcoming_function():
    print("hey")
welcoming_function()

def welcoming_function_name(name):
    print(f"hey {name}")
welcoming_function_name("Steve")

#  types of arguments for functions : 1. positional 2. default 3. keyword 4. arbitrary
def divide(x, y):
    z = x / y
    return z
print(divide(10,3))

# default arguments 
def net_price(list_price, discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)
print(net_price(500))
print(net_price(500,0.2)) # now dicsount = 0.2 instead of default 0

# keyword arguments - order of arguments doesn't matter
def gello(greeting, title, first, last):
   print(f" {greeting} {title} {first} {last}")

#using keywords after assigning without it
# if we started wirh a keyword - the following should has keywords as well
gello ("Hi","Mr.", last = "Paper",first ="Jonh")

def get_phone(country, area, first, last):
   return f"{country} - {area} - {first} - {last}"

phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)

# arbitrary
# *args = multiple non-key - put into tuple(), 
# **kwargs = multiple keyword - put onto dictionary[]

def add(*nums):
    total = 0
    for num in nums:
        total+=arg
    return total

print(add(1,2,3,4))
#kwargs
def print_address(**kwargs):
    for value in kwargs.values():
        print(value)
    # for key,value in kwargs.items():
    #     print(f"Key is {key}: value :{value}")


print_address(street = "North West" , city = "Chicago", country = "Us")

# Iterables = An object/collection that can return its element 
#              one at a time, allowing it to be iterated over in a loop

numbers =[1,2,3,4,5,6]
# string, list, tuple, {}, dictionary are iterable

for number in numbers:
#for number in reversed(numbers):
    print(number)


# membership operators = used to test whether a value/variable is found in a sequence
#                         (string, list, tuple, set, dictionary)
#                         in/ not in
word = "APPLE"
if "A" in word:
    print("The is a letter 'A' in a word")

# if it's a dictionary 
dic = {"a": "first", "b": "second", "c": "third"}
letter = input()
if letter in dic:
    print (f"{letter} has a {dic[letter]} number")


# list comprehension - [expression for value in iterable #+if condition]
doubles = [x*2 for x in range(1,11)]
print(doubles)

fruits = ["apple","orange","banana"] 
fruits = [fruit.capitalize() for fruit in fruits]    
print(fruits)

# with if condition
numbers = [1,3,-5,2,-10]
positive_nums = [num for num in numbers if num>=0]
even_nums = [num for num in numbers if num == 0]



# match-case statement (switch):
def day_of_week(day):
    match day:
        case 1:
            return "It's Sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Wendesday"
        case _:
            return "There is no matching case"
        
print(day_of_week(3))

# using or in case switch
def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday":
            return False
        case _:
            return False
        
print(is_weekend("Monday"))

# variable scope = where a variable ia visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in. local is using first and so on

# a is local for this functions
def fun1():
    a = 1
    print(a)
def fun2():
    # a is local for this function, 
    # but it's different from a fun1
    a = 2
    print(a)

fun1()
fun2()

# Enclosed were function in function
# Global is outside of any function
x = 3
print(x)
# built-in
from math import e
print(e)
