"""
Q67: Given a list of marks, use list comprehension to create a new list that contains only the marks that are above 75. Example: marks = [65, 80, 70, 90, 75, 82, 60] -> [80, 90, 82].
"""

marks = [65, 80, 70, 90, 75, 82, 60]

result = [mark for mark in marks if mark > 75]

print(result)