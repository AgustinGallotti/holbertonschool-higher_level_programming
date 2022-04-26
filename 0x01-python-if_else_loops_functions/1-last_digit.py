#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number > 6):
    n == number % 10
    if (number > 0):
        print(f"Last digit of {number} is {n} and is greater than 6 and not 0")
if (n == number % -10):
    if (number < 0 and number < 5):
        print(f"Last digit of {number} is {n} and is less than 6 and not 0")
elif (n == 0):
    print(f"The last digit of {number} is {n} and is 0")
