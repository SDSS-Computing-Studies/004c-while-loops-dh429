#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
You will need to keep track of a current value, and modify
or update the current value through every iteration of the
while loop

(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
number = 2

while number != 50:
    print(number)
    number = number + 2
    if number == 50:
        break