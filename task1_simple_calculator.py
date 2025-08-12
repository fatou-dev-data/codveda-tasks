def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# User input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("\nChoose the operation:")
print("1 - Addition (+)")
print("2 - Subtraction (-)")
print("3 - Multiplication (*)")
print("4 - Division (/)")

choice = input("Your choice (1/2/3/4): ")

if choice == "1":
    result = addition(a, b)
    operator = "+"
elif choice == "2":
    result = subtraction(a, b)
    operator = "-"
elif choice == "3":
    result = multiplication(a, b)
    operator = "*"
elif choice == "4":
    result = division(a, b)
    operator = "/"
else:
    print("Invalid choice.")
    result = None

if result is not None:
    print(f"{a} {operator} {b} = {result}")
