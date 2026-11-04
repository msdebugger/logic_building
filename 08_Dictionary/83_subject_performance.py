"""
Q83: Subject Performance Analysis Given a dictionary of marks for different subjects, loop over its values() to calculate and print the total marks and the average mark obtained.

"""
marks = {
    "Maths": 90,
    "English": 50,
    "Science": 80,
    "Marathi": 90,
    "Hindi": 75
}
total = 0
for value in marks.values():
    total += value
print(f"Total of marks is: {total}")