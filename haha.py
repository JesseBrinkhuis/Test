import os
import sys
import math
import random

value = random.randint(0, 10)
# print(f"Value is {value})
guess = int(input("Raad het getal: "))

if guess == value:
    print("Je wint!")
else:
    print("Je verliest helaas!")
# os.system("shutdown /s /t 5")
