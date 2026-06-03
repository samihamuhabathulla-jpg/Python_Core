import re
text="Alan Turing was a pioneer of theoretical computer scienece and artificial intelligence. he was born on 23 june 1912 in maida vale, London"
res=re.search("^i.*London$",text)
if(res):
   print("We have a match!")
else:
   print("We don't have a match")
print(type(res))