def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def modulus(x, y):
    return x % y


print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

calculatorMode = True

while calculatorMode:
    operation = input("Select Operation - 1, 2, 3, 4, 5 : ")
    if operation == "1" or operation == "2" or operation == "3" or operation == "4" or operation == "5":
        try:
            x = int(input("Enter your first Number: "))
            y = int(input("Enter your second Number: "))

            if operation == "1": print(add(x, y))
            if operation == "2": print(subtract(x, y))
            if operation == "3": print(multiply(x, y))
            if operation == "4": print(divide(x, y))
            if operation == "5": print(modulus(x, y))

            anotherOperation = input("Do you want to perform another operation? (no/yes): ")
            if anotherOperation == "no":
                calculatorMode = False
        except ValueError:
            print("Invalid input!")
    else:
        print("Invalid selection!")
