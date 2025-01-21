questions = ("What is the capital of France?", 
            "What is 2 + 2?", 
            "Which planet is known as the Red Planet?", 
            "Who wrote 'Romeo and Juliet'?", 
            "What is the largest ocean on Earth?")

options =  (("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
            ("A. 3", "B. 4", "C. 5", "D. 6"),
            ("A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"),
            ("A. William Shakespeare", "B. Charles Dickens", "C. J.K. Rowling", "D. Mark Twain"),
            ("A. Pacific Ocean", "B. Atlantic Ocean", "C. Indian Ocean", "D. Arctic Ocean"))

answers = ("A", "B", "A", "A", "A")
guesses =[]
score = 0
question_num = 0

for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): " ).upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("You are right!")
    else:
        print(f"Incorrect. The right answer is {answers[question_num]}")
    print()
    question_num += 1
print(f"Congrats!\nTotal number is: {score}\n")
print(f"Here is your percentage: {score/len(answers) *100:2}%")

print("------------------------")
print("         ANSWERS        ")
print("------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end= " ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end= " ")
print()