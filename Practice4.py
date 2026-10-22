# =====================================================================
#  LESSON 4: Conditions (if / elif / else)
# =====================================================================
 


# Exercise 1: Ask the user for a number and print whether it’s positive, negative, or zero.
number = int(input("Enter any number to check it's positive, negative or zero: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
    
    
# Exercise 2: Ask the user for two numbers and print which one is bigger, or “Both are equal”.
    
first_num = int(input("First number: "))
second_num = int(input("Second number: "))

if first_num > second_num:
    print(f"{first_num} is bigger")
elif first_num < second_num:
    print(f"{second_num} is bigger")
else:
    print("Both are equal")


# Exercise 3: Grade calculator. Ask for marks out of 100:

# 90 and above → A+
# 80–89 → A
# 70–79 → B
# 60–69 → C
# Below 60 → Fail
# Bonus: if the marks are above 100 or below 0, print “Invalid marks”

marks = int(input("Enter marks out of 100: "))
if  marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Your grade is: A+")
elif marks >= 80:
    print("Your grade is: A")
elif marks >= 70:
    print("Your grade is: B")
elif marks >= 60:
    print("Your grade is: C")
else: 
    print("Fail")


# Exercise 4: Leap year. Ask the user for a year. A year is a leap year if:

# it’s divisible by 4 and not divisible by 100, or
# it’s divisible by 400

# Test with: 2024 (leap), 1900 (not leap), 2000 (leap), 2026 (not leap).

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap year")
else:
    print(f"{year} : Not a Leap year")


# Exercise 5 (challenge): Simple calculator. Ask for two numbers and an operator (+, -, *, /). Print the result. 
# If the operator is / and the second number is 0, print “Cannot divide by zero” instead of crashing. 
# If the operator is anything else, print “Invalid operator”.

print("====Simple Calculator====")
first_num = int(input("Enter First number: "))
second_num = int(input("Enter Second number: "))

operator = input("Enter any operator from (+, -, *, /): ")

if operator == '+':
    print(f"Result by adding {first_num} in {second_num} is {first_num + second_num}.")
elif operator == '-':
    print(f"Result by subtracting {first_num} from {second_num} is {first_num - second_num}.")
elif operator == '*':
    print(f"Result by multiplying {first_num} by {second_num} is {first_num * second_num}.")
elif operator == '/':
    if second_num == 0:
        print("Cannot divide by zero.")
    else:
        print(f"Result by dividing {first_num} by {second_num} is {first_num / second_num}.")
else:
    print(f"'{operator}' is Invalid operator")