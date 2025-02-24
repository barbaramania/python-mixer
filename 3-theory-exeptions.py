##########################
# ALL ABOUT EXCEPTIONS # #
##########################

# ####################################
# exception = an event that interrupts the flow of the program
#             (ZeroDivisionError, TypeError,ValueError)
#             1. try: 2. except: 3. finally

try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print ("Enter only numbers please")

# not a good practice to have it for everything at ones. Use as a last resort
except Exception: 
    print("Something went wrong")

finally:
    print("Do some cleanup here") #will execute anyway


