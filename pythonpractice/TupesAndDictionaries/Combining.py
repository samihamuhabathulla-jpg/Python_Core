d1 = {'Gfg': 20, 'is': 36, 'best': 100}
d2 = {'Gfg2': 26, 'is2': 19, 'best2': 70}
keys1 = list(d1.keys())
values2 = list(d2.values())
res = {}
for i in range(len(keys1)):
    res[keys1[i]] = values2[i]
print(res)