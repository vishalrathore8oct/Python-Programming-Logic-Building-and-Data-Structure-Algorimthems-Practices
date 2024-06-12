'''
Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*
'''

for i in range(1, 6):
    for j in range(1, 6):
        if i <= j:
            print("*", end=" ")
    print()