lst = [('for', 24), ('Gods', 8), ('creates', 30)]
for i in range(len(lst)):
    for j in range(len(lst) - i - 1):
        if lst[j][1] > lst[j + 1][1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)