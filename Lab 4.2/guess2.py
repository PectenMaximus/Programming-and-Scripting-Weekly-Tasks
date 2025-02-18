# guess a number - programe tells user if they are too high or too low 

import numpy as np
number_to_guess = np.random.randint(1, 20)

guess = int (input ('Please guess a number: '))

while guess != number_to_guess:
    if guess < number_to_guess:
        print ("Too Low!")
    else:
        print ("Too High!")
        guess = int (input("guess again:"))

print ('well done! it was',number_to_guess)