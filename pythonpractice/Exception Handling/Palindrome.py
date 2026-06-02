try:
    n=int(input("Enter number: "))
    temp=n
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n=n//10
    if temp==rev:
        print("Palindrome")
    else:
        print("Not Palindrome")
except ValueError:
    print("Enter only integer numbers")