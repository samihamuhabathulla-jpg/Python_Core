My_dict = {}
My_dict = {1:"apple",2:"ball"}
My_dict = {1:"CSE","name":"Ram"}
print(type(My_dict))


print(dict())
numbers=dict(x=5,y=0)
print(numbers)
numbers1 = dict({'x':4,'y':5})
print(numbers1)
numbers1=dict([('x',5),('y',-5)])
print(numbers1)

Myfamily={"child1":{"name":"Ram","year":2005},"child2":{"name":"sita","year":2007}}
print(Myfamily)

thisdict={"brand":"ford","model":"mustang","year":1964}
for x in thisdict:
    print(x,thisdict[x])

    d={1:'one',2:'two'}
    print(d.popitem())
    print(d)

    d={1:"one",2:"three"}
    d1={2:"two"}
    d.update(d1)
    print(d)

    squares={}
    for x in range(5):
        squares[x]=x*x
    print(squares)

    squares={x:x*x for x in range(5)}
    print(squares)

