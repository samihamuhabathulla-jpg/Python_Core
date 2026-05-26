my_set={1,2,3,4,3,2}
print(my_set)
my_set=set((1,2,3,2))
print(my_set)

my_set={1,3}
print(my_set)
print(list(my_set)[0])

my_set.add(2)
print(my_set)

my_set.update([2,3,4])
print(my_set)

my_set.update({4,5})
my_set.update({3,6})
print(my_set)

my_set={1,3,4,5,6}
print(my_set)
my_set.discard(4)
print(my_set)
my_set.remove(6)
print(my_set)
my_set.discard(2)
print(my_set)

my_set={1,3,4,5,6}
print(my_set)
print(my_set.pop())
my_set.clear()
print(my_set)
