import sys

itemsInBackpack = ["book", "computer", "keys", "travel mug"]

while True:
    print("Would you like to:")
    print("1. Add an item to the backpack?")
    print("2. Check if an item is in the backpack?")
    print("3. Quit")
    userChoice = input()

    if (userChoice == "1"):
            print("What item do you want to add to the backpack?")
            itemToAdd = input()
            if itemToAdd == "":                                                                                                     # Add's user's entry into backpack.
                break
            else:
                itemsInBackpack.append(itemToAdd)
    if (userChoice == "2"):
            print("What item do you want to check to see if it is in the backpack?")
            itemToCheck = input()
            if itemToCheck in itemsInBackpack:
                    print('Yes! ' + itemToCheck + ' is inside your backpack. Here is the full list of contents in your backpack: ')# Lets user know item is in backpack.
                    for item in itemsInBackpack[:-1]:
                            print(item, end=', ')
                    print ('and', itemsInBackpack[-1])
            else:
                    addNewItem = input("Sorry! " + itemToCheck + " isn't in your backpack. Would you like to add it?")                                          # If items isn't in backpack, it allows the user to add to backpack
                    if addNewItem.startswith('y'):
                        itemsInBackpack.append(itemToCheck)
                        print(itemToCheck + ' has been added to your backpack. Here is a full list of all items inside your backpack: ') # If user doesn't have item in backpack, allows them to add. Then prints full list of items in backpack
                        for item in itemsInBackpack[:-1]:
                                print(item, end=', ')
                        print ('and', itemsInBackpack[-1])
    if (userChoice == "3"):
            sys.exit()
