foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit):")
    if food.lower() == "q":
     break
    else:
       price = float(input(f"Enter the price of a {food}: $"))
       total += price
       foods.append(food)
       prices.append(price)
       
print (f" The is your list: ")
for x in range (0, len(foods)):
    print(f"{foods[x]} for ${prices[x]}")
print(f"Your total is ${total}")