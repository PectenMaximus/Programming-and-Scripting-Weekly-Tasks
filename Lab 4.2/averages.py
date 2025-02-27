# This programme keeps reading numbers until the user enters a 0.
# This programme gets the adverage of all the numbers the reader before entering 0.

numbers = []

number = int (input('Please Enter a number '))

while number != 0:
    number.append(number)
    number = int(input)('Enter a numer - 0 to quit)')

for value in numbers:
    print (value)

average = float (sum(numbers))/len(numbers)
print (f'the average is {average}')