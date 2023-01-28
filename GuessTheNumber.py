n = 18

numberOfGuesses = 9

print("Guess the number hidden in the code to win this game within 9 tries. Guess the number between 0 to 20")

while numberOfGuesses>=0:
    Guesses = input("Enter you guess number : ")
    if int(Guesses) < n:
        print("Increase your number")
    elif int(Guesses) > n:
        print("Decrease your number")
    elif int(Guesses) == n:
        print("you won the game in " + str(numberOfGuesses) + " Tries")
        break
    else:
        print("invalid input")

    if numberOfGuesses == 0:
        print("No Guesses Left - Game Over")
        break
    numberOfGuesses = numberOfGuesses - 1
    print(str(numberOfGuesses) + " Chances left")