L=int(input("Enter Lower Limit:"))
U=int(input("Enter Upper Limit:"))
print("The prime numbers between",L,"and",U,"are:")
for num in range(L,U+1):
    if num > 1: #prime numbers are greater than 1
        for i in range(2,num):
            if (num % i) == 0:
                break
        else: #for-else 
            print(num)