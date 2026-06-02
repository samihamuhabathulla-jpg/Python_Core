from collections import Counter
lst = [(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]
counts = Counter(lst)
pairs = 0
for tup in counts:
    rev = (tup[1], tup[0])
    if rev in counts and tup < rev:
        pairs += counts[tup] * counts[rev]
    elif tup == rev:
        pairs += (counts[tup] * (counts[tup] - 1)) // 2
print(pairs)