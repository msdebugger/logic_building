"""
Q87: Student Details
Create a nested dictionary containing details for 4 students, where each student entry includes their name, age, and city. Write a loop to print the full details of each student in a clear, readable format.
"""

students = {
    "student1": {
        "name": "Varsha",
        "age": 25,
        "city": "Mumbai"
    },
    "student2": {
        "name": "Rahul",
        "age": 23,
        "city": "Pune"
    },
    "student3": {
        "name": "Priya",
        "age": 24,
        "city": "Nashik"
    },
    "student4": {
        "name": "Amit",
        "age": 22,
        "city": "Thane"
    }
}

for student_id, details in students.items():
    print(f"\nDetails of {student_id}:")
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"City: {details['city']}")