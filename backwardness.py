#writing the number backward in a list


number = str(input("Print any number: "))
#can add check if it's a number
#number = str(1234)
lenght = len(number)
new_number=[0]*lenght
x=0
a = lenght - 1
while x < lenght:
    new_number[a] = int(number[x])
    a = a - 1 
    x = x + 1 
print(new_number)