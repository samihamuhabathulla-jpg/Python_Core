class InputNotANumberException(Exception): pass
class DivisionByZeroException(Exception): pass
class InvalidMultiplierException(Exception): pass

try:
    operator = input()
    operand1 = input()
    operand2 = input()
    try:
        op1 = float(operand1) if '.' in operand1 else int(operand2)
        op2 = float(operand2) if '.' in operand2 else int(operand2)
    except ValueError:
        raise InputNotANumberException
    if operator == '/' and op2 == 0:
        raise DivisionByZeroException
    if operator == '*' and (op1 in [0, 1] or op2 in [0, 1]):
        raise InvalidMultiplierException
    if operator == '+': res = op1 + op2
    elif operator == '-': res = op1 - op2
    elif operator == '*': res = op1 * op2
    elif operator == '/': res = op1 / op2
    print(f"Input: {operand1} {operator} {operand2}")
    print(f"Output: {res}")
except InputNotANumberException:
    print("Error: Input must be in number format.")
except DivisionByZeroException:
    print("Error: Division by zero is not allowed.")
except InvalidMultiplierException:
    print("Error: Multiplier and multiplicand cannot be 0 or 1.")