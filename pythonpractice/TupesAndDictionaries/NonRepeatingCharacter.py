from collections import OrderedDict
s = "goods for goods"
k = 3
counts = OrderedDict()
for char in s:
    counts[char] = counts.get(char, 0) + 1
non_repeat = [char for char, count in counts.items() if count == 1]
if len(non_repeat) >= k:
    print(non_repeat[k - 1])
else:
    print("Less than k non-repeating characters in input.")