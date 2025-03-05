#PROG_06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

num1 = float(input("Enter number 1: "))
answer = num1

for i in range (2,11):
    num = float(input(f"Enter number {i}: "))
    answer -= num

print(f"\nThe result is {answer:.2f}")