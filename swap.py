# Swap two numbers without using a temporary variable

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping
a, b = b, a

print(f"After swapping: a = {a}, b = {b}")
