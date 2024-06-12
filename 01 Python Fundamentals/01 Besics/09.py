'''
Exercise 9: Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. For example, 545, is the palindrome numbers

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
'''

usr_num = int(input("Enter your number = "))
final_result = usr_num
reverse_num = 0

while usr_num != 0: 
    reverse_num = (reverse_num * 10) + (usr_num % 10)
    usr_num = usr_num // 10

if final_result == reverse_num:
    print("Yes. given number is palindrome number")
else:
    print("No. given number is not palindrome number")