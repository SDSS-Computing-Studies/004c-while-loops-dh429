#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""

num1 = 1

num2 = 1

num3 = num1 + num2

num4 = num3 + num2
while num1 <= 100 or num2 <= 100 or num3 <= 100:
    print(num1, num2, end = " ")
    num1 = num2 + num1
    num2 = num1 + num2
