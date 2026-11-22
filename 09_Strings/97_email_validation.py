"""
Q97: Email Validation
Take an email as input. Validate that it contains exactly one @ and at least one '.'. Print "Valid" or "Invalid"
"""
email = input("Enter email: ")

if email.count("@") == 1 and email.count(".") >= 1:
    print("Valid")
else:
    print("Invalid email")

