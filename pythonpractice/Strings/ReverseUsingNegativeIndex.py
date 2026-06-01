word = input("Enter a word : ")
length = len(word)
ans = ""
for i in range(-1, -(length + 1), -1):
    ans += word[i]
print("Reversed word :", ans)