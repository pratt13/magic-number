import random

random_number = random.randint(1,10)
ALLOWED_VALUES = list(range(1,11))

guess_count = 0
while guess_count < 3:
    input_number = input("Input a number here: ")
    if not input_number.isdigit() or (input_number.isdigit() and int(input_number) not in ALLOWED_VALUES):
        print(f"Input value must be {ALLOWED_VALUES}")
    else:
        verified_input_number = int(input_number)
        guess_count += 1
        if verified_input_number == random_number:
            print(f"Success! You guessed the random number was {verified_input_number}!")
            # Break the loop
            break
        elif abs(verified_input_number - random_number) == 1:
            print("Close - you were one away")
        else:
            print(f"Fail! You chose {verified_input_number} - the number to guess was {random_number}")

