import random

options = ["rock", "paper", "scissors"]  # This is a list


def get_choices():
    player_choice = input("Enter a choice: rock, paper, scissors ")
    computer_choice = random.choice(options)
    game_choices = {"player": player_choice, "computer": computer_choice}
    return game_choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors. You win!"
        else:
            return "Paper wraps rock. You lose!"
    elif player == "paper":
        if computer == "scissors":
            return "Scissors cut paper. You lose!"
        else:
            return "Paper wraps rock. You win!"
    elif player == "scissors":
        if computer == "rock":
            return "Rock smashes scissors. You lose!"
        else:
            return "Scissors cut paper. You win!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])

print(result)