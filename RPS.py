import random

player_sorce = 0
computer_sorce = 0

while True:

    #Player Part
    player_input = input("Enter your input: Rock, Paper, Scissor: ")

    print(f'You have selected {player_input}')

    #Computer input part

    computer_random = random.randint(1,3)

    if computer_random == 1:
        computer_input = "Rock"
    elif computer_random == 2:
        computer_input = "Paper"
    else:
        computer_input = "Scissor"
    print(f'Computer selected {computer_input}')

    if player_input == "Rock":
        if computer_input == "Rock":
            print("Tied")
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')
        elif computer_input == "Paper":
            print("Computer Wins")
            computer_sorce = computer_sorce + 1
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')
        else:
            print("Player Wins")
            player_sorce = player_sorce + 1
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')

    elif player_input == "Paper":
        if computer_input == "Paper":
            print("Tied")
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')
        elif computer_input == "Rock":
            print("Player wins")
            player_sorce = player_sorce + 1
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')
        else:
            print("Computer wins")
            computer_sorce = computer_sorce + 1
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')

    elif player_input == "Scissor":
        if computer_input == "Paper":
            print("Player wins")
            player_sorce = player_sorce + 1
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')
        elif computer_input == "Rock":
            print("Computer wins")
            computer_sorce = computer_sorce + 1
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')
        else:
            print("Tied")
            print(f'Scores:  computer:{computer_sorce} , player:{player_sorce}')
    #sorces
    if computer_sorce == 10:
        print("Computer wins the game!")
        break
    elif player_sorce == 10:
        print("Player wins the game!")
        break