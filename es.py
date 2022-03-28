#Program to count letter 'e' in a text file
#Author: Lais

# We start by creating a function called letterFrequency that reads the file and inputs the filename in the commandline as an argument:
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

# call function and display the letter count and add file source. in this case I chose the file 'bmi.py' to search for the letter 'e'.
print(letterFrequency('bmi.py', 'e'))