sentence = input("Enter a sentence : ")
words = sentence.split(" ")
max = words[0]
for i in words:
    if len(i)<len(max):
        max = i
print("Smallest word is",max)