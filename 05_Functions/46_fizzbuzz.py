"""
Q46: Write a function fizzbuzz(n) that takes a single number and prints "Fizz" if it's divisible by 3, "Buzz" if it's divisible by 5, "FizzBuzz" if it's divisible by both, otherwise print the number itself. (Assignment)
"""

num = int(input("Enter number: "))

def fizzbuzz(a):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return a

print(fizzbuzz(num))    


