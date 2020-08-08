#date2 - date1 = timedelta
import datetime
election = datetime.date(2019, 11, 5)

dob_str = input("What is your Date of Birth? mm/dd/yyyy")
#Convert user input into a date
dob_data = dob_str.split("/")
dobMonth = int(dob_data[0])
dobDay = int(dob_data[1])
dobYear = int(dob_data[2])
dob = datetime.date(dobYear,dobMonth,dobDay)

#Calculate number of days lived
numberOfDays = (election - dob).days

#Convert this into whole years to display the age
age = numberOfDays // 365
print("You are " + str(age) + " years old.")
