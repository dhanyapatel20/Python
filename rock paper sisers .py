import random
while True:
    user_choice = input("enter your choice (rock,paper or sissors): ")
    possible_choises = ["rock", "paper", "sissors"]
    computer_choice = random.choice(possible_choises)
    print(f"you chose {user_choice}, computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("it's a tie!")
    elif user_choice == "rock" and computer_choice == "sissors":
        print("you win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("you win!")
    elif user_choice == "sissors" and computer_choice == "paper":
        print("you win!")
    else:
        print("you lose!")
    play_again = input("do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break