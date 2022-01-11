numberofLives = 3
secretNumber = 9

while numberofLives > 0:
    guessedNumber = int(input("Guess a number between 0-9: "))
    numberofLives -= 1
    if guessedNumber == secretNumber:
        print("You have guessed the correct number. ")
        break
    else:
        print(f"You have {numberofLives} lives left. ")
else:
    print("You have failed .. Please try again. ")