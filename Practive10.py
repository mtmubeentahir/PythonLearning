# =====================================================================
#  LESSON 10: Files and JSON
# =====================================================================
 
import json
 
# Exercise 1: Write a program that asks the user for 3 things they want
# to learn, then saves them to goals.txt, one per line. Then read the
# file and print its contents.
 
with open("goals.txt", "w", encoding="utf-8") as file:
    for i in range(1, 4):
        goal = input(f"Goal {i}: ")
        file.write(f"{goal}\n")
 
with open("goals.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
 
 
# Exercise 2: Diary. Ask the user for one line of text and append it to
# diary.txt. Run the program a few times, then write code that reads
# the file and prints each entry numbered:
# 1. Started learning files today
# 2. JSON looks like dictionaries
 
entry = input("Write today's diary entry: ")
 
with open("diary.txt", "a", encoding="utf-8") as file:
    file.write(f"{entry}\n")
 
with open("diary.txt", "r", encoding="utf-8") as file:
    for index, line in enumerate(file, start=1):
        print(f"{index}. {line.strip()}")
 
 
# Exercise 3: Write a function count_lines(filename) that returns how
# many lines a file has. If the file doesn't exist, return 0 instead of
# crashing.
 
def count_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return len(file.readlines())
    except FileNotFoundError:
        return 0
 
print(count_lines("diary.txt"))
print(count_lines("missing.txt"))
 
 
# Exercise 4: Create this dictionary and save it to profile.json with
# indent=4. Then load it back and print your name and your second skill.
# profile = {
#     "name": "Mubeen",
#     "goal": "AI Engineer",
#     "skills": ["Python", "Git", "FastAPI"]
# }
 
profile = {
    "name": "Mubeen",
    "goal": "AI Engineer",
    "skills": ["Python", "Git", "FastAPI"]
}
 
with open("profile.json", "w", encoding="utf-8") as file:
    json.dump(profile, file, indent=4)
 
with open("profile.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)
 
print(f"Name: {loaded['name']}")
print(f"Second skill: {loaded['skills'][1]}")
 
 
# Exercise 5: Read an AI response. Given this JSON text, use
# json.loads() and print the model name, every text in content (using
# a loop), and the total tokens (input + output).
 
response_text = '''
{
    "model": "demo-model",
    "content": [
        {"type": "text", "text": "Python is a great first language."},
        {"type": "text", "text": "Start with the basics, then build projects."}
    ],
    "usage": {"input_tokens": 25, "output_tokens": 18}
}
'''
 
response = json.loads(response_text)
 
print(f"Model: {response['model']}")
 
for block in response["content"]:
    print(block["text"])
 
usage = response["usage"]
print(f"Total tokens: {usage['input_tokens'] + usage['output_tokens']}")
 
 
# Exercise 6 (challenge): Persistent shopping list. Upgrade your Lesson 6
# shopping list so it remembers items between runs:
# - On start, load the items from shopping.json (an empty list if the
#   file doesn't exist).
# - Show the current items, numbered.
# - Let the user add items until they type done.
# - Save the updated list back to shopping.json.
 
try:
    with open("shopping.json", "r", encoding="utf-8") as file:
        items = json.load(file)
except FileNotFoundError:
    items = []
 
print("Current list:")
for index, item in enumerate(items, start=1):
    print(f"{index}. {item}")
 
while True:
    item = input("Add an item (or 'done' to finish): ").strip()
    if item.lower() == "done":
        break
    if item:
        items.append(item)
 
with open("shopping.json", "w", encoding="utf-8") as file:
    json.dump(items, file, indent=4)
 
print(f"Saved {len(items)} items.")