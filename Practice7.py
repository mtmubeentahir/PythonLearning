# ===================================================================
# Lesson 7: Dictionaries and Sets
# ===================================================================


# Exercise 1: Create a dictionary about yourself with name, age, city, and profession. Print each value with a label. Then change your age, add a new key hobby, and print the whole dictionary.

user = {
    "name": "Mub",
    "age": 30,
    "city": "Lahore",
    "profession": "Labour"
}

print(f"Name: {user['name']}, Age: {user['age']}, City: {user['city']}, Profession: {user['profession']}")
user['age'] = 34
user["hobby"] = "Nothing"

for key, value in user.items():
    print(f"{key}: {value}")


# Exercise 2: Given:

prices = {"rice": 350, "sugar": 160, "milk": 220, "bread": 150}
# Loop through it and print each item like rice: Rs 350. Then print the total of all prices.

for key, value in prices.items():
    print(f"{key}: Rs {value}")

print(sum(prices.values()))




# Exercise 3: Price lookup. Using the same prices dictionary, ask the user for an item name. If it exists, print its price. If not, print “Item not found”.
prices = {"rice": 350, "sugar": 160, "milk": 220, "bread": 150}

print(list(prices))
item_name = input("Enter any item name from list to see the prices: ").strip().lower()
print(prices.get(item_name, "Item not found."))



# Exercise 4: Word counter. Ask the user for a sentence and count how many times each word appears. For example, the cat and the dog should give:

# the: 2
# cat: 1
# and: 1
# dog: 1

sentence = input("Write a sentence to count the same words: ")
counter = {}
for word in sentence.split():
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
        
for key, value in counter.items():
    print(f"{key}: {value}")

# Exercise 5: Given:

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Ahmed", "marks": 58},
    {"name": "Zara", "marks": 74}
]

# Print each student’s name and whether they passed (marks >= 60) or failed. Then print the name of the student with the highest marks.

top =students[0]
for student in students:
    if student['marks'] >= 60:
        print(f"Name: {student['name']} is passed with  Marks: {student['marks']} ")
    else:
        print(f"Name: {student['name']} is failed with  Marks: {student['marks']} ")
    
    if student['marks'] > top['marks']:
        top = student

print(f"Top student: {top['name']} with {top['marks']} marks")        



    

# Exercise 6 (challenge): Given:


class_a = set(["Ali", "Sara", "Ahmed", "Zara", "Bilal"])
class_b = set(["Sara", "Hamza", "Zara", "Usman"])

print(f"Students in both classes: {class_a & class_b}")

print(f"Students only in both class A: {class_a - class_b}")

print(f"Students only in both class A: {class_a | class_b}")
