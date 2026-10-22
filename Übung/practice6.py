#Python Calculator 
import math
operator = input("Enter an operator (+, -, * , /):")
num1 = float(input("Enter a number:"))
num2 = float(input("Enter a number:"))

#print(num1 + num2)

if operator == "+" :
    result = num1 + num2
elif operator == "-" :
    result = num1 - num2
elif operator == "*" :
    result = num1 * num2
else:
    result = num1 / num2
    
print(round(result , 3))