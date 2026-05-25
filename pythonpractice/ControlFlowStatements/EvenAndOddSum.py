num = input()
even_sum = 0
odd_sum = 0
for char in num:
    digit = int(char)
    if digit % 2 == 0:
        even_sum = even_sum + digit
    else:
        odd_sum = odd_sum + digit
print(even_sum, odd_sum)