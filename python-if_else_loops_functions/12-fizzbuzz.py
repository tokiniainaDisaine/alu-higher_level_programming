#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 != 0 and i % 5 != 0:
            print(f"{i}", end=" ")
        elif i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
