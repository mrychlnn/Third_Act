#PROG_02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if num1 != num2:
    print ("The inserted number are NOT EQUAL.")
else: 
    print ("Both numbers are EQUAL.")

