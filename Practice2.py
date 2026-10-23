# =====================================================================
#  LESSON 2: Input, Type Conversion, and Operators
# =====================================================================
 
# Exercise 1: Ask the user for their name and birth year. Calculate
# their age (use 2026) and print:
# Hi name, you are about 30 years old.
 
name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))
age = 2026 - birth_year
 
print(f"Hi {name}, you are about {age} years old.")
 
 
# Exercise 2: Ask the user for two numbers. Print their sum,
# difference, product, and division result.
 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
 
print(f"Sum: {a + b}")
print(f"Difference: {a - b}")
print(f"Product: {a * b}")
print(f"Division: {a / b}")
 
 
# Exercise 3: Predict the output, then run it to check:
# print(20 // 6)
# print(20 % 6)
# print(2 ** 3)
# print(7 == 7.0)
 
# Answer:
# 3
# 2
# 8
# True
 
 
# Exercise 4: Shopping bill. Ask the user for a product price and the
# quantity. Calculate the total, then apply a 10% discount
# (total * 0.10). Print the total, the discount amount, and the
# final price.
 
price = float(input("Product price: "))
quantity = int(input("Quantity: "))
 
total = price * quantity
discount = total * 0.10
final_price = total - discount
 
print(f"Total: {round(total, 2)}")
print(f"Discount: {round(discount, 2)}")
print(f"Final price: {round(final_price, 2)}")
 
 
# Exercise 5 (challenge): Ask the user for a number of minutes, for
# example 135. Convert it to hours and minutes using // and %, and print:
# 135 minutes = 2 hours and 15 minutes
 
minutes = int(input("Enter number of minutes: "))
 
hours = minutes // 60
remaining_minutes = minutes % 60
 
print(f"{minutes} minutes = {hours} hours and {remaining_minutes} minutes")
 