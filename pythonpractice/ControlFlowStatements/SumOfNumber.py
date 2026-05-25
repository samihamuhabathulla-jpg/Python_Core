n = int(input("Enter a number : "))
i = 0
for i in range(1, i<=n, 2):
    if i%2==0:
      odd+=i
    else:
       even+=i-1
print("Even sum : ",even)
print("Odd sum : ",odd)