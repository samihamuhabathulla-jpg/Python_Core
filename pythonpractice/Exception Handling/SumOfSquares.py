try:
    n=int(input("Enter number: "))
    if n<1 or n>100:
        raise Exception
    s=0
    for i in range(1,n+1):
        s=s+i*i
        print(s)
except:
    print("Enter value between 1 to 100")