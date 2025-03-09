# A program that puts 10 random numbers into a queue(list), 
# A program should then output all the values in the queue
# then take the numbers from the queue one at a time

# Imports
import random

queue = []
number_of_numbers=10
range_to=100

for n in range (0,number_of_numbers):
    queue.append(random.randint(0,range_to))

print (f"queue is {queue}")

while len (queue) !=0:
    current_number=queue.pop(0)

print ("current Number is {current_number} and the queue is {queue}")

print ("the queue is now empty")
