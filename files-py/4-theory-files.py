
##########################
# #  ALL ABOUT FILES   # #
##########################

####################################
# # File detection

# file paths:
# relative -  folder/test.txt
# absolute - c:/users/folder/test.txt
#            c:\\users\\folder\\test.txt

import os

file_path = "files-py/test-folder/test.txt"
dir_path = "files-py/test-folder"
if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print("That location doesn't exist")


###################################
# # File writing (.txt, .json, .csv)
txt_data = "I like pineapple"

# "output.txt"- file in the main python-part1 folder
file_path = "files-py/output.txt"

# with will open and close the file
# "w" - if file FileExists - overwrite
# "x" - if file doesnt exist, if it exists = error
# "a" - append a file
# "r" - read
# as: file = File() - giving a name = returnt file after open()
with open(file = file_path, mode = "w") as file:
# with open(file_path,"w") as file: - the same
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

try:
    with open(file_path, mode = "x") as file:
    # FileExistsError without try-catch
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists!")
finally:
    pass
# Output.txt : I like pineapple

with open(file_path, "a") as file:
    file.write("! " + txt_data)
    print(f"txt file '{file_path}' was created")
# Output.txt: I like pineapple! I like pineapple

# example n.2
employees = ["Squidward", "Spongebob", "Patrick"]
file_path = "files-py/outputList.txt"

# TypeError: write() argument must be str, not list
with open(file_path, "w") as file:
    for employee in employees:
        file.write(employee + " ")
    print(f"txt file '{file_path}' was created")
# OutputList.txt: Squidward Spongebob Patrick 

#  JSON - collection of key-value pairs
import json
employee = {
    "name": "Spongebob",
    "age": 30,
    "position":"cook"
}
file_path = "files-py/output.json"

with open(file_path, "w") as file:
    # dump is converting a dictionary into json
    json.dump(employee, file)
    # json.dump(employee, file, indent = 4) - will add 4 spaces
    print(f"json file '{file_path}' was created")

#  CVS - comma separated values 
# list of lists
import csv

employees = [["Name", "Age", "Positioon"],
             ["Spongebob", 30, "Cook"],
             ["Patrick", 37, "Unemployed"],
             ["Sandi", 27, "Scientist"]]
file_path = "files-py/output.csv"

with open(file_path, "w", newline ="") as file:
# newline because in a for-loop we're creating an extra row
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"csv file '{file_path}' was created")


###################################
# # File reading (.txt, .json, .csv)

file_path = "files-py/output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
# Output: I like pineapple! I like pineapple
except FileNotFoundError:
    print("File was Not Found")
except PermissionError:
    print("You don't have permission")

#JSON Reading
import json

file_path = "files-py/output.json"

with open(file_path, "r") as file:
        content = json.load(file) ###
        print(content)
        # print(content["name"])
# Output: {'name': 'Spongebob', 'age': 30, 'position': 'cook'}

#CSV Reading
import csv

file_path = "files-py/output.csv"

with open(file_path, "r") as file:
        content = csv.reader(file) ###
        for line in content:
                print(line)
                # print(line[0]) - all names
# Output:['Name', 'Age', 'Positioon']
# ['Spongebob', '30', 'Cook']
# ['Patrick', '37', 'Unemployed']
# ['Sandi', '27', 'Scientist']