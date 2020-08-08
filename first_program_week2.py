print('Halt!! I am the Knight of First Python Program!. He or she who would open my program must answer these questions!')
Ready = input('Are you ready?').lower()
if Ready.startswith('y'):
    print('Great, what is your name?') # ask for their name
else:
    print('Run me again when you are ready!')
    exit()
myName = input()
if myName.lower() == 'jamie martin':
    print('Well hello, Professor Martin! I hope you enjoy Month Python puns!') # special greeting for Professor.
elif myName.lower() == 'ian ince':
    print('All Hail The Creator!') #special greetings for Creator
else:
    print('Nice to meet you, ' + myName + '!')

print('What is your quest? (degree program at Champlain College?)') # ask for their degree
degree = input()
if degree == 'Cybersecurity':
    print('My creator as well!')
elif degree == "i don't know":
    print("Don't me get the Black Knight. He's invincible and may bleed on you.") #insert pun here
else:
    print('I bet a lot of people are interested in ' + degree)

print('What is your favorite color?') # ask for their favorite color
color = input ()
if color.lower () == 'green':
    print('Speaking of green.... Bring me..... A Shrubbery!')
else:
    print(color + ' is a nice color')

print('How many kids do you have?') #ask if have kids
kid = input ()
if kid == '0':
    print("Don't be a DINK! (double income no kids). Kids makes life interesting! This means you only have " + str(int(kid)+1) + ' or ' + str(int(kid)+2) + " (if you have a spouse) in your immediate family.")
    exit()
if kid == '1':
    print('Nice! Does your child also enjoy the color ' + color + '?') #ask if kid have like same color
else:
    print('Nice! Does any of your ' + kid + ' children enjoy the color ' + color + '?')

likecolor = input ()
if likecolor.startswith('y'):
    print('Great! You have something in common in your family of ' + str(int(kid)+1) + ' or ' + str(int(kid)+2) + ' (if you have a spouse).') #add parent and kid's age
else:
    print('Well that stinks! I hope your family of ' + str(int(kid)+1) + ' or ' + str(int(kid)+2) + ' (if you have a spouse) have something else in common.' )

print('I will now ride off in the sunset with my coconuts. Now for something completely different. Goodbye!')
