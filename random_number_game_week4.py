def main():
    from random import randint
    randomNum = randint(1,100)
    guessesTaken = 0
    print("Hello! I am a random number guessing game. I am thinking of a number 1-100. You have infinite changes to get it right. Please guess a number.")
    while guessesTaken < float('inf'):                                                                                                              # Infinite Guesses
        guess = input()
        guess = int(guess)

        guessesTaken = guessesTaken + 1

        if guess < randomNum:
            print('Higher')                                                                                                                         # Informing user to go higher
        if guess > randomNum:
            print('Lower')                                                                                                                          # Informing user to go lower
        if guess == randomNum:
            break
    if guess == randomNum:
        guessesTaken = str(guessesTaken)
        restart=input('Congrats! You guessed my number! It only took you ' + guessesTaken + ' guesses!. Would you like to play again?').lower()     # Allow user to play again.
        if restart.startswith('y'):
            main()
        else:
            exit()
    if guess != randomNum:
        randomNum = str(randomNum)
        restart=input('Sorry! You guessed incorrectly. My number was ' + randomNum +  '. Would you like to play again?').lower()                   # Allow user to play again.
        if restart.startswith('y'):
            main()
        else:
            exit()
main()
