import random

print("HELLO, WELCOME TO ROCK-PAPER-SCISSORS GAME")

username = input("Enter Your Name Here To Start The Game: ")
user_score = 0
computer_score = 0
max_attempts = 5
attempts = 0

print('''
Rules to follow:-
1. Rock vs Scissors -> Rock
2. Scissors vs Paper -> Scissors
3. Paper vs Rock -> Paper
''')

while attempts < max_attempts:
    print(f"\nScores: {username}: {user_score} | Computer: {computer_score}")

    userinput = input("\nEnter a choice (Rock, Paper, Scissors) or 'quit' to exit: ").capitalize()
    if userinput == 'Quit':
        print("Thank you for playing. Goodbye!")
        break

    possible_outcomes = ["Rock", "Scissors", "Paper"]
    computerinput = random.choice(possible_outcomes)

    print(f"\nYou Have Chosen {userinput}, Computer Has Chosen {computerinput}.\n")

    if userinput == computerinput:
        print(f"Both players have selected the same option {userinput}. It's a tie!")
    elif userinput == "Paper":
        if computerinput == "Rock":
            print("Paper wraps Rock. You have won this round!")
            user_score += 1
        else:
            print("Scissors cut Paper. You have lost this round!")
            computer_score += 1
    elif userinput == "Rock":
        if computerinput == "Scissors":
            print("Rock crushes Scissors. You have won this round!")
            user_score += 1
        else:
            print("Paper covers Rock. You have lost this round!")
            computer_score += 1
    elif userinput == "Scissors":
        if computerinput == "Paper":
            print("Scissors cut Paper. You have won this round!")
            user_score += 1
        else:
            print("Rock crushes Scissors. You have lost this round!")
            computer_score += 1

    attempts += 1

if user_score > computer_score:
    print(f"\nCongratulations {username}! You won the game with {user_score} points!")
elif user_score < computer_score:
    print(f"\nSorry, the computer won the game with {computer_score} points. Better luck next time!")
else:
    print("\nThe game ended in a tie!")