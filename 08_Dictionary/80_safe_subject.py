"""
Q80: Safe Subject Access Define a dictionary with five subjects and their respective marks. Utilize the get() method to try accessing a subject that is not in the dictionary, ensuring it prints "Not Available" as a default. (Homework)
"""

subjects = {
    "maths": 100,
    "science": 93,
    "history": 80,
    "marathi": 85,
    "hindi": 75

}

print(subjects.get("english", "Not Available"))