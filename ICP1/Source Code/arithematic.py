num1String = input('Enter first number: ')
num2String = input('Enter second number: ')

num1 = float(num1String)
num2 = float(num2String)

# Ask for the input again if zero was second number
if num2 == 0.0:
    num2String = input('Please enter a number besides zero:')
    num2 = float(num2String)

# Performing Arithmetic Operations
addnum = num1+num2
subnum = num1-num2
multnum = num1*num2
divnum = num1 / num2

# Displaying results and limiting decimal points to 2 decimal places
print('Sum of the numbers', "%.2f" % addnum)
print('Difference of 2 numbers', "%.2f" % subnum)
print('Multiplication of 2 numbers', "%.2f" % multnum)
print('The first number divided by the second number', "%.2f" % divnum)