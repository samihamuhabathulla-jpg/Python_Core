str1 = input("Enter the string: ")
result = ""
for ch in str1:
    if ch.isalnum() or ch == " ":
        result += ch
    else:
        result += "#"
print(result)