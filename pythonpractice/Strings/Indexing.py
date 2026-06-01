s1 = input("Enter a string : ")
s2 = input("Enter a string : ")
x = s1[0] + s2[0]
mid1 = len(s1) // 2
mid2 = len(s2) // 2
y = s1[mid1] + s2[mid2]
z = s1[-1] + s2[-1]
result = x + y + z
print(result)