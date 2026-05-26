t=list()
print(type(t))
vowel_string="aeiou"
t=list(vowel_string)
print(t)
['a','e','i','o','u'] 

list1=["red","green","blue","yellow","black"]
for i in range (len(list1)):
    print(list1[i])

    list1=["Tiger","Zebra","Lion","Elephant","Giraffe","cat","dog"]
    list1.sort()
    print(list1)

    list1=[34,66,12,89,45,23]
    list1.sort(reverse=True)
    print(list1)

    t=[1,2,3,4,5]
    t1=t.copy()
    t1[0]=10
    print(t)
    [1,2,3,4,5]
    print(t1)
    [10,2,3,4,5]
    print(t==t1)