import random

# print("\u25CF \u250C \u2510 \u2502 \u2500 \u2514 \u2518")

# ● ┌ ┐ │ ─ └ ┘

top =           "┌─────────┐"
middle =        "│         │"
middle_double = "│  ●   ●  │"
end =           "└─────────┘"
dice_art = {
    1:(top, middle, "│    ●    │", middle, end),
    2:(top, "│  ●      │", middle, "│      ●  │", end),
    3:(top, 
            "│  ●      │", 
            "│    ●    │",
            "│      ●  │",
       end),
    4:(top, middle_double, middle,middle_double, end),
     5:(top, middle_double ,  "│    ●    │", middle_double, end),
     6:(top, middle_double, middle_double,middle_double, end)
}

# # checking how dice looks like
# for key, value in dice_art.items():
#     for item in value:
#         print(item)
#     print() 

dice = [] 
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))


# input where dices are lined down:

# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#           # get returns the value for a specified key. If the key doesn't exist, it returns None or a specified default value.
#         print(line)

# works the same
# for die in dice:
#     for line in dice_art.get(die):     
#         print(line)

# input where dices are in a row
# range(num_of_dice) based on index while die in dice based on element
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end =" ")
    print()
        

for die in dice:
    total += die
print(f"total: {total}")


