try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    c = a/b
except(ZeroDivisionError):
    print("Can't divide by zero")
except NameError:
    print("this is Value Error")
else:
    print("No exception ocuurs")
finally:
    print("Successfully executed")

