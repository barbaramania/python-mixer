# # object = A "bundle" of related attributes (variables) and methods (functions)
#         #   object - cup contains this attributes:
#             #   liquid = "coffee"
#             #   temp = 70
#             #   is_empty = False
# # a method is a function that belongs into an object 
#             #   def fill_cup():
#             #   def empty_cup():

# # To create any object we need a class
# # class = used to design the structure and layout of an object

# ###################################################
# # class is usually a separate file named lowercase
# # from car import Car - if we are using a separate file

# # capitalized
# class Car:
#     # this is a constructor
#     # dunder method = double underscore "__"

#     # self refers to the object we currently working with
#     def __init__(self, model, year, color, for_sale):
#         # access throught self 
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#     # methods are identical for each object:
#     def drive(self):
#         print(f"You drive the {self.model}")

#     def stop(self):
#         print(f"You stopped the {self.model}")

#     def describe(self):
#         print(f"{self.year} {self.color} {self.model}")

# # matching number of arguments exept 'self'
# car1 = Car("Toyota", 2011, "Black", True)
# car2 = Car("Mustang", 2000, "Red", False)

# print(car1) # <__main__.Car object at 0x0000023CA08C2ED0> - memory slot 

# # '.' - attribute access operator
# print(car1.model) # Toyota

# car2.drive() # You drive the Mustang
# car2.describe() # 2000 Red Mustang

# # Note: Nested functions (inner functions) cannot be accessed directly from the main code or other functions 
# # because they are local to the enclosing function. 
# # However, methods in a class can be accessed from outside the class through an instance of the class.

####################################

# # class variables  = shared among all instances of a class
# #                     Defined outside the constructor
# #                     Allow you to share data among all objects created from that class

# class Student:
#     #class variable

#     class_year = 2025
#     num_students = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1

# student1 = Student("Klara", 32)
# student2 = Student ("Kim", 12)

# print(student1.name, student1.age, student1.class_year) #Klara 32 2025
# print(Student.class_year, Student.num_students) # 2025 2 - better practice

#############################

# # Inheritancce - Allows a class to inherit attributes and methods from another class
# #                 Helps with code reusability and extensibility
# #                 class Child(Parent) same as Sub(Super)

# class Animal:
#     def __init__ (self, name):
#         self.name = name
#         self.is_alive = True
    
#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     def speak(self):
#         print("Woof!")

# class Cat(Animal):
#     def speak(self):
#         print("Meow!")

# class Mouse(Animal):
#     def speak(self):
#         print("Squeek!")

# dog = Dog("Puff")
# cat = Cat("Snow")
# mouse = Mouse("Mimi")

# print(dog.is_alive) # True
# print(mouse.sleep()) # Mimi is sleeping
#                      # None        
# # mouse.sleep()
# dog.speak() # Woof!
