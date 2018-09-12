print ('bmi calculation')
x = float (input('enter your height in meters:'))
y = float (input('enter your weight in kgs:'))

BMI = y/(x**2)
print('BMI:')
print(BMI)
if BMI<=18.50:
	print ('poor , eat more')
if BMI>18.50 and BMI<24.99:
	print ('normal')	


