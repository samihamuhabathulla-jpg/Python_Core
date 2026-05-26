word = input("Enter a word : ")
c=0
for i in word:
    c+=1

print("count of the word ",c)
print("Repeating the word 2 times : ",(word+word))
print("First letter ",word[0])
print("Three letters ",word[0:4])