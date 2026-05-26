user_input = input("Enter numbers: ").split()
maximum = int(user_input[0])
for string_number in user_input:
    number = int(string_number)
    if number > maximum:
        maximum = number
print("The maximum number is", maximum)