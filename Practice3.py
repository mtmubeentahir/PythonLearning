# =====================================================================
#  LESSON 3: Strings
# =====================================================================
 
# Exercise 1: Ask the user for their full name. Print it in UPPERCASE,
# in lowercase, and in Title Case, then print how many characters it has.
 
full_name = input("Full Name: ").strip()
 
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(len(full_name))
 
 
# Exercise 2: Predict the output, then run it to check:
# city = "Gujranwala"
# print(city[0])
# print(city[-1])
# print(city[0:4])
# print(city[4:])
# print(city[::-1])
 
# Answer:
G
a
Gujr
anwala
alawnarjuG
 
 
# Exercise 3: Ask the user for an email address. Print the username
# (the part before @) and the domain (the part after @).
 
email = input("Email address: ").strip()
parts = email.split("@")
 
print(f"Username: {parts[0]}")
print(f"Domain: {parts[1]}")
 
 
# Exercise 4: Ask the user for a sentence. Print how many words it has.
 
sentence = input("Enter any sentence: ")
word_count = len(sentence.split())
 
print(f"Your sentence has {word_count} words.")
 
 
# Exercise 5 (challenge): Ask the user for a word and check whether
# it's a palindrome, meaning it reads the same backwards, like "level"
# or "madam". Print True or False.
 
word = input("Enter a word: ").strip().lower()
 
print(f"Is palindrome: {word == word[::-1]}")