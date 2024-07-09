import random

random_number = random.randint(1,10)
ALLOWED_VALUES = list(range(1,11))

def magic_number():
    random_number = random.randint(1,10)
    guess_count = 0
    while guess_count < 3:
        try:
            input_number = int(input("Input a number here: "))
            if input_number not in ALLOWED_VALUES:
                raise ValueError("Not a valid input number")
            guess_count += 1
            if input_number == random_number:
                print(f"Success! You guessed the random number was {input_number}!")
                # Break the loop
                break
            elif abs(input_number - random_number) == 1:
                print("Close - you were one away")
            else:
                print(f"Fail! You chose {input_number} - the number to guess was {random_number}")

        except ValueError:
            print(f"Input value must be {ALLOWED_VALUES}")
        
if __name__ == "__main__":
    magic_number()