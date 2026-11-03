"""
Q82: World Capitals 
Create a dictionary mapping five countries to their capital cities. Iterate through this dictionary using the items() method and print each pair in the format: Country -> Capital. (Homework)
"""

capitals = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "Italy": "Rome",
    "England": "London",
    "Japan": "Tokyo"
}

for key, value in capitals.items():
    print(f"{key} -> {value}")    

