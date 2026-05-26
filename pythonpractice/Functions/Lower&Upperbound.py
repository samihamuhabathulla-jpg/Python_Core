even = 0
odd = 0
def evenSum(n):
    global even
    even+=n
def oddSum(n):
    global odd
    odd+=n
for i in range(1,1000+1):
    if i%2==0:
        evenSum(i)
    else:
        oddSum(i)
print("Even Sum of numbers from 1 to 1000 is",even)
print("Odd Sum of numbers from 1 to 1000 is",odd)
print("The absolute difference between two sums is",(even - odd))