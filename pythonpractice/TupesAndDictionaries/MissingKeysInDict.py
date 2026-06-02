defd = {'a': 1, 'b': 2, 'd': 3}
key = 'c'
try:
    print(defd[key])
except KeyError:
    print("Key Not found")