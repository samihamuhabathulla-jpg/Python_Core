t1 = (30, 9, 7)
t2 = (4, 6)
if isinstance(t1, str) and isinstance(t2, str):
    res = tuple(t1 + t2)
else:
    res = t1 + t2
print(res)