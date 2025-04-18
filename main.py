from string import ascii_uppercase
from random import randint

alphabet = list(ascii_uppercase)

def generate_random_combination():
    combination = ""
    for x in range(3):
        letter_id = randint(0, 23)
        combination += alphabet[letter_id]
    return combination

#How to "teach" a sequence of logical instructions to think? I bet it have to change its code, a function that write itself.'

if __name__ == '__main__':
    print(generate_random_combination())