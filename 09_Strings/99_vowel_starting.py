"""
Q99: Vowel-Starting Words
Take a sentence as input. Split it into words and print how many words start with a vowel.
"""

sentence = input("Enter sentence: ")

words = sentence.split()

vowels = "aeiou"
count = 0

for word in words:
    if word[0].lower() in vowels:
        count += 1

print("Words starting with a vowel:", count)