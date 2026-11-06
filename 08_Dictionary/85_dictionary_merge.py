"""
Q85: Dictionary Merge Function
Write a Python function named merge_dicts(d1, d2) that accepts two dictionaries (d1 and d2) as arguments and returns a new dictionary formed by merging them using the update() method. Ensure d1 remains unchanged.
"""

def merge_dicts(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result


dict1 = {"name": "Varsha", "age": 25}
dict2 = {"city": "Mumbai", "language": "Python"}

merged = merge_dicts(dict1, dict2)

print("Original Dictionary 1:", dict1)
print("Original Dictionary 2:", dict2)
print("Merged Dictionary:", merged)