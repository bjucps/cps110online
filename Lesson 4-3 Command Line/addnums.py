# File: addnums.py
import sys

if len(sys.argv) != 3:
   print('Please supply two numbers.')
   print('Usage: python addnums.py <num1> <num2>')
   exit()

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

sum = num1 + num2
print("Sum of", num1, "and", num2, "is:", sum)

