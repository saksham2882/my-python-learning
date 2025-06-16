# arithmetic operations and a simple calculator

# Basic operations
print("Division:", 15 / 6)           # division (returns float)
print("Floor division:", 15 // 6)    # Floor division (returns integer)
print("Modulus:", 5 % 3)             # Remainder of division
print("Exponentiation:", 2 ** 4)     # 2 raised to the power of 4

# Simple calculator
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

print(f"The addition of {num1} and {num2} is: {num1 + num2}")
print(f"The subtraction of {num1} and {num2} is: {num1 - num2}")
print(f"The multiplication of {num1} and {num2} is: {num1 * num2}")
print(f"The division of {num1} by {num2} is: {num1 / num2}")
print(f"The modulus of {num1} and {num2} is: {num1 % num2}")