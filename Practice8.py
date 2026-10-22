# =====================================================================
#  Lesson 8: Functions
# =====================================================================

# Exercise 1: Write a function square(n) that returns n squared. Test it with 4, 7, and 10.

def square(n):
    return n*n

print(square(4))
print(square(7))
print(square(10))

# Exercise 2: Write a function is_even(n) that returns True or False. Then use it in a loop to print every number from 1 to 10 with “Even” or “Odd”.

def is_even(n):
    return n%2 == 0

for i in range(1,11):
    if is_even(i):
        print(f"{i}: Even")
    else:
        print(f"{i}: Odd")

# Exercise 3: Write a function average(numbers) that takes a list and returns its average rounded to 2 decimals. Test it with [78, 92, 65, 88].
def average(numbers):
    return round(sum(numbers)/len(numbers),2)

print(average([78, 92, 65, 88]))


# Exercise 4: Write a function get_grade(marks) that returns the grade using the rules from Lesson 4 (A+, A, B, C, Fail, or “Invalid marks”). Then use it on this list:

def get_grade(marks):
    grade = ''
    if  marks < 0 or marks > 100:
        grade =  "Invalid marks"
    elif marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    else: 
        grade = "Fail"
    return grade

all_marks = [95, 82, 45, 71, 105, 66]
# Print each mark with its grade.
for m in all_marks:
    print(f"Marks: {m} and grade: {get_grade(m)}")

# Exercise 5: Write a function count_vowels(text) that returns the number of vowels in a string. Then write a second function is_palindrome(word) that returns True or False. 
# Test both with the user’s input.

def count_vowels(text):
    count = 0
    for n in text:
        if n in "aeiou":
            count += 1
    return count

def is_palindrome(word):    
    return word == word[::-1]

text = input("Write a word to check if it's plaindrome and how much vowels it has: ").strip().lower()

print(f"Total vowels in ({text}) are {count_vowels(text)}")
print(f"This text  ({text}) is plaindrom or not: {is_palindrome(text)}")

# Exercise 6 (challenge): Calculator, version 2. Rewrite your Lesson 4 calculator using functions:

# calculate(a, b, operator) returns the result, or an error message string for division by zero or an invalid operator.
# Put the main part in a while True loop so the user can keep calculating until they type q to quit.
def calculate(first_num, second_num, operator):
    if operator == '+':
        return first_num + second_num
    elif operator == '-':
        return first_num - second_num
    elif operator == '*':
        return first_num * second_num
    elif operator == '/':
        if second_num == 0:
            return "Cannot divide by zero."
        else:
            return first_num / second_num
    else:
        return operator + " is Invalid operator"

print("====Simple Calculator====")
while True:
    operator = input("Enter any operator from (+, -, *, /) or q to quit: ")
    if operator.lower() == 'q':
        break
    first_num = float(input("Enter First number: "))
    second_num = float(input("Enter Second number: "))
    
    
    print(calculate(first_num, second_num, operator))
    