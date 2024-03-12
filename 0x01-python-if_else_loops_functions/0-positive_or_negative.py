#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# MY CODE WILL BE HERE --THIS CODE WILL SHOW YOU IF THE NUMBER IS POSITIVE OR NEGATIVE OR EQUALS TO 0--
if number == 0 :
     print(f"{number:d} is zero")
elif number > 0 :
     print(f"{number:d} is positive")
else :
    print(f"{number:d} is negative")
