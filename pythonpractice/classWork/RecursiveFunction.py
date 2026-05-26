def factorial(number):
    if number == 0:
        return 1
    else:
        return (number*factorial(number-1))
    
number = int(input("Enter any number : "))
fact = factorial(number)
print("The factorial of",number,"is",fact)