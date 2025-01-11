#This is my simple calculator

num1 =float(input("Enter the first number "))

operator= input("Enter an operator (+ - * /) ")
while len(operator) != 1:
    print("Please enter only one character.")
    operator = input("Re-enter an operator (+ - * /): ")

num2 =float(input("Enter the second number "))

#The next line will not run because the programm cannot use string with numeric values. + - is an operator and doesnot belong in any datatype

#print (num1 + operator + num2)

if operator == "+":
    print(f"The result is: {num1+num2}")
elif operator == "-":
    print(f"The result is: {num1-num2}")
elif operator == "*":
    print(f"The result is: {num1*num2}")
elif operator == "/":
    print(f"The result is: {round(num1/num2,3)}") #3 digits after the comma 
else:
    print("Sorry, but you can choose only between '+ - * /' ")