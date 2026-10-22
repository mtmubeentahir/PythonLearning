# =====================================================================
#  Lesson 6: Lists and Tuples
# =====================================================================

# Exercise 1: Create a list of 5 cities. Print the first city, the last city, and the total number of cities. 
# Then add a new city to the end, remove the second city, and print the final list.

cities = ["Gujrat", "Gujranwala", "Lahore", "Islamabad", "Jehlum"]

print(cities[0])
print(cities[-1])
print(len(cities))

cities.append("Peshawer")
cities.remove("Gujranwala") # cities.pop(1)

print(cities)

# Exercise 2: Given marks = [78, 92, 65, 88, 54, 95, 71], print the highest, the lowest, the total, and the average (rounded to 2 decimals).

marks = [78, 92, 65, 88, 54, 95, 71]

print(max(marks))
print(min(marks))
print(sum(marks))
print(round(sum(marks)/len(marks),2))

# Exercise 3: Ask the user to enter 5 numbers, one at a time, using a loop. Store them in a list, then print the list sorted from smallest to largest.

n = []
for i in range(1,6):
    a = int(input(f"Enter number ({i}/5) :"))
    n.append(a)
n.sort()
print(n)


# Exercise 4: Given numbers = [12, 7, 3, 18, 25, 6, 9, 30], create two new lists, one with the even numbers and one with the odd numbers, and print both.

numbers = [12, 7, 3, 18, 25, 6, 9, 30]
even = []
odd = []

for n in numbers:
    if n%2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(f"Even list is : {even}")
print(f"Odd list is : {odd}")



# Exercise 5: Shopping list app. Use a while True loop that keeps asking the user to type an item. Add each item to a list. When the user types done, stop the loop and print every item numbered like this:

# 1. Milk
# 2. Bread
# 3. Eggs

# Hint: enumerate(items, start=1) starts counting from 1.


cart = []

while True:
    item = input("Enter item: ")
    if item.strip().lower() == "done":
        break
    else:
        cart.append(item)
        
for index, item in enumerate(cart, start=1):
    print(f"{index}. {item}")

# Exercise 6 (challenge): Given nums = [4, 2, 7, 2, 9, 4, 1, 7], create a new list with the duplicates removed, keeping the original order. The result should be [4, 2, 7, 9, 1].
# Hint: loop through nums, and only append a number if it’s not in the new list yet.

nums = [4, 2, 7, 2, 9, 4, 1, 7]

uniq = []
for n in nums:
    if n not in uniq:
        uniq.append(n)
print(uniq)