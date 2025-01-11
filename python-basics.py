# # This is my basic skills
# print("Hi")
# print("It's really good!")

# # Variables
# first_name ="Jessica" #string
# age = 25 #integer
# price = 10.498 #float
# status = False #boolean (or True)


# print(first_name)
# print(f"Hello {first_name}") #f-string formating

# #Typecusting - the process of cinverting a variable from one type to anither str(), int(), float(), bool()
# #concatenation. no str into int OR bool always True is it's not null

# print(type(price))
# price = int(price)
# print(type(price))


# #input functions
# number = input("What is your age? ") #always as a string
# number = int(number)
# number += 1
# print(f"Wow! You're {number} yrs old!")

# # Calculaing the volume of a parallelepiped

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# height = float(input("Enter the height: "))
# print(f"The volume is {length * width * height}cm^3")


# # math
# count = 0
# count += 4
# count -= 1
# count *= 3
# count /= 2 #4.5
# count **= 2 #4.5^2 = 20.25
# count %= 3 #remaidner=2.25 as 20.25/3 = 6 (2.25) 
# count //= 4 # = 1 as the oposite of %: 6/4 = 1 - full

# print(round(count)) #2
# # abs = ||, pow(x,y)=x^y, max(x,y,z), min(x,y,z)
# import math    #for
# print(math.pi)
# print(math.e)
# print(math.sqrt(count))

# radius = float(input('Enter the radius of a circle: '))
# circumference = 2 * math.pi * radius
# area = math.pi * pow(radius,2)
# print(f"The circumference is: {round(circumference)}cm and the are is {area}cm^2")

# #if-else-statement. The logic is horrible and it's just for an exapmle
# age2 = int(input("Enter your age: "))
# if age2 >= 18 and age2<101: # 18<=age2<101 - same
#     if age2 == 100:
#         print("Are you real?")
#     else:
#         print("You are allowed!")
# elif age2 < 0:
#     print("Who are you?")
# else:
#     print("Sorry, see you later!")

# #logical operators
# #and, or, not

# condition3 = False
# age3 = int(input("Enter your age: "))

# if age3 >= 18 and age3!=100 and age3!=101: 
#     print("You are allowed!")
# elif age3 == 100 or age3 == 101 and not condition3:
#     print("Congrats!")
# else:
#     print("Sorry, see you later!")   

# #conditional expressions. if-else in one line
# num = 4
# print ("Positive" if num > 0 else "Negative")
# a = 4
# b = 5
# max_num = a if a<b else b
# print(max_num)

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
