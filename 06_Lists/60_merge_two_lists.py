"""
Q60: Merge two lists
Given two lists, merge them into a single new list without modifying the originals. Hint: use the + operator or a loop to combine. Example: list1 = [1, 2], list2 = [3, 4] -> merged = [1, 2, 3, 4]
"""

list1 = [1, 2]
list2 = [3, 4]

merged = []

for i in range(len(list1)):
    merged.append(list1[i])
for i in range(len(list1)):
    merged.append(list2[i])

print(merged)    