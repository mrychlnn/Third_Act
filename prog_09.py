#PROG_09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

print("The numbers from 0 to 100 w/o number ends with zero and five are: ")
for num in range(101):
    if num % 5 != 0:
        print (num)