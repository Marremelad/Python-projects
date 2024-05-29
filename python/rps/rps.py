import random

def main():
    while True:
        cpu, player = choices()
        print(winner(cpu, player))

def choices():

    choice = {"paper": 1,
              "scissors": 2,
              "rock": 3,
              }

    cpu = random.choice(list(choice))

    if choice[cpu] == 3:
        choice["paper"] = 4

    print("Make your choice")
    while True:
        player = input().lower()
        if player in choice:
            break
        else:
            print("Not a valid choice")

    print(f"You chose {player}")
    print(f"CPU chose {cpu}")

    return choice[cpu], choice[player]

def winner(cpu, player):

    if cpu == player:
        return "Tie"
    elif cpu > player:
        return "CPU wins"
    else:
        return "Player wins"

main()

