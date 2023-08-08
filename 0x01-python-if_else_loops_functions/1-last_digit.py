#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    number = number * -1
    last = last * -1
end = ""
if last > 5:
    end = "and is greater than 5"
elif last == 0:
    end = "and is 0"
elif last < 6 and last != 0:
    end = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last} {end}")
