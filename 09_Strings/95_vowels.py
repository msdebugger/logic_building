"""
Q95: Read a sentence from the user. Count and print the total number of vowels (a, e, i, o, u, case-insensitive) present in it, using a for loop. (Homework)
"""
sentence = input("Enter line: ")

count = 0
sentence = sentence.lower()

for char in sentence:
    if char in "aeiou":
        count += 1

print("Total vowels:", count)