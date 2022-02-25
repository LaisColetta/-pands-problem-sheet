# Program that generates a random number between 0 and 100 to guess
#Author: Lais

import random

a = (input('Please guess a random number: '))
randomnumber = random.randint(0, 100)

while a != randomnumber:
    a = (input('Wrong\nPlease guess again: '))

print ('Well done! The number is {}' .format (a))