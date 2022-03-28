#Program that checks if today is a weekday/weekend day and returns a message to the user.
#Author: Lais 
  
#import the module datetime to work with dates as date objects
import datetime

#create weekNumber variable. datetime.today() method returns the current date, and the weekday() returns the day of the week as an integer. Monday is indexed as 0 and Sunday as 6.
weekNumber = datetime.datetime.today().weekday()

#check if the week number is greater than 5 then its a weekend otherwise it is a weekday.
if weekNumber < 5:
    print("Yes, unfortunately today is a Weekday".format(datetime.datetime.today()))
else:
    print ("It is the weekend, yay!".format(datetime.datetime.today()))











