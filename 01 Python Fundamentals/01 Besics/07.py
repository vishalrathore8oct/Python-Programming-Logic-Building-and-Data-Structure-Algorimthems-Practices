'''
Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.

Given:

str_x = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times
'''

user_str = "Emma is good developer. Emma is a writer"

fint_str = input("Enter the finding string = ")

print(user_str.count(fint_str))
