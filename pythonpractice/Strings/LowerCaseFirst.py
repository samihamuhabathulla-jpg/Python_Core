word = input("Enter a word : ")
lower = ""
upper = "" 
for i in word:
    if(i.isupper()):
       upper+=i
    else:
        lower+=i
print("After changing : ",(lower+upper))