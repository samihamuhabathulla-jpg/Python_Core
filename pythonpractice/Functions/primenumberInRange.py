import math
start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
if(end<start):
    print("Invalid Number")
def prime(n):
    if n <= 1:
        return False
    end = int(math.sqrt(n))
    for i in range(2, end + 1):
        if n%i == 0:
            return False
    return True
if(end<start):
    print("Invalid Numbers")
else:
    for i in range(start, end+1):
        check = prime(i)
        if check:
            print(i)