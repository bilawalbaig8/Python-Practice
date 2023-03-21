import random

lst = ["Rock", "Paper", "Scissor"]

choice = ""
quite = ''
player_Score = 0
opponent_Score = 0

while quite.capitalize() != "Q" or quite.capitalize() != "QUITE":
    print("select any of the following")

    choice = input("Press 'R' for 'Rock'\n"
                   "Press 'P' for 'Paper'\n"
                   "Press 'S' for 'Scissor'\n")

    opponent = random.choice(lst)

    if choice.capitalize() == 'R' and opponent == 'Rock':
        print("Player selection : Rock")
        print("Opponent selection : ", opponent)
        print("\n Match Draw")

    elif choice.capitalize() == 'R' and opponent == 'Paper':
        print("Player selection : Rock")
        print("Opponent selection : ", opponent)
        print("\n You Lose")
        opponent_Score = opponent_Score + 1

    elif choice.capitalize() == 'R' and opponent == 'Scissor':
        print("Player selection : Rock")
        print("Opponent selection : ", opponent)
        print("\n You Win")
        player_Score = player_Score + 1

    elif choice.capitalize() == 'P' and opponent == 'Paper':
        print("Player selection : Paper")
        print("Opponent selection : ", opponent)
        print("\n Match Draw")

    elif choice.capitalize() == 'P' and opponent == 'Scissor':
        print("Player selection : Paper")
        print("Opponent selection : ", opponent)
        print("\n You Lose")
        opponent_Score = opponent_Score + 1

    elif choice.capitalize() == 'P' and opponent == 'Rock':
        print("Player selection : Paper")
        print("Opponent selection : ", opponent)
        print("\n You Win")
        player_Score = player_Score + 1

    elif choice.capitalize() == 'S' and opponent == 'Scissor':
        print("Player selection : Scissor")
        print("Opponent selection : ", opponent)
        print("\n Match Draw")

    elif choice.capitalize() == 'S' and opponent == 'Rock':
        print("Player selection : Scissor")
        print("Opponent selection : ", opponent)
        print("\n You Lose")
        opponent_Score = opponent_Score + 1

    elif choice.capitalize() == 'S' and opponent == 'Paper':
        print("Player selection : Scissor")
        print("Opponent selection : ", opponent)
        print("\n You Win")
        player_Score = player_Score + 1

    else:
        print("Input is invalid")

    quite = input("Press Q to Quite Or C to Continue")
    if quite.capitalize() == "Q":
        print("\nPlayer score is : ", player_Score)
        print("Opponent score is : ", opponent_Score)
        break
