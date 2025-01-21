#Given an integer x, return yes if x is a palindrome, and no otherwise.

number = str(-121)
lenght = len(number)
new_number=[0]*lenght
x=0
a = lenght - 1
while x < lenght:
    new_number[a] = number[x]
    a = a - 1 
    x = x + 1 
new_number= ''.join(new_number)
print(number, new_number)
if new_number == number:
   print("yes")
else:
    print("no")


# optimization:

# Negative numbers cannot be palindromes.
# if number < 0:
#     print("no")

# Using built-in function to reverse the number as a string
# else:
#     number_str = str(number)
#     if number_str == number_str[::-1]:
#         print("yes")
#     else:
#         print("no")