# This programme keeps reading numbers until the user enters a 0.
# This programme gets the adverage of all the numbers the reader before entering 0.

numbers = []

number = int(input('Please Enter a number: '))

while number != 0:
    numbers.append(number)
    number = int(input('Enter a number - 0 to quit: '))

for value in numbers:
    print(value)

if numbers:  # Check if the list is not empty to avoid division by zero
    average = float(sum(numbers)) / len(numbers)
    print(f'The average is {average}')
else:
    print('No numbers were entered.')