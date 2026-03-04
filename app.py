from calculator import Calculator

calc = Calculator()

def process_input(a, operator, b=None):

    if operator == "+":
        return calc.add(a, b)

    elif operator == "-":
        return calc.subtract(a, b)

    elif operator == "*":
        return calc.multiply(a, b)

    elif operator == "/":
        return calc.divide(a, b)

    elif operator.lower() == "c":
        return calc.clear()

    else:
        raise ValueError("Invalid operator")