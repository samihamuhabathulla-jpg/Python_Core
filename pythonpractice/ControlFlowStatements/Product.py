code = int(input("Enter code (1, 2, or 3): "))
if code == 1:   
    num1 = float(input("Enter first decimal: "))
    num2 = float(input("Enter second decimal: "))
    print(num1 + num2)

elif code == 2:
    val1 = int(input("Enter first integer: "))
    val2 = int(input("Enter second integer: "))
    print(val1 * val2)

elif code == 3:
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    print(str1 + str2)

else:
    print("Invalid Code!")