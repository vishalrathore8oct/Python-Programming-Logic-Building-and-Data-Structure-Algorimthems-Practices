'''
Exercise 1: Calculate the multiplication and sum of two numbers

Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

Given 1:

number1 = 20
number2 = 30

Expected Output:

The result is 600

Given 2:

number1 = 40
number2 = 30

Expected Output:

The result is 70
'''

num1 = int(input("Enter the first number = "))
num2 = int(input("Enter the second number = "))

if (num1 * num2) <= 1000:
    print("The result is", num1 * num2)
else: 
    print("The result is", num1 + num2)

