import random

random_number = random.randint(1,10)

input_number = int(input("Input a number here: "))
if input_number == random_number:
    print(f"Success! You guessed the random number was {input_number}!")
else:
    print(f"Fail! You chose {input_number} - the number to guess was {random_number}")

