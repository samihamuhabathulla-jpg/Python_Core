k = 2
lst = [(2, 3), (3, 3), (1, 4), (2, 4), (2, 5), (3, 4), (1, 4), (3, 4), (4, 7)]
counts = {}
res = []
for tup in lst:
    counts[tup[0]] = counts.get(tup[0], 0) + 1
    if counts[tup[0]] <= k:
        res.append(tup)
print(res)