#Program that that calculates somebody's Body Mass Index (BMI)
#Author: Lais

#input weight - create the variable 'weight'
weight = float(input('Enter your weight (kg): '))
#input height - create the variable height
height = float(input('Enter you height (cm): '))
#use the variables to calculate the BMI. The calculation was based on the article https://www.dummies.com/ that teaches how to calculate an individuals BMI.
result = round(weight/(height*height),2)

#print result. Use .format to format the value in the string and avoid syntax error.
print ('The BMI is (kg/m2) = {}' .format(result))


