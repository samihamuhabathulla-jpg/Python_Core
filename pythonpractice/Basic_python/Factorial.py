n = int(input("Enter a number: "))
i = 1
while i <= n:
    factorial = 1
    j = 1
    while j <= i:
        factorial = factorial * j
        j += 1
    print("The factorial of", i, "is", factorial)
    i += 1