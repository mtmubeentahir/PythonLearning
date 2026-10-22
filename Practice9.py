# =====================================================================
#  LESSON 9: Error Handling (try / except)
# =====================================================================
 
# Exercise 1: Ask the user for a number and print its square. If they
# type something that isn't a number, print "That's not a valid number"
# instead of crashing.
 
try:
    num = float(input("Enter a number: "))
    print(f"Square: {num * num}")
except ValueError:
    print("That's not a valid number")
 
 
# Exercise 2: Ask for two numbers and print the result of dividing them.
# Handle both ValueError and ZeroDivisionError with different messages.
 
try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    print(f"Result: {a / b}")
except ValueError:
    print("Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
 
 
# Exercise 3: Write a function get_int(prompt) that keeps asking until
# the user enters a valid whole number, then returns it. Use it to ask
# for the user's age and birth year.
 
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")
 
age = get_int("Enter your age: ")
birth_year = get_int("Enter your birth year: ")
 
print(f"Age: {age}, Birth year: {birth_year}")
 
 
# Exercise 4: Given:
# fruits = ["apple", "banana", "mango"]
# Ask the user for a position number and print the fruit at that
# position. Handle both ValueError (not a number) and IndexError
# (position doesn't exist).
 
fruits = ["apple", "banana", "mango"]
 
try:
    position = int(input(f"Enter a position (0 to {len(fruits) - 1}): "))
    print(f"Fruit: {fruits[position]}")
except ValueError:
    print("Please enter a whole number.")
except IndexError:
    print("That position doesn't exist.")
 
 
# Exercise 5: Given:
# prices = {"rice": 350, "sugar": 160, "milk": 220}
# Ask the user for an item name and print its price using prices[item]
# (not .get()). Catch the KeyError and print "Item not found".
 
prices = {"rice": 350, "sugar": 160, "milk": 220}
 
item = input("Enter an item name: ").strip().lower()
 
try:
    print(f"{item}: Rs {prices[item]}")
except KeyError:
    print("Item not found")
 
 
# Exercise 6 (challenge): Calculator, version 3. Take your Lesson 8
# calculator and make it crash-proof:
# - Use a get_number() function, so typing abc asks again instead of
#   crashing.
# - Keep the q to quit option.
# - Bonus: inside calculate(), use try / except ZeroDivisionError
#   instead of if b == 0.
 
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
 
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return f"'{operator}' is an invalid operator"
 
print("==== Simple Calculator ====")
 
while True:
    operator = input("Enter an operator (+, -, *, /) or q to quit: ").strip()
    if operator.lower() == "q":
        print("Goodbye!")
        break
 
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
 
    print(f"Result: {calculate(a, b, operator)}")