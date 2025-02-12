# This program reads in two numbers and output the interger answer and the remainder

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
ans = int (x//y) # // is used to divide and return the integer value
remainder = x % y # % is used to return the remainder

print("{} divided by {} is {} with remainder {}".format(x, y, ans, remainder))