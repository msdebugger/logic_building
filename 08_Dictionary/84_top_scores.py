"""
Q84: Top Scorers
Populate a dictionary with six student names and their corresponding marks. Loop through it and print the
names of all students who achieved a score above 75.
"""

marks = {
    "Amit": 85,
    "Rahul": 65,
    "Priya": 90,
    "Sneha": 72,
    "Neha": 80,
    "Rohan": 55
}

for name, score in marks.items():
    if score > 75:
        print(name)
