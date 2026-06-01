str1 = input("Enter the main string: ")
sub = input("Enter the substring: ")
position = str1.rfind(sub)
print("Last occurrence of", sub, "starts at index", position)