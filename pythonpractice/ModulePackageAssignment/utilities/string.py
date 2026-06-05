def count_vowels(s):
    c=0
    for i in s:
        if i.lower() in "aeiou":
            c=c+1
    return c