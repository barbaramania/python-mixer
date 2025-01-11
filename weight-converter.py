#This is a simple weight converter 

weight = float(input("Enter your weight: "))
unit = input("Is this weight in killograms or pounds(K or P)? ")

if unit =="K"or unit =="k":
    converted_weight = round(weight * 2.205,2)
    converted_unit = "Lbs."
    print(f"Your weight in pounds is {converted_weight}{converted_unit}")
# same as :
# if unit =="K"or unit =="k":
#     print(f"Your weight in pounds is {round(weight * 2.205,2)}Lbs. ")

elif unit =="P" or unit =="p":
    converted_weight = round(weight/2.205,2)
    converted_unit = "Kgs."
    print(f"Your weight in killograms is {converted_weight}{converted_unit}")
else:
    print("Unit is not valid!")