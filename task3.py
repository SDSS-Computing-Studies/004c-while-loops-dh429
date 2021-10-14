#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
import math
while True:
        number = input("Enter a number:")
        number = float(number)

        while number != number.is_integer() and number % 2 != 0:
            print("That is not an even integer")
            number = input("Enter a number:")
            number = float(number)

            if number.is_integer() and number % 2 == 0:
                print ("That is an even integer")
                break

        else:
            print("That is an even integer")
            break
