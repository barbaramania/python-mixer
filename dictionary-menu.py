menu = {
    "pizza": 4.45,
    "burger": 5.25,
    "pasta": 6.75,
    "salad": 3.95,
    "fries": 2.50,
    "soda": 1.85,
    "coffee": 2.15,
    "sandwich": 4.95,
    "soup": 3.50,
    "ice cream": 2.75,
    "cake": 3.95
}

cart = []
total = 0

print("\n🍽️  Welcome to Our Restaurant! 🍽️\n")
print("Here is our menu:\n")
print("╔══════════════════╦═══════════╗")
print("║      Item        ║   Price   ║")
print("╠══════════════════╬═══════════╣")
for key, value in menu.items():
    print(f"║ {key.capitalize():<16} ║ ${value:>7.2f}  ║")
print("╚══════════════════╩═══════════╝")
print("\n🌟 Feel free to select items from the menu! 🌟\n")


while True:
    food = input("Select an item (q to quit)").lower()

    if food == "q":
     break
    elif food in menu:
      cart.append(food) #looking for key value but doesnt work backwards 
      total += menu.get(food)
    else:
       print (f"Sorry, {food} is not on the menu. Please choose another item.")

print("\nHere's your order summary:")
for item in cart:
    print(f"  - {item.capitalize():<10}: ${menu[item]:.2f}")
print(f"\n Your total is: ${total:.2f}")