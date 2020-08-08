listToPrint = []
while True:
    newWord = input("Enter a word to add to the list. After each word, please hit Enter. Once completed, hit Enter again.")
    if newWord == "":               #allow user's to type word to add to list
        break
    else:
        listToPrint.append(newWord)         #add's input to the list
print("Here is your list:")    #shows list enter by user
for item in listToPrint[:-1]:
    print(item, end=', ')
print('and', listToPrint[-1])
