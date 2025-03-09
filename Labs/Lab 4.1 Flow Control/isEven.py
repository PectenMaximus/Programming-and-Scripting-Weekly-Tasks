# Code that promts user to input a number and tells user if it is even 

number = int(input("Enter a number: "))
if (number % 2) == 0: 
    print(f"{number} is even")
else:
    print(f"{number} is odd")
