OPS = {
    "+": lambda num1, num2: num1 + num2,
    "-": lambda num1, num2: num1 - num2,
    "*": lambda num1, num2: num1 * num2,
    "/": lambda num1, num2: num1 / num2 if num2 != 0 else None
}

choice = input("Choose operation (+, -, *, /): ")
try:
    operation = OPS[choice]
except KeyError:
    print("Selected operation doesn't exist")
else:
    try:
        number1 = float(input("Give 1st number: "))
        number2 = float(input("Give 2st number: "))
        result = operation(number1, number2)

        if result is None:
            print("This program can't reach infinity")
        else:
            print(f"Result: {result:.2f}")
    except ValueError:
        print("I don't think this is a number")
