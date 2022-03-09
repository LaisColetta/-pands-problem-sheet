#Write a program that asks a user to input a string and outputs every second letter in reverse order.
#Author: Lais
#References: https://realpython.com/reverse-string-python/, https://stackoverflow.com/

#$ python secondstring.py
#Please enter a sentence: The quick brown fox jumps over the lazy dog.
#.o zletrv pu o wr cu h

string = (input('Please enter a sentence: '))
# create a string with characters at multiples of 2
secondletter = (string[::2])

#print second letter reversed:
print (secondletter [::-1])

