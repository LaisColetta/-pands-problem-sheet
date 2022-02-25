# In practice the percentages are rounded ie 69.5 gets rounded to 70 so is equal to a Distinction.
# How would you modify the program in 1 to deal with this? I see two ways.

a = int(input('Enter a number: '))
rounded = round(a)
if rounded%2 == 0:
    print ('{} is even'.format(rounded))
else:
    print ("{} is odd".format(rounded))

#How would you use a while loop to modify 1 so that it keeps prompting the user for a number until the user enters -1:
a = int(input('Enter a number: '))
while a!=(-1):
    a = (input('Enter another number: '))
print ('Well done, the  correct number is {}'.format (a))
