# prints out all the even numbers from 2 to 100

number_to = 100
number_from = 2

for number in range(number_from, number_to):
    if (number % 2) == 0:
        print(number)

