# Python Slot Machine
# Using three separate functions in the code
# to spin, print, and count balance

# Additions in the code:
# using continue instead of forever-while input
# using case switch instead of else-if

import random
import time

def spin_row():
    # set{} is unordered, but it's unsplittable, so no point to use it
    # () tuple will use less memory
    symbols = ("😊", "😭", "😍", "😁", "🫡")
    # for a randomizer loop:
    # row.append(random.choice(symbols))
    return random.choices(symbols, k=3)

def print_row(row):
    for _ in row:
        time.sleep(1)
        print(_, end=" ")  
    print()  # For a new line after the row is printed

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        match row[0]:
            case "😊": return bet * 2
            case "😭": return bet * 3
            case "😍": return bet * 4
            case "😁": return bet * 5
            case "🫡": return bet * 6
    else:
        return 0

def main():
    balance = 100

    # Welcome message with a nice border
    print("╔══════════════════════════════╗")
    print("║     Welcome to Emoji Slots!  ║")
    print("║    🎰  Spin the Reels!  🎰   ║")
    print("╚══════════════════════════════╝")
    print("\n✨ Match 3 identical symbols to win! ✨")
    print("Symbols: 😊 😭 😍 😁 🫡")

    print(f"\nStarting balance: ${balance}")
    
    # Checking conditions for the game loop
    while balance > 0:
        bet = input("Place your bet amount (press 'f' to exit) $ ")

        if bet.lower() == 'f':
            print(f"\n🎉 See you next time! Your balance is: ${balance}")
            exit()

        if not bet.isdigit():
            print("⚠️ Your bet should be a number! Please try again.")
            continue

        bet = int(bet)

        if bet > balance:
            print("⚠️ Insufficient funds. You don't have enough balance!")
            continue

        if bet <= 0:
            print("⚠️ Bet amount must be greater than zero.")
            continue

        balance -= bet
        row = spin_row()
        print("\nSpinning the reels... ⏳")
        print_row(row)
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"🎉 Congratulations! You won ${payout} 🎉")
        else:
            print("Sorry, you lost this round. Better luck next time!")

        balance += payout
        print(f"\nYour current balance: ${balance}")

    # Final message when the player runs out of balance
    print("\n❌ Game Over! You have no more balance. Thanks for playing! ❌")

if __name__ == '__main__':
    main()
