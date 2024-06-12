'''
Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
'''

usr_num = int(input("Enter your number = "))
reverse_num = ""

while usr_num != 0: 
    reverse_num += " " + str(usr_num % 10)
    usr_num = usr_num // 10

print(reverse_num)

