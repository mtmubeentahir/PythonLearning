# =====================================================================
#  LESSON 1: Getting Started
# =====================================================================

# Exercise 1: Write a program that prints your name, your city, and
# your favorite food, each on a separate line.
 
name = "Mubeen"
city = "Gujranwala"
fav_food = "Pizza"
 
print(name)
print(city)
print(fav_food)
 
 
# Exercise 2: Create variables item = "Book", price = 450, and
# quantity = 3. Then use an f-string to print:
# I bought 3 Book for 450 rupees each.
 
item = "Book"
price = 450
quantity = 3
 
print(f"I bought {quantity} {item} for {price} rupees each.")
 
 
# Exercise 3: Predict the output without running it, then run it to check:
# a = 10
# b = "10"
# print(a + 5)
# print(b + "5")
# print(type(b))
 
# Answer:
15
105
'str'
 
 
# Exercise 4 (challenge): Create variables for the length and width of
# a rectangle. Calculate the area (length * width) and print it with
# an f-string.
 
length = 10
width = 50
area = length * width
 
print(f"The area of the rectangle is {area}")
 