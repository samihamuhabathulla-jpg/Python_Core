import math
def prime(n):
    if n <= 1:
        return False
    end = int(math.sqrt(n))
    for i in range(2, end + 1):
        if n%i == 0:
            return False
    return True
for i in range(1, 100):
    check = prime(i)
    if check:
        print(i, "is a Prime number")