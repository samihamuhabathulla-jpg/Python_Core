num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
try:
    num3 = float(num1/num2)
    print("Division of two numbers is",num3)
except ZeroDivisionError:
    print("Can't divide a number by zero")
