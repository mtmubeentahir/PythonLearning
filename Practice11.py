# =====================================================================
#  Lesson 11: Modules, pip, and Virtual Environments
# =====================================================================
 
#Exercise 1: Use the random module to simulate rolling two dice. Print both dice and their total. Then roll them 5 times in a loop.
 
import random

def dice_roll():
    return random.randint(1,6), random.randint(1,6)
    
dice1 , dice2 = dice_roll()
print(f"Dice1: {dice1}, Dice2: {dice2} and their total: {dice1 + dice2}")

for i in range(5):
    dice1 , dice2 = dice_roll()
    print(f"Dice1: {dice1}, Dice2: {dice2} and their total: {dice1 + dice2}")
    
    
# Exercise 2: Use datetime to print today’s date and the current time. Then ask the user for their birth year and calculate their age using the current year from datetime instead of typing 2026.
# Hint: datetime.now().year

import datetime
print(datetime.datetime.now())

dob = int(input("Your Birth year: "))
print(f"Your age is: {datetime.datetime.now().year - dob}")


# Exercise 3: Your own module. Create helpers.py containing:

# get_number(prompt)
# is_even(n)
# a test inside if __name__ == "__main__":

# Then create main.py that imports both functions, asks for a number, and prints whether it’s even or odd. Run main.py, then run helpers.py directly, and notice the difference.
from helper import get_number, is_even

num = get_number("Enter a number: ")
if is_even(num):
    print(f"{num} is even")
else:
    print(f"{num} is odd")


