t=(10,20,30,40,50)
t=(100,)+t[1:]
print(t)
(100,20,30,40,50)

addr='monty@python.org'
uname,domain=addr.split('@')
print(uname)
print(domain)
