# import re


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def moddivide(num1, num2):
    return num1 % num2


def square(num1):
    return num1 ** 2


def squareroot(num1):
    return num1 ** 0.5

# checker = re.compile("[0-9]+")


while True:
    print("Which Operation would you like to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo")
    print("6. Square")
    print("7. Square Root")
    print("0. Exit")
    print("")

    x = int(input("Select a number between 0 and 7: "))

    if x == 0:
        print("Selected Exit. Goodbye.")
        break

    if x > 7 or x < 1:
        print("Error. Please input a valid number.")
        print("")
        continue

    print("")
    print("The format of your operation will be the first number, operation sign, then the second number.")
    print("""
Example: 
x + y, x * y
x - y, x / y""")
    print("")
    y = int(input("What is the first number? "))

    if x in range(1, 6):
        z = int(input("What is the second number? "))

    if x == 1:
        print("Selected Add: ")
        print(str(y) + " + " + str(z))
        print(add(y, z))
        print("\n")

    elif x == 2:
        print("Selected Subtract: ")
        print(str(y) + " - " + str(z))
        print(subtract(y, z))
        print("\n")

    elif x == 3:
        print("Selected Multiply: ")
        print(str(y) + " * " + str(z))
        print(multiply(y, z))
        print("\n")

    elif x == 4:
        print("Selected Divide: ")
        print(str(y) + " / " + str(z))
        print(divide(y, z))
        print("\n")

    elif x == 5:
        print("Selected Modulo: ")
        print(str(y) + " % " + str(z))
        print(moddivide(y, z))
        print("\n")

    elif x == 6:
        print("Selected Square: ")
        print(str(y) + " ^ 2")
        print(square(y))
        print("\n")

    elif x == 7:
        print("Selected Square Root:")
        print("The square root of " + str(y) + ": ")
        print(squareroot(y))
        print("\n")







