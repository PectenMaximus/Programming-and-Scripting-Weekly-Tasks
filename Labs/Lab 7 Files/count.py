FILENAME = "count.txt"

def readNumber():
    try:
        with open(FILENAME) as f:
            number = int(f.read())
            return number
    except FileNotFoundError:
        print(f"{FILENAME} not found. Creating the file with initial number 0.")
        with open(FILENAME, 'w') as f:
            f.write('0')
        return 0

num = readNumber()
print(num)