try:
    m=int(input("Enter maths mark: "))
    p=int(input("Enter physics mark: "))
    c=int(input("Enter chemistry mark: "))

    if m>=65 and p>=55 and c>=50 and (m+p+c)>=180:
        print("Eligible")
    else:
        raise Exception

except:
    print("Not Eligible")