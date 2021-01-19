import random
#BahaEddineChouari,TP2,2LM2
while True:
    Player_action = input("Select a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    AI_action = random.choice(possible_actions)
    print(f"\nYou chose {Player_action}, AI chose {AI_action}.\n")

    if Player_action == AI_action:
        print(f"You and the AI have selected the same choice which is {Player_action}. It's a tie!")
    elif Player_action == "rock":
        if AI_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif Player_action == "paper":
        if AI_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif Player_action == "scissors":
        if AI_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    Try_again = input("Do you want to try again? (yes/no): ")
    if Try_again.lower() != "yes":
        break
