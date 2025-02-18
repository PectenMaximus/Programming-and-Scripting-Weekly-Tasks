# Prints out a students grade based on their percentage

grade = float(input("Enter your grade in percentage: "))

if grade >= 70:
    print("Distinction")
elif grade >= 60 and grade < 70:
    print("Merit")
elif grade >= 50 and grade < 60:
    print("Pass")
elif grade >= 40 and grade < 49:
    print("Refer")
else:
    print("Fail")
