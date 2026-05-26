def add (a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def callback(operation,operand1,operand2):
    return operation(operand1,operand2)
    return result
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Add:", callback(add, a, b))
print("Subtract:", callback(sub, a, b))
print("Multiply:", callback(multiply, a, b))