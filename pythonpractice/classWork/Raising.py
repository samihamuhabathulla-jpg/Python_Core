try:
    num =int(input("Enter a positive integer:"))
    if(num<=0):
        raise ValueError("This is a negative number!")
except ValueError as e:
    print(e)
    print("I am successfully handled")