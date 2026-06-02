#comma separated
l = (input("Enter the numbers : "))
my_list = l.split(",")
try:
    five = my_list[5]
    print("The 5th index element is",five)
except IndexError:
    print("Error: Index out of range! ")