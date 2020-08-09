# Programming with Lists
### Comma Code

Say you have a list value like this:

    listToPrint = ['apples', 'bananas', 'tofu', 'cats']

Write a program that prints a list with all the items separated by a comma and a space, with and inserted before the last item. For example, the above list would print 'apples, bananas, tofu, and cats'. But your program should be able to work with any list not just the one shown above. Because of this, you will need to use a loop in case the list to print is shorter or longer than the above list. Make sure your program works for all user inputs. For instance, we wouldn't want to print "and" or commas if the list only contains one item.

You can use the following code to start your program. It will let the user type a list

    listToPrint = []
    while True:
        newWord = input("Enter a word to add to the list (press return to stop adding words) > ")
        if newWord == "":
            break
        else:
            listToPrint.append(newWord)

### Backpack of stuff

Complete the following code. Fill in the two sections of code identified in the comments.

    import sys

    itemsInBackpack = ["book", "computer", "keys", "travel mug"]

    while True:
        print("Would you like to:")
        print("1. Add an item to the backpack?")
        print("2. Check if an item is in the backpack?")
        print("3. Quit")
        userChoice = input()
    
        if(userChoice == "1"):
            print("What item do you want to add to the backpack?")
            itemToAdd = input()
        
            ####### YOUR CODE HERE ######
            #add the item to the backpack
            ####### YOUR CODE HERE ######
        
        if(userChoice == "2"):   
            print("What item do you want to check to see if it is in the backpack?")
            itemToCheck = input()
        
            ####### YOUR CODE HERE ######
            #Print out if the user's item is in the backpack
            ####### YOUR CODE HERE ######
    
        if(userChoice == "3"): 
            sys.exit()

### Character Picture Grid

Say you have a list of lists where each value in the inner lists is a one-character string, like this:

    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

You can think of grid[x][y] as being the character at the x- and y-coordinates of a “picture” drawn with text characters. The (0, 0) origin will be in the upper-left corner, the x-coordinates increase going right, and the y-coordinates increase going down.

Copy the previous grid value, and write code that uses it to print the image.

    ..OO.OO..
    .OOOOOOO.
    .OOOOOOO.
    ..OOOOO..
    ...OOO...
    ....O....

Hint: You will need to use a loop in a loop in order to print grid[0][0], then grid[1][0], then grid[2][0], and so on, up to grid[8][0]. This will finish the first row, so then print a newline. Then your program should print grid[0][1], then grid[1][1], then grid[2][1], and so on. The last thing your program will print is grid[8][5].

Also, remember to pass the end keyword argument to print() if you don’t want a newline printed automatically after each print() call.  For instance if you wrote:

    print("Hello World", end="")
    print("Hello")

It would print out the first command without a newline at the end of it:

    Hello WorldHello

### Comments:
This was a assignment I had to create for my CMIT-135 class at Champlain College.
