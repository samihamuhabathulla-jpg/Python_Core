N = int(input("Enter the value of N:"))
i=1
sum=0
while i<=N:
    num = int(input("Enter the user inputs:"))
    if num==-1:
        break
    else:
        sum=sum+num
        i=i+1
print("The sum of user inputs is",sum)