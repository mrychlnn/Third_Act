#PROG_07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

even = 0

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        even += 1

print (f"\nThe number of even numbers is {even}")