##########################
#Programm 1
#This is my simple calculator

num1 =float(input("Enter the first number "))

operator= input("Enter an operator (+ - * /) ")
while len(operator) != 1:
    print("Please enter only one character.")
    operator = input("Re-enter an operator (+ - * /): ")

num2 =float(input("Enter the second number "))

#The next line will not run because the programm cannot use string 
# with numeric values. + - is an operator and doesnot belong in any datatype

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



######################
#programm 2
#Compund interest calculator

principle =0
rate = 0
time = 0

#Adds a variation of 0 in variable
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        principle = float(input("The principle amount should be more than zero: "))
    else:
        break

while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        rate = float(input("The rate amount should be more than zero: "))

while time <= 0:
    time = float(input("Enter the time in yers: "))
    if time <= 0:
        time = float(input("Time should be more than zero: "))

total = principle * pow((1 + rate / 100),time)
print(f"Balance after {time} year/s is ${total:.2f}")