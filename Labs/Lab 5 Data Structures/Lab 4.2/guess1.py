# Promts the user to guess a number - programme keeps prompting the user until they guess the correct number

number_to_guess = 5

guess = int (input("Guess a number: "))
while guess != number_to_guess:
    print ("Wrong!")
    guess = int(input("Guess again: "))

print ("Well done! The number was", number_to_guess)