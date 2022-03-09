# Program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.

#Author: Lais
#References:https://www.w3schools.com/python/python_while_loops.asp, https://realpython.com/lessons/while-loops/

#Create variable for the while loop
value = (input('Please enter a positive number: '))

#While loop: Value is different than one, if even, divide it by 2, if odd, multiply it by three and add one.
#Notes: Result value has to be entered after 'print' to work for the next round of calculations.
while value !=1:
    if (value % 2 == 0):
        print ('{} is an even number and divided by 2 is: {}'.format((value),(value /2)))
        value = float(value/2)

    else:
        print ('{} is an odd number and multiplied by 3 + 1 is: {}'.format((value),(value*3+1)))
        value = float((value*3)+1)
    
#If value is 1, the program will end.
print ( 'The program ended, number one has been entered')
    






