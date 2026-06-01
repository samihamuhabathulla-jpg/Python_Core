s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
newString = ""
for i in range(len(s1)):
    newString += s1[i] + s2[-(i + 1)]
print(newString)