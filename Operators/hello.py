# Simple operators
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # two stars are used for exponentiation (2 to the power of 16)
print(37 / 3)  # single forward slash is a division
print(37 // 3)  # double forward slash is an integer division
        # it returns only the quotient of the division (i.e. no remainder)
print(37 % 3)  # percent sign is a modulus operator
        # it gives the remainder of the left value divided by the right value
#Implementing user input
print('What is your name?')
name = input()  # read a single line and store it in the variable "name"
print('Hi ' + name + '!')

a = input() #interprets user input as a string
b = input()
s = a + b
print(s) #this will just concat user input. If you are expecting an int you must do the following...

a = int(input())
b = int(input())
s = a + b
print(s)

#   Calculate the Simple Interest
#
#   The formula for Simple Interest is
#   si = principal * interest rate * number of years
#   where si is the simple interest

p = 18819.99    # principal
r = 0.05        # rate of interest
t = 2           # years

si = p * r * t
print("Simple interest at the end of 2 years $", format(si, "0.2f")) # format(value, format-specifier) 0 is width (total space) is automaitcally increased as needed. 2 is to what decimal point. If you want scientific notation you can replace the 'f' with 'e' or 'E'. Add ',' before precision to add commas to make large numbers more readable
print(format(98813343817.7129, ",.2f"))
98,813,343,817.71 
#   Type codes d, b, o, x can be used to format in decimal, binary, octal and hexadecimal respectively