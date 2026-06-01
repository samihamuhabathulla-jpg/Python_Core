def add_mul(num1,num2,num3):
    out=(num1+num2)*num3
    return out

val1=int(input("Enter the first integer:"))
val2=int(input("Enter the second integer:"))
val3=int(input("Enter the third integer:"))
result=add_mul(val1,val2,val3)
print("The result is ",result)