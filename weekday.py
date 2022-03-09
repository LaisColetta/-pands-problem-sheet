#Program that checks if today is a weekday/weekend day
#Author: Lais
#Reference: https://www.tutorialsrack.com/articles/324 / YouTube video: Datetime Module (Dates and Times) || Python Tutorial || Learn Python Programming
  
# Import Module
import datetime

# weekday() function to get the week number from the date
weekNumber = datetime.datetime.today().weekday()

#check if the week number is greater than 5 then its a weekend otherwise it is a weekday.
if weekNumber < 5:
    print("Yes, unfortunately today is a Weekday".format(datetime.datetime.today()))
else:
    print ("It is the weekend, yay!".format(datetime.datetime.today()))











