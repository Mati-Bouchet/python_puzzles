import random

coin = ["heads", "tails"]

def player_choice():
    player_choice = input("Please enter your choice: ")
    return player_choice

def flip_coin():
    return random.choice(coin)

def check_win(player, flip):
    if player == flip:
        print("You win")
    else:
        print("You lost")

my_choice = player_choice()

flip = flip_coin()

print(f"Your choice: {my_choice}")
print(f"Flip: {flip}")
check_win(my_choice, flip)