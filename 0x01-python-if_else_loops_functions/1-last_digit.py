#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    test = number * -1
    last = (test % 10) * -1
else:
    last = number % 10

if last > 5 or last < -5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif (last < 6) or (last < -6):
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
