#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number => 0 else number % -10
if last_digit > 5:
    print("Last digit of", f"{number:d}", "is", f"{number:d}", "and is greater than 5")
elif last_digit == 0:
    print("Last digit of", f"{number:d}", "is", f"{number:d}", "and is 0")
elif last_digit < 6 and != 0:
    print("Last digit of", f"{number:d}", "is", f"{number:d}", "and is less than 6 and not 0")
