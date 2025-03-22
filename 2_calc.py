OPS = {
    "+": "addition",
    "-": "subtraction",
    "*": "multiplication",
    "/": "division"
}

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    return None

choice = input("Choose operation (+, -, *, /): ")
try:
    operation = OPS[choice]
except KeyError:
    print("Selected operation doesn't exist")
else:
    try:
        number1 = float(input("Give 1st number: "))
        number2 = float(input("Give 2st number: "))

        if choice == "+":
            res = addition(number1, number2)
            print(f"Result: {res:.2f}")
        elif choice == "-":
            res = subtraction(number1, number2)
            print(f"Result: {res:.2f}")
        elif choice == "*":
            res = multiplication(number1, number2)
            print(f"Result: {res:.2f}")
        elif choice == "/":
            if number2 == 0:
                print("This program can't reach infinity")
            else:   
                res = division(number1, number2)
                print(f"Result: {res:.2f}")
    except ValueError:
        print("I don't think this is a number")
