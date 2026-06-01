str1 = input("Enter the string: ")
words = str1.split()
for word in words:
    has_alpha = False
    has_digit = False
    for ch in word:
        if ch.isalpha():
            has_alpha = True
        if ch.isdigit():
            has_digit = True
    if has_alpha and has_digit:
        print(word)