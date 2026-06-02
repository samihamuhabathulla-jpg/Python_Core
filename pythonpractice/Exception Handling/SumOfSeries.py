try:
    n=int(input("Enter number: "))
    if n<=0:
        raise Exception
    s=0
    for i in range(1,n+1):
        s=s+(1/(i**i))
    print(round(s,5))
except:
    print("Exception: Enter only positive numbers")