"""
Q102: Longest Word
Take a sentence as input. Print the longest word in it.
"""



sentence = input("Enter a sentence: ")

words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)