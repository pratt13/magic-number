# Random Number Game

Input a number between 1 and 10, if you guess correct you win!

To run, run 
```sh
python random_number_game.py
```

## Different levels
Each level works the same, except it has a different task.
Level 1 is easiest, then progressively harder.
Depending on your experience, you can skip to any level you want to begin.
Each level is on a separate branch to this.



* Level 1 - Python execution of script, fix the bug.
* Level 2 - Update the success print statement to include the input variable that won the game.
* Level 3 - Raise an error if the inputted value is not 1,2,3,4,5,6,7,8,9,10. The program should do nothing other than the print if the input value is not correct. At this point we can assume the input is still a number.
* Level 4 - Add an additional print statement when the input is off by one
    `Close - you were one away`
* Level 5 - Allow a retry if the input is not valid
* Level 6 - Combine all the above so the program allows, 
    * infinite retires for every invalid input.
    * three tries to correctly guess the value
* Level 7 - Encapsulate all the logic into a single python function
* Level 8 - refactor and tidy up
* Level 9 - Create your own program that when runs:
    * Asks for the users first name - and this program only works for people with names between 2 and 20 characters long.
    * Ask for their age in years, they must be at least 5-99 years old. Different ages use different programs.
    * Ask for their favorite food out of: apples, bananas or grapes.
    For each step think about validation, what letters would be allowed.
    After everything is submitted, it should print out a summary of the users selections.



## Learning
Each level has different implementations, but the outcomes should be:
* Conditional expressions
* Print formatting
* If/else statements
* Exception raising
* Try/catch
* While statements
* Data encapsulation