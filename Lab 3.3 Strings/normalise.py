# This program reads in a string and strips any leading or trailing spaces. It also converts all the letters to lower case. The program also outputs the length of the original string and the normalised string.

raw_string = input("Enter a string: ")
normalised_string = raw_string.strip().lower()

length = len(raw_string)
length_normalised = len(normalised_string)

print ("That string normalised is:", {normalised_string})
print ("We reduced the input string from", {length}, "to", {length_normalised}, "characters")
