# Python Banking program
# This program simulates a simple banking system where you can check your balance, 
# deposit money, withdraw money, and exit the program.

def show_balance(balance):
    print(f"---\nYour current balance is: ${balance:.2f}\n---")  

def deposit(balance):
    amount = float(input("Enter an amount to be deposited:  $"))  
    if amount > 0:
        return amount
    else:
        print("⚠️ Invalid amount! Please enter a positive number.")  
        return 0
  

def withdraw(balance):
    amount = float(input("Enter an amount to withdraw:  $"))  
    if (balance - amount) >= 0:
        return amount
    elif amount < 0:
        print("⚠️ Amount should be greater than 0.")  
        return 0
    else:
        print(f"⚠️ Insufficient funds! You can't withdraw ${amount:.2f} because your balance is ${balance:.2f}")  
        return 0



def main():
    balance = 0
    is_running = True

    while is_running:
        print("\n--- Banking App ---")  
        print("1. Show Balance")  
        print("2. Deposit")  
        print("3. Withdraw")  
        print("4. Exit")  

        choice = input("Enter your choice (1-4):  ")  

        match choice:
            case '1': 
                show_balance(balance)
            case '2': 
                balance += deposit(balance)    
                print(f"---\nYour current balance is: ${balance:.2f}\n---")  
            case '3': 
                balance -= withdraw(balance) 
                print(f"---\nYour current balance is: ${balance:.2f}\n---")  
            case '4': 
                is_running = False
            case _:
                print("---\n⚠️  Invalid choice. Please enter a valid option (1-4).\n---")  


    print("\n---\nThank you for using the banking program! Have a wonderful day!")  

if __name__ == '__main__':
    main()
