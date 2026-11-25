"""
Q100: Sorted Names
Take a list of names as input (comma separated). Split them, sort them alphabetically, and join them back with " | " as separator.
"""

names = input("Enter names (comma separated): ")

names = names.split(",")

names.sort()

result = " | ".join(names)

print(result)