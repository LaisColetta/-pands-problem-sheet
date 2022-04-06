#Program that takes a positive floating-point number as input and outputs an approximation of its square root.
#Author: Lais

#create a function that returns an aprox square root. We will run Newton's method many times until we get a close enough result.
#set the error parameter that we would like to work on as a default and that will be considered 'acceptable'(0.00001)
def sqrt(num, error=0.00001):
    # variable for the first guess = num
    guess = num
    #calculate a difference that is going to be used to measure against the error rate paramater set previously.
    diff2 = 999999
    #while loop to keep repeting formula and improving our guess until it meets the level of error level we set.
    while diff2>error:
        #newton's method formula:
        newGuess = guess - ((guess**2 - num)/ (2* guess))
        #calculate the error. use ABS function to take the absolute value in case it is a negative value. 
        diff1 = (newGuess - guess)
        diff2 = abs(diff1)
        
    #If the different is still too big (bigger than 'error') the loop will continue, otherwise it ends.
        guess = newGuess
    return guess

a = (input('Please enter a positive number: '))
b = sqrt(float(a))
print ('The square root of {} is approx. {}'.format(a,b))


