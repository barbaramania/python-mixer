# validate user input experience
# <12 characters
# no spaces
# no digits

#Solution 1
user_name = input("What is your name? ")
if len(user_name) < 12 and user_name.find(" ") == -1 and not user_name.isalpha():
    print(f"Hello {user_name}! ")
elif not user_name.find(" ") == -1:
    print("Re-enter your user name without any spaces.")
elif not user_name.isalphat():
    print("Re-enter your user name without any numbers.")
else:
    print("Your user name cant be more than 12 variables")


#if we want to finish the program only after the correct validation 
#Solution 2
user_name = input("What is your name? ")
print(user_name.isalpha())
while len(user_name) >= 12 or user_name.find(" ") != -1 or not user_name.isalpha():
    print("There are some problems with your name.")

    if not user_name.find(" ") == -1:
        user_name = input("Re-enter your user name without any spaces: ")
    elif not user_name.isalpha():
        user_name = input("Re-enter your user name without any numbers: ")
    else:
        user_name = input("Re-enter your user name as user name cant be more than 12 characters: ")
else:
    print(f"Hello {user_name}! ")


#Some improvements in while condition.
# Solution 3
while len(user_name) >= 12 or (" " in user_name) or not user_name.isalpha(): #() has been changed
    print("There are some problems with your name.")
    
    if " " in user_name: 
        user_name = input("Re-enter your user name without any spaces: ")
    elif not user_name.isalpha():
        user_name = input("Re-enter your user name without any numbers or special characters: ")
    else:
        user_name = input("Re-enter your user name as it can't be more than 12 characters: ")

print(f"Hello {user_name}!")