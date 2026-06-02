def find_max(t, n):
    if n == 1:
        return t[0]
    return max(t[n - 1], find_max(t, n - 1))

items = (11, 65, 54, 23, 76, 33, 82, 98)
print(find_max(items, len(items)))