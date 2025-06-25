#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    comparison = "and is greater than 5"
elif last_digit < 6 and last_digit != 0:
    comparison = "and is less than 6 and not 0"
elif last_digit == 0:
    comparison = "and is 0"
else:
    comparison = "and there's an error"

print(f'Last digit of {number} is {last_digit} {comparison}')
