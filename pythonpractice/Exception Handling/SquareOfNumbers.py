try:
    n=int(input("Enter a number: "))
    print("The square of",n,"is",n*n)

except ValueError:
    print("Error: Invalid input.")
    print("Please enter a valid number.")

finally:
    print("Execution complete")