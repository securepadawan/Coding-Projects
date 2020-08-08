# Programming Assignment - Loops

1. Write a program that counts down from 10. Implement your program first with a while loop.  Now implement your program with a for loop. Include both versions in your submission file.

2. Write a program that prints 2^n 2 n where n goes from 1 to 100. Print one answer per line (note: you are answering the question, how high can you count on 100 fingers). Write your program using a 'for' loop.  Reminder '**' is the operator for exponents, so for example 4**3 is 4 to the third power, or 4 * 4 * 4 which equals 64. 

E.g.

    2
    4
    8
    16
    ....

3. Extend your guessing game from last week.  Write a program that picks a random number from 1-100.  Then ask the user to guess a number. Tell the user if the answer is higher or lower than the number they guessed, or if they got the correct answer.  Allow them to guess again if they got the guess incorrect.  They should be able to guess numbers an infinite number of times until they get the correct answer, at which point your loop will end.

To generate a number from 1-100 you will need the following code at the beginning of your program:

    from random import randint
    randomNum = randint(1,100)

4. Extra Credit - 5 possible points - Write a program that generates the multiplication table for numbers 1-10. Use two for loops to complete your program. You will need to put one for loop inside of the other for loop. As an extra challenge, see if you can get the indention to look correct. So the output of your program should be:

    1  2  3  4  5  6  7  8  9
    2  4  6  8 10 12 14 16 18
    3  6  9 12 15 18 21 24 27
    4  8 12 16 20 24 28 32 36
    5 10 15 20 25 30 35 40 45
    6 12 18 24 30 36 42 48 54
    7 14 21 28 35 42 49 56 63
    8 16 24 32 40 48 56 64 72
    9 18 27 36 45 54 63 72 81

