# Simple Calculator using a loop for continuous operation

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

operations = {
    '1': add,
    '2': subtract,
    '3': multiply,
    '4': divide
}

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice == '5':
        break

    if choice in operations:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        operation = operations[choice]
        result = operation(num1, num2)
        print(f"Result: {result}")
    else:
        print("Invalid input")