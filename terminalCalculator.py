#This is a calculator that works inside the terminal

def calculator0():
    print("This is a basic arithmatic calculator, please enter your first number")

    num1 = float(input("Enter first number here: "))
    operator = input("Enter your operator here: ")
    num2 = float(input("Enter second number here: "))

    def calculator():
        if operator == ("+"):
            result = float(num1 + num2)
        elif operator == ("-"):
            result = float(num1 - num2)
        elif operator == ("/"):
            result = float(num1 / num2)
        elif operator == ("*"):
            result = float(num1 * num2)
        elif operator == ("**"):
            result = float(num1 ** num2)

        return result

    print(calculator())

def calculatorVersion1():
    # functions for available operations
    def multiply(x, y):
        return x * y
    def division(x, y):
        return x / y
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def exponent(x, y):
        return x ** y
    def floorDiv(x, y):
        return x // y
    def youngsModu(x, y):
        return x % y

    print("""
    This is a basic calculator for arithmetic operationsm, select your operations
    1.) Addition
    2.) Subtraction
    3.) Multiplication
    4.) Division
    5.) Exponents
    6.) Floor Division
    7.) Young's Modulus
    """)

    while True: #The calculator itself
        choice = (input("Kindly enter an operation to calculate (1/2/3/4/5/6/7): "))
        if choice in ('1', '2', '3', '4' ,'5', '6', '7'):
            num1 = int(input("enter first number: "))
            num2 = int(input("enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, '=', subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, '=', multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, '=', str(division(num1, num2)))
            elif choice == '5':
                print(num1, "**", num2, '=', str(exponent(num1, num2) ))
            elif choice == '6':
                print(num1, '//', num2, '=', floorDiv(num1, num2))
            elif choice == '7':
                print(num1, '%', num2, '=', youngsModu(num1, num2))
            else:
                print("invalid input, sorry!")

def calculatorVersion2():
    # functions for available operations
    def multiply(x, y):
        return x * y
    def division(x, y):
        return x / y
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def exponent(x, y):
        return x ** y
    def floorDiv(x, y):
        return x // y
    def youngsModu(x, y):
        return x % y

    print("""
    This is a basic calculator for arithmetic operations, select your operations
    1.) Addition
    2.) Subtraction
    3.) Multiplication
    4.) Division
    5.) Exponents
    6.) Floor Division
    7.) Young's Modulus
    """)

    while True:
        print("Kindly enter an operation to calculate (1/2/3/4/5/6/7) or \'q\' to quit ")
        choice = (input())
        if choice in (('1 2 3 4 5 6 7').split()):
            num1 = int(input("enter first number: "))
            num2 = int(input("enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
            elif choice == '2':
                print(num1, "-", num2, '=', subtract(num1, num2))
            elif choice == '3':
                print(num1, "*", num2, '=', multiply(num1, num2))
            elif choice == '4':
                print(num1, "/", num2, '=', str(division(num1, num2)))
            elif choice == '5':
                print(num1, "**", num2, '=', str(exponent(num1, num2) ))
            elif choice == '6':
                print(num1, '//', num2, '=', floorDiv(num1, num2))
            elif choice == '7':
                print(num1, '%', num2, '=', youngsModu(num1, num2))
            else:
                print("invalid input, sorry!")
        elif choice == 'q':
            break




calculatorVersion2()

