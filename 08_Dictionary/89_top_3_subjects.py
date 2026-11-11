"""
Q89: Top 3 Subjects by Marks
Given a dictionary of subjects and their marks, sort it by marks in descending order. Then, print only the top 3 subjects with the highest marks.
"""
marks = {
    "Maths": 90,
    "English": 75,
    "Science": 95,
    "Marathi": 80,
    "Hindi": 65,
    "Computer": 98
}

# Sort dictionary by marks in descending order
sorted_marks = sorted(
    marks.items(),
    key=lambda item: item[1],
    reverse=True
)

# Print only the top 3 subjects
print("Top 3 Subjects by Marks:")

for subject, score in sorted_marks[:3]:
    print(f"{subject}: {score}")