
import random

# Game 1
#Integer guess game
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
print(answer)
guesses = 1
is_running = True

print(f"Hello! Select a number between {lowest_num} and {highest_num}.")
while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():

        guess = int(guess)
        if answer < guess < highest_num:
            print("---Too high. Try again")
            guesses += 1
        elif lowest_num < guess < answer:
            print("---Too low. Try again")
            guesses+= 1
        elif guess == answer:
            print(f"\nYou nailed it! The correct answer is {answer}")
            print(f"Total number of quesses is {guesses}")
            is_running = False
        else:
           print(f"---The number is out of range.\n Select a number between {lowest_num} and {highest_num}.")
           guesses += 1
    else:
        print(f"---It is not a number.\n Select a number between {lowest_num} and {highest_num}.")
        guesses += 1
        
# # Game 2
# # rock-paper-scissors

# options = ("rock", "paper" , "scissors")
# running = True

# while running:
#     player = None
#     computer = random.choice(options)

#     while player not in options:
#         player = input("Enter a choice:'rock', 'paper' , 'scissors': ").lower()

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")
#     if computer == player:
#         print ("It's a tie!")
#     elif (player == "rock" and computer == "paper") or (player == "paper" and computer == "scissors") or (player == "scissors" and computer == "paper"):
#         print ("Computer won!")  
#     else:
#         print("You won!")
    
    
#     if input("One more game? (y or n): ").lower() != "y":
#         running =  False


# print("Thanks for playing")