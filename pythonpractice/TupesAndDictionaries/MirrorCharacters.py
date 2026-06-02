k = 3
s = "paradox"
mirror_dict = {chr(i): chr(219 - i) for i in range(97, 123)}
res = s[: k - 1]
for char in s[k - 1 :]:
    res += mirror_dict.get(char, char)
print(res)