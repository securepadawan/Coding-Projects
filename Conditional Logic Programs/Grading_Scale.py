def main():

    print('Hello. I am grade percentage to letter grade converter')
    grade = input ('Please type your grade percentage:')
    if (grade >= str(93)):
        restart=input('A+           Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(90)):
        restart=input('A-           Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(87)):
        restart=input('B+           Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(83)):
        restart=input('B            Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(80)):
        restart=input('B-           Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(77)):
        restart=input('C+           Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(73)):
        restart=input('C            Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(70)):
        restart=input('C-           Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(67)):
        restart=input('D+           Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(63)):
        restart=input('D            Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade >= str(60)):
        restart=input('D-           Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
    elif (grade < str(60)):
        restart=input('F            Would you like to check another grade?').lower()     # Allow user to check another grade.
        if restart.startswith('y'):
            main()
        else:
            exit()
main()
