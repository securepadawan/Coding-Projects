def main():                                                             #Loop Command to restart script if user types incorrect input.

    print('Hello. I am the age verification system for the 2019 National Election Day (November 5th, 2019). You must be 18 years old before election day.')
    verification = input('Please type "birth date" or "age" for verification').lower()
    if verification.lower() == 'birth date':
        import datetime
        election = datetime.date(2019, 11, 5)
        dob_str = input("What is your Date of Birth? mm/dd/yyyy")       # Verification via birthday
        dob_data = dob_str.split("/")                                   # Convert user input into a date
        dobMonth = int(dob_data[0])
        dobDay = int(dob_data[1])
        dobYear = int(dob_data[2])
        dob = datetime.date(dobYear,dobMonth,dobDay)
        numberOfDays = (election - dob).days                            # Calculate number of days lived
        day_in_year = 365.2425
        b_age = int(numberOfDays // day_in_year)                        # Convert this into whole years to display the age
        if(b_age >= 18):
                print("You are " + str(b_age) + " years old. You are of voting age")
        else:
                print("You are " + str(b_age) + " years old. You must be 18 to vote")

    elif verification.lower() == 'age':
        print('Please enter your current age')                          # Verification via age
        age = int(input())
        if (age >= 18):
            print('You are of voting age')
        else:
            print ('You must be 18 to vote. Depending on your birth date, you may be old enough.') # Even though the user may be 18 today, depending on birth date, they still may be able to vote.
            import datetime
            election = datetime.date(2019, 11, 5)
            dob_str = input("What is your Date of Birth? mm/dd/yyyy")   # Verification via birthday
            dob_data = dob_str.split("/")                               # Convert user input into a date
            dobMonth = int(dob_data[0])
            dobDay = int(dob_data[1])
            dobYear = int(dob_data[2])
            dob = datetime.date(dobYear,dobMonth,dobDay)
            numberOfDays = (election - dob).days                        # Calculate number of days lived
            days_in_year = 365.2425
            age = int(numberOfDays // days_in_year)                     # Convert this into whole years to display the age
            if(age >= 18):
                print("You will be " + str(age) + " years old on election day. You are of voting age")
            else:
                print("You will be " + str(age) + " years old on election day. You must be 18 to vote")

    else:
        restart=input('This is not a correct response. Do you wish to start again?').lower() # Invalid input by user. Allows user to restart and end script.
        if restart.startswith('y'):
            main()
        else:
            exit()
main()



