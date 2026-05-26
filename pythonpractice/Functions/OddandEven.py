start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
even = 0
odd = 0
def evenSum(n):
    global even
    even+=n
def oddSum(n):
    global odd
    odd+=n
for i in range(start,end+1):
    if i%2==0:
        evenSum(i)
    else:
        oddSum(i)
print("Even Sum : ",even)
print("Odd Sum : ",odd)