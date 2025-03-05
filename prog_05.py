#PROG_05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

rem = num1 % num2
print (f"The remainder of two numbers is {rem:.0f}")