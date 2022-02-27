#Program that takes a positive floating-point number as input and outputs an approximation of its square root.
#Author: Lais
#reference: Approximating Square Roots w/ Newton's Method - YouTube and https://codereview.stackexchange.com/questions/48725/approximating-the-square-root-using-an-iterative-method/48904#48904

#set error variable (between iterations we get a difference that is a certain amount we will consider 'good enough')
def sqrt(num, error=0.00001):
    #first guess = num
    guess = num
    diff = 999999
    while diff>error:
        #newton's method formula
        newGuess = guess - ((guess**2 - num)/ (2* guess))
        diff = newGuess - guess
        #we don't know which are bigger so take absolute of the difference
        if diff < 0: 
            diff *= -1
    #this code will keep running and each time it get a guess we will check and how much the new guess is different from the result. If the different is still to big (bigger than 'error') the loop will continue, otherwise it ends.
        guess = newGuess
    return guess

a = (input('Please enter a positive number: '))
b = sqrt(a)
print ('The square root of {} is approx. {}'.format(a,b))


