'''
Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

Expected Output:

Orginal String is  pynative
Printing only even index chars

p
n
t
v
'''

user_str = input("Enter the string = ")

for i in range(0, len(user_str), 2):
    print(user_str[i])
    