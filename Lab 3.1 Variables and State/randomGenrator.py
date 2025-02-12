# imports
import numpy as np

# function to generate random numbers
random_number = np.random.randint(1, 100)
print (random_number)

#Function that allows the user to input the range to generate the random number from
first_number_in_range = int(input("Enter the first number in the range: "))
second_number_in_range = int(input("Enter the second number in the range: "))
random_number = np.random.randint(first_number_in_range, second_number_in_range)
print (random_number)
