"""
Chapter 01 - Basic Exception Handling Examples
"""

# Example 1 - ZeroDivisionError

try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")


# Example 2 - Multiple Exceptions

try:
    value = int(input("Enter a number: "))
    result = 100 / value

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")


# Example 3 - else

try:
    number = 10 / 2

except ZeroDivisionError:
    print("Error")

else:
    print("Success:", number)


# Example 4 - finally

file = None

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    if file:
        file.close()
        print("File closed.")


# Example 5 - raise

age = -5

if age < 0:
    raise ValueError("Age cannot be negative.")