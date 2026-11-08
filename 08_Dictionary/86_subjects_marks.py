"""
Q86: Subjects and Marks
Create a dictionary of 6 subjects and their respective marks. Print the subject with the highest marks and the one with the lowest, using max() and min() functions alongside a lambda expression.
"""
marks = {
    "Maths": 90,
    "English": 75,
    "Science": 95,
    "Marathi": 80,
    "Hindi": 65,
    "Computer": 98
}

highest = max(marks.items(), key=lambda item: item[1])
lowest = min(marks.items(), key=lambda item: item[1])

print(f"Highest Marks: {highest[0]} - {highest[1]}")
print(f"Lowest Marks: {lowest[0]} - {lowest[1]}")