"""
Q92: Combine Lists into Dictionary
You have two separate lists: one containing subject names and another containing corresponding marks. Create a dictionary from these two lists using dictionary comprehension, mapping each subject to its mark.
"""

subjects = ["Maths", "English", "Science", "Marathi", "Hindi"]
marks = [90, 75, 80, 85, 70]

subject_marks = {
    subject: mark
    for subject, mark in zip(subjects, marks)
}

print(subject_marks)