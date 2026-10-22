=====================================================================
 Lesson 5: Loops
=====================================================================
 

# Exercise 1: Print the numbers from 1 to 10, then print the even numbers from 2 to 20.

for i in range(1,11):
    print(i)


# Exercise 2: Multiplication table. Ask the user for a number and print its table from 1 to 10:

num = int(input("Enter number to print table: "))
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")


# Exercise 3: Ask the user for a number n and print the sum of all numbers from 1 to n. For example, n = 100 should give 5050.

num = int(input("Enter number to print Total of all number from 1: "))
total = 0
for i in range(1, num+1):
    total +=i

print(f"Total of all number is : {total}")


# Exercise 4: Count vowels. Ask the user for a sentence and count how many vowels (a, e, i, o, u) it has.

sentence = input("Enter a sentence to count vowels: ").lower()
count = 0
for letter in sentence:
    if letter in "aeiou":
        count += 1
        
print(f"Total number of vowels in sentence are: {count}")
    

# Exercise 5: Number guessing game. Set secret = 7. Keep asking the user to guess until they get it right. 
# After each wrong guess, tell them “Too high” or “Too low”. When they guess correctly, print how many attempts it took.
secret = 7
num =0
attempts = 0
while num != secret:
    num =  int(input("Guess the number : "))
    attempts += 1
    if num == secret:
        print(f"It tooke {attempts} attempts to guess the number")
    elif num < secret:
        print("Too low")
    else:
        print("Too High")


# Exercise 6 (challenge): Star pattern. Ask for a number of rows and print a triangle like this for 5 rows:
# *
# **
# ***
# ****
# *****

num =  int(input("Number of rows : "))

for i in range(1,num+1):
    print("*" * i)