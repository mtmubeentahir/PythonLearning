# =====================================================================
#  Lesson 12: Classes and Objects (OOP)
# =====================================================================
 
# Exercise 1: Create a class Rectangle with length and width. Add methods area() and perimeter() that return the results. 
# Create two rectangles and print their area and perimeter. 

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
rec = [Rectangle(5,9),Rectangle(9,9)]

for r in rec:
    print(f"Area : {r.area()}")
    print(f"Perimeter : {r.perimeter()}")


# Exercise 2: Create a class Student with name and a list of marks. Add these methods:

# average() returns the average, rounded to 2 decimals
# grade() returns the grade based on the average (reuse your Lesson 8 grade logic)
# __str__ returns something like Ali: average 82.5, grade A

# Create three students and print them.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def average(self):
        return round(sum(self.marks)/len(self.marks),2)
    
    def grade(self):
        avg = self.average()
        if  avg < 0 or avg > 100:
            return "Invalid marks"
        elif avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else: 
            return "Fail"

    
    def __str__(self):
       return f"{self.name}: average {self.average()}, grade {self.grade()}"
        
s1 = Student("Ali", [92,65,83,75,49])
s2 = Student("Furqan", [89,56,38,57,94])

print(s1)
print(s2)
        

# Exercise 3: Build the BankAccount class from Step 4 yourself, without copying, and add:

# a history list that records every deposit and withdrawal as a string, like "Deposit: 500"
# a show_history() method that prints the history, numbered
# a check that refuses negative or zero deposit amounts

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self, amount):
        if amount <= 0:
            return "Invalid Amount."
        self.balance += amount
        self.history.append(f"Deposit: {amount}")
        return "Deposit successful"
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        self.history.append(f"Withdraw: {amount}")
        return "Withdaraw successful"
    
    def show_history(self):
        for index, entry in enumerate(self.history, start=1):
            print(f"{index}. {entry}")
    
    def __str__(self):
        return f"{self.owner}'s account: Rs {self.balance}"
            
acc = BankAccount("Ali", 5000)
print(acc.deposit(0))
print(acc.deposit(500))
print(acc.withdraw(7000))
print(acc.withdraw(2000))
print(acc)
acc.show_history()



# Exercise 4: Shopping cart. Create a class Cart that stores items in a dictionary like {"rice": 350}. Add these methods:

# add_item(name, price)
# remove_item(name), which prints “Item not found” if the item isn’t in the cart
# total() returns the sum of all prices
# show() prints all items and the total

class Cart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, name, price):
        self.items[name] = price
        return "Item Added successful"
    
    def remove_item(self, name):
        if name not in self.items:
            return "Item not found"
        self.items.pop(name)
        return "Item removed."
    
    def total(self):
        return sum(self.items.values())
    
    def show(self):
        for name, price in self.items.items():
            print(f"{name}: Rs {price}")
        print(f"Total: Rs {self.total()}")


 
cart = Cart()
cart.add_item("rice", 350)
cart.add_item("oil", 650)
cart.add_item("milk", 300)
cart.show()
 
cart.remove_item("rice")
cart.remove_item("sugar")
cart.show()

# Exercise 5: Inheritance. Create a class Employee with name and salary, and a method info(). 
# Then create Manager(Employee), which also has a team_size and overrides info() to include it. 
# Use super().__init__(). Create one of each and print their info.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def info(self):
        return f"Name: {self.name} Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def info(self):
        return f"{super().info()}, Team size: {self.team_size}"
 



e = Employee("Ali", 50000)
m = Manager("Rafi", 74000, 11)


print(e.info())
print("===============")
print(m.info())


# Exercise 6 (challenge): A simple chat history class. This is a small taste of AI app code. Create a class Conversation:

# __init__ creates an empty list called messages
# add_message(role, text) appends a dictionary like {"role": "user", "text": "Hi"}. The role must be "user" or "assistant"; otherwise, print an error and don’t add it.
# show() prints each message like user: Hi
# save(filename) saves the messages to a JSON file
# load(filename) loads the messages from a JSON file

# Create a conversation, add 4 messages (alternating user and assistant), save it, then create a new Conversation object, load the file into it, and show it.

import json
class Conversation:
    def __init__(self):
        self.messages = []
        
    def add_message(self, role, message):
        if role not in ("user", "assistant"):
            print(f"Error: invalid role '{role}'")
            return
        self.messages.append({"role": role, "text": message })
    
    
    def show(self):
        for msg in self.messages:
            print(f"{msg['role']}: {msg['text']}")
            
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.messages, file, indent=4)
    
    def load(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            self.messages = json.load(file)


    
chat = Conversation()
chat.add_message("user", "Hi")
chat.add_message("assistant", "Hello! How can I help?")
chat.add_message("user", "Prepare email notes")
chat.add_message("assistant", "Done. Here are your notes.")
chat.add_message("robot", "This should not be added")
chat.save("chat.json")
 
new_chat = Conversation()
new_chat.load("chat.json")
new_chat.show()