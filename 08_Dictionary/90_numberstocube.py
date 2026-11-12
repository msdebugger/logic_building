"""
Q90: Numbers to Cubes
Using dictionary comprehension, create a new dictionary where keys are numbers from 1 to 10 (inclusive), and values are the cube of each number.
"""

cubes = {num: num ** 3 for num in range(1, 11)}

print(cubes)