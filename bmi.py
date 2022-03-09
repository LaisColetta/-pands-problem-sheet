#Program that that calculates somebody's Body Mass Index (BMI). 
#Author: Lais
#References: https://www.javatpoint.com/,https://www.w3resource.com/

#Input weight
weight = float(input ('Enter your weight (kg): '))
#Input height
height = float(input('Enter you height (cm): '))
#calculation of BMI according to https://www.dummies.com/
result = round(weight/(height*height),4)

#print result:
print ('The BMI is (kg/m2) = {}' .format(result))


