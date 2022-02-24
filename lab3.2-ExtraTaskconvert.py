#Write a program that takes in a float amount of dollars, and returns that absolute amount in cent.
#Author: Lais

amount = float(input ('Enter amount '))
inCents = (abs(amount))*100
rounded = int(inCents)
print ('The {} amount in cents is {}'.format(amount,rounded))
