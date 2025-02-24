####################################
# ALL ABOUT CLASSES, DECORATORS # #
####################################



 # object = A "bundle" of related attributes (variables) and methods (functions)
        #   object - cup contains this attributes:
            #   liquid = "coffee"
            #   temp = 70
            #   is_empty = False
# a method is a function that belongs into an object 
            #   def fill_cup():
            #   def empty_cup():

# To create any object we need a class
# class = used to design the structure and layout of an object

##################################################
# class is usually a separate file named lowercase
# from car import Car - if we are using a separate file

# capitalized
class Car:
    # this is a constructor
    # dunder method = double underscore "__"

    # self refers to the object we currently working with
    def __init__(self, model, year, color, for_sale):
        # access throught self 
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # methods are identical for each object:
    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stopped the {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")

# matching number of arguments exept 'self'
car1 = Car("Toyota", 2011, "Black", True)
car2 = Car("Mustang", 2000, "Red", False)

print(car1) # <__main__.Car object at 0x0000023CA08C2ED0> - memory slot 

# '.' - attribute access operator
print(car1.model) # Toyota

car2.drive() # You drive the Mustang
car2.describe() # 2000 Red Mustang

# Note: Nested functions (inner functions) cannot be accessed directly from the main code or other functions 
# because they are local to the enclosing function. 
# However, methods in a class can be accessed from outside the class through an instance of the class.

###################################

# class variables  = shared among all instances of a class
#                     Defined outside the constructor
#                     Allow you to share data among all objects created from that class

class Student:
    #class variable

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Klara", 32)
student2 = Student ("Kim", 12)

print(student1.name, student1.age, student1.class_year) #Klara 32 2025
print(Student.class_year, Student.num_students) # 2025 2 - better practice

############################

# Inheritancce - Allows a class to inherit attributes and methods from another class
#                 Helps with code reusability and extensibility
#                 class Child(Parent) same as Sub(Super)

class Animal:
    def __init__ (self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")

dog = Dog("Puff")
cat = Cat("Snow")
mouse = Mouse("Mimi")

print(dog.is_alive) # True
print(mouse.sleep()) # Mimi is sleeping
                     # None        
# mouse.sleep()
dog.speak() # Woof!

##############################

# multiple inheritance - inherit from more than one parent class
                        # C(A, B)

#  multilevel inheritance - inherit from a parent which inherits from another parent
                # B(A)
                # C(B)

# super() - function used in a child class to call methods from a parent class(superclass)
            # class Super:
            #     pass
            # class Sub(Super)

class Shape:
    def __init__(self, color, border):
        self.color = color
        self.border = border
    def describe(self):
        print(f"Parent. It is {self.color} and {'has a border' if self.border else 'doesnt have a border'}")

class Triangle(Shape):
    def __init__(self, color, width, border):
        # self.color = color
        # self.border = border
        super().__init__(color,border)
        self.width = width

class Circle(Shape):
    def __init__(self, color, radius, border):
         #    self.color = color
         #    self.border = border
         super().__init__(color,border)
         self.radius = radius

    # method overwriting
    def describe(self):
         print(f"Child. It is a circle with radius {self.radius}")
 

class Square(Shape):
    def __init__(self, color, width, border):
         #    self.color = color
         #    self.border = border
         super().__init__(color,border)
         self.width = width

    # method overwriting
    def describe(self):
         print(f"Child. It is a square with width {self.width}")
         # extending the functionality
         super().describe()    


circle = Circle('red', 3, True)
triangle = Triangle('black', 10, False)
square = Square('white', 7, False)

print(circle.color) #red

triangle.describe() # Parent. It is black and doesnt have a border
# method overwriting, using a childs version:
circle.describe() # Child. It is a circle with radius 3
# extended method overwriting, using both child and parent versions:
square.describe() # Child. It is a square with width 7
                  # Parent. It is white and doesnt have a border

###############################

# Polymorphism = "have many forms or faces"
#                 1. Inheritance - an ibject could be treated of the  type as a parent class
#                 2. "Duck Typing" - object must have necessary attributes/methods

# this is to work with abstract methods/classes
from abc import ABC, abstractclassmethod

class Shape:

    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14* self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, type, radius):
        self.type = type
        super().__init__(radius)



shapes = [Circle(4), Square(5), Triangle(6,7), Pizza('Veg', 22)]
for shape in shapes:
    print(f"{shape.area()}cm^2", end = ", ")
    # 50.24cm^2, 25cm^2, 21.0cm^2, 1519.76cm^2, 



# "Duck Typing" - "If it looks like a duck and quacks like a duck, it must be a duck"

# Basically, we didn't inheritanced anything, but put the same attributes 
# and methods separatly in a class without the same parent

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:
    def horn(self):
        print("Honk!")

class CarDuck:
    def speak(self):
        print("Honk!")
    alive = False

animals = [Dog(), Cat(), Car()]

# for animal in animals:
#     animal.speak()
# # AttributeError: 'Car' object has no attribute 'speak' 

newAnimals = [Dog(), Cat(), CarDuck()]

for animal in newAnimals:
    animal.speak()
    # don't need (), because we're working with an attribute, not with method
    print(animal.alive)
# Woof!
# True
# Meow!
# True
# Honk!
# False    

#################################

# Static methods - a method that belong to a class rather than any object from that class(instance)
#                 usually used fro general utility functions

# Instance methods - best for operations on instances of the class (objects) /def inst(self):/
# Static methods - best for utilitu functions that dont need access to class data / @staticmethod def inst(var): return/

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    # Instance method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    # Static method because we are using variables that were created inside of this class
    #there is no 'self' or any objects that we created inside of __init__
    @staticmethod #decorator
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook"]
        return position in valid_positions
    

#we are calling a method that is not connected with any object
#we dont need any employee1
print(Employee.is_valid_position("Cook")) #True

employee1 = Employee("Peter", "Manager")
employee2 = Employee("Pan", "Cook")

print(employee1.get_info()) #Peter = Manager


 ######################################

# Class methods - allow operations related to the class itself
#                 take (cls)/(self) as the first parameter, which repserents the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name= name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += self.gpa
        
    # Instance method
    def get_info(self):
        return f"{self.name} = {self.gpa}"
    
    # Class method
    @classmethod
    def get_count(cls):
        return f"Total number of students {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else: 
            return f"The average gpa is {cls.total_gpa/cls.count:.2f}"


student1 = Student("Bill", 3.4) 
student2 = Student("Myra", 2.4)
student3 = Student("Peter", 3.9)

print(Student.get_count()) #Total number of students 3
print(Student.get_average_gpa()) #The average gpa is 3.23

# ####################################
# Magic methods = Dunder methods ( double ubderscore) __init__, __str__, __eq__
#                 Authomatically called by many of pythons built-in operators.
#                 Allow developrs to define or customize the behavior of objects

class Magic:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # method will print a sentence from return insted of printing the address
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__ (self,other):
       return self.title == other.title and self.author == other.author
    
    def __lt__ (self,other):
        return self.num_pages < other.num_pages 
    # same for > __gt__
    
    def __add__(self,other):
        return f"{self.num_pages + other.num_pages} pages" 

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__ (self,key):
        if key == "title":
         return self.title
        elif key == "author":
         return self.author
        elif key == "num_pages":
         return self.num_pages
        else:
            return f"Key '{key}' was not found"



book1 = Magic("Fairy", "First", 50)
book1a = Magic("Fairy", "First", 50)
book2 = Magic("Billian", "Second", 1223)
book3 = Magic("The Lion", "Third", 232)

print(book3) #The Lion by Third
print(book1 == book1a) #False befor the __eq__ , True after creating that method
print(book1 < book2) # TypeError: '<' not supported between instances of 'Magic' and 'Magic'
                     # True after creating __lt__ 
#  for > is __gt__
print(book1 + book2) # TypeError: unsupported operand type(s) for +: 'Magic' and 'Magic'
                     # 1273 pages after creating __add__ 
print ("Lion" in book3) # TypeError: argument of type 'Magic' is not iterable
                        # True after creating __contains__
print(book1['title']) #TypeError: 'Magic' object is not subscriptable
                      # Fairy

# ####################################
# @property = decorator used to define a method as a property 
#             (it can be accessed like an attribute)
#             Benefit: add additional logic when read, write, or delete attributes
#             gives you getter, setter, and deleter method 

class Rectangle:
    def __init__ (self, width, height):
        # _attribute = private, can access only within this class
        self._width = width
        self._height = height
    
    # 2 getters
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    # 2 setters
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print ("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print ("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("width was deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("height was deleted")

rectangle = Rectangle (10,8)

#direct
print(rectangle._width) #will return 10 anyway
print(rectangle._height)

#using getter methods
print(rectangle.width) #10
print(rectangle.height) #8

rectangle2 = rectangle
rectangle2.width = 0 # Width must be greater than zero
print(rectangle2.width) #10
rectangle2.width = 5 # No output
print(rectangle2.width) #5

del rectangle.height # AttributeError: property 'height' of 'Rectangle' object has no deleter
                     # height was deleted after adding deleter

# print(rectangle.height) #AttributeError: 'Rectangle' object has no attribute '_height'.

# ####################################
# Decorator = A function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the Decorator


# without the wrapper the functioin will execute without calling it in code
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("You add sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
# get_ice_cream - base function
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream")

# # before adding any flavors we dont need any arguments and *args, **kwargs
# get_ice_cream() # You add sprinkles
#                 # You add fudge
#                 # Here is your ice cream
                
get_ice_cream("vanilla") # TypeError: get_ice_cream() missing 1 required positional argument: 'flavor'              
# works after we added *args, **kwargs




