def main():

    print('Hello. I am an addition calculator')
    number1 = input ('Please provide me the first number to add')                                                                             # Requesting first number
    number2 = input ('Please provide me the second number to add')                                                                            # Requesting second number
    sum = float(number1) + float(number2)                                                                                                     # Adding numbers user provided.
    if (sum >= 100):
        restart=input('They add up to ' + str(sum) + '. They add up to a big number. Would you like to try another two numbers?').lower()     # Allow user to check other numbers.
        if restart.startswith('y'):
            main()
        else:
            exit()
    else:
        restart=input('They add up to ' + str(sum) + '. Would you like to try another two numbers?').lower()                                   # Allow user to check other numbers.
        if restart.startswith('y'):
            main()
        else:
            exit()
main()
