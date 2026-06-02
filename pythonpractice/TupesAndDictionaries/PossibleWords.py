from collections import Counter
words = ["go", "bat", "me", "eat", "goal", "boy", "run"]
charset = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
res = []
for w in words:
    if not (Counter(w) - Counter(charset)):
        res.append(w)
print(", ".join(res))