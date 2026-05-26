String =input("Enter a string:")
total_digits=0
total_letters=0
for s in String:
    if s.isnumeric():
        total_digits+=1
    elif s.isalpha():
        total_letters+=1

    else:
        pass
    print("Total letters found:-",total_letters)
    print("Total digits found:-",total_digits)