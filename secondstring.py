#Write a program that asks a user to input a string and outputs every second letter in reverse order.
#Author: Lais

#create a variable asking the user to input sentence
string = (input('Please enter a sentence: '))
#create a string that prints the every other character from the first letter to the end - [start:stop:step]. Step = 2 because it is printing every second letter from the start.
secondletter = (string[1::2])

#print variable 'second letter' reversed. Slicing: [from 0, to end, -1 (reversed)]:
print (secondletter[::-1])
