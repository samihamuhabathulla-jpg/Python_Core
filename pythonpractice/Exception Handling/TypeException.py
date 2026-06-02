num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
def mul(num1,num2):
    try:
      num3 = num1*num2
      print("The result is",num3)
    except TypeError:
       print("Inavalid operand type")

mul(num1,num2)
