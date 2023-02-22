def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():

    num1 = float(input("what is your first number?: "))
    for i in operations:
        print(i)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what is your next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        stop_loop = input(
            "Type 'y' to continue calculating, or type 'n' to exit.: ")
        if stop_loop == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()