#Program to count letter 'e' in a text file
#Author: Lais
#Reference: www.geeksforgeeks.org,https://docs.python.org/3/library/functions.html#open, https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-7.php

# We start by creating a function that reads the file:
def letterFrequency(fileName, letter):
    # open file in read mode
    file = open(fileName, "r")
    # store content of the file in a variable
    text = file.read()
    #count variable (as we did in Lab07.02)
    count = 0
    for character in text:
        #check if character contains the given letter
        if character == letter:
            count += 1
            
    # return letter count
    return count

# call function and display the letter count
print(letterFrequency('week06-WeeklyTask.py', 'e'))