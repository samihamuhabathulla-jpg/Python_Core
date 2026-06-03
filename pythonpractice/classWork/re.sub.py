import re 
text="Alan Turing was a pioneer of theoretical computer scienece and Turing artificial intelligence. he was born on 23 june 1912 in maida vale, London"
res=re.sub("theoretical","practical",text)
print("result={}".format(res))