word = input("Enter a word : ")
count = 0
counted = ""
for i in word:
    if not i.isalpha() and not i.isnumeric():
        if i not in counted:
            count = count + word.count(i)
            counted = counted+i 
print("The special character count is",count)       
    