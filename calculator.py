from calc_art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    continue_calc = True
    while continue_calc:
        operation_symbol = input("Choose one operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                "Type 'y' to continue calculating with 16 or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            continue_calc = False
            calculator()


calculator()
