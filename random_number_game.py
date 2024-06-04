import random

random_number = random.randint(1,10)
ALLOWED_VALUES = list(range(1,11))

valid_input = False
while not valid_input:
    input_number = input("Input a number here: ")
    if not input_number.isdigit() or (input_number.isdigit() and int(input_number) not in ALLOWED_VALUES):
        print(f"Input value must be {ALLOWED_VALUES}")
    else:
        valid_input = True

verified_input_number = int(input_number)
if verified_input_number == random_number:
    print(f"Success! You guessed the random number was {verified_input_number}!")
elif abs(verified_input_number - random_number) == 1:
    print("Close - you were one away")
else:
    print(f"Fail! You chose {verified_input_number} - the number to guess was {random_number}")

