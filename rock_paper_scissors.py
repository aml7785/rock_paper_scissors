import random

def rock_paper_scissors():
    list = ['rock', 'paper', 'scissors']
    computer_pick = random.choice(list)
    computer_score = 0
    user_score = 0
    play = 'yes'
    while play.lower() == 'yes':
        user_choice = input("Rock, paper, scissors (Earn 10 points if you win): ")
        user_choice = user_choice.lower()
        if user_choice not in list:
            user_choice = input("Rock, paper, scissors: ")
        if user_choice == 'rock' and computer_pick == 'paper':
            computer_score += 10
            print("Sorry, you lost this round")
        elif user_choice == 'rock' and computer_pick == 'scissors':
            user_score += 10
            print("You won!")
        elif user_choice == 'rock' and computer_pick == 'rock':
            print("It's a tie!")
        elif user_choice == 'paper' and computer_pick == 'rock':
            user_score += 10
            print("You won!")
        elif user_choice == 'paper' and computer_pick == 'scissors':
            computer_score += 10
            print("Sorry you lost this round")
        elif user_choice == 'paper' and computer_pick == 'paper':
            print("It's a tie!")
        elif user_choice == 'scissors' and computer_pick == 'paper':
            user_score += 10
            print("You won!")
        elif user_choice == 'scissors' and computer_pick == 'rock':
            computer_score += 10
            print("Sorry you lost this round")
        else:
            print("It's a tie!")
        print("Your score is: " + str(user_score))
        print("Computer score is: " + str(computer_score))
        play = input("Do you want to play again? ")