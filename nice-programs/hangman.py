# using a dictionary with tuples

# this is hangman game with a food topic

import random
# can create a separate file for a variety of words
from wordsForHangman import words


# dictionary of key:()
# key is a number of guesses
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" O ",
        "   ",
        "   "),
    2: (" O ",
        " | ",
        "   "),
    3: (" O ",
        "/|",
        "  "),
    4: (" O ",
        "/|\\",
        "   "),
    5: (" O ",
        "/|\\",
        "/   "),
    6: (" O ",
        "/|\\",
        "/ \\")
}

def display_man(wrong_guesses):
    print("\n----------------")
    # calling spesific value in the dictionary
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("----------------\n")

# list of underscore chacacters
# flip a letter in we guessed right
def display_hint(hint):
    # printing a list with a space insted of '','',
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    #creating a list with a special size
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    # creating an empty set, a =() doesn't work
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input ("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Only one letter at a time")
            continue

        if guess in guessed_letters:
            print("Your guess is already guessed")
            continue

        guessed_letters.add(guess)
        
        if guess in answer:
            for index in range(len(answer)):
                if answer[index] == guess:
                    hint[index] = guess
        else:
            wrong_guesses += 1        

        if "_" not in hint:
            display_man(wrong_guesses)  
            display_answer(answer)
            print("You win!\n")
            is_running = False
        elif wrong_guesses >= 6:
            display_man(wrong_guesses)  
            display_answer(answer)
            print("You lose :(\n")
            is_running = False

if __name__ == '__main__':
    main()