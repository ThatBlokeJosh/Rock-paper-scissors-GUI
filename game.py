import random
list = []

def game(choice):
    choices = ["rock", "paper", "scissors"]
    computer = choices[random.randint(0, 2)]
    list.append(computer)
    player = choice
    if player == computer:
        return "tie"
    elif player == "rock":
        if computer == "paper":
            return "lose"
        else:
            return "win"
    elif player == "paper":
        if computer == "scissors":
            return "lose"
        else:
            return "win"
    elif player == "scissors":
        if computer == "rock":
            return "lose"
        else:
            return "win"
def returncomputer():
    return list[-1]
