"""
Q91: Filter Passing Marks
Given an existing dictionary of subjects and their respective marks, use dictionary comprehension to
generate a new dictionary that includes only the subjects where the student scored 40 or more (i.e.,
passed)
"""

marks = {
    "Maths": 90,
    "English": 35,
    "Science": 80,
    "Marathi": 30,
    "Hindi": 75
}

passed_subjects = {
    subject: score
    for subject, score in marks.items()
    if score >= 40
}

print(passed_subjects)