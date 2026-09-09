# Take a person's age and whether they have a valid ID (True/False) as input. They can enter a venue
# only if they are 18 or older AND have a valid ID. Print the appropriate message. (Homework)

age = int(input("Enter age: "))
hasId = bool(input("Enter have a id or not: "))

if age >= 18 and hasId == True:
    print("Person can enter")
else:
    print("Person cannot enter")

