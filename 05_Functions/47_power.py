"""
Q47: Write a function power(base, exp) that returns base raised to exp using a loop - no ** operator or pow() allowed. (Assignment)
"""

base = int(input("Enter base: "))
exp = int(input("Enter exp: "))

def power(b, e):
    power = 1
    for i in range(1, exp+1):
        power = power * base
    return power

print(power(base, exp))    

