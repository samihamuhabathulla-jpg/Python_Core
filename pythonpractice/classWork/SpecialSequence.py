import re 
text ="Alan Turing was born on 23 june 1912 in London"
res=re.findall('\AAlan',text)
print("Result for \A =",res)
print("-"*79)
res=re.findall(r'\bLon',text)
print("result for \\b=",res)
print("-"*79)

res=re.findall(r'ring\b',text)
print("Result for \\b=",res)
print("-"*79)

res=re.findall(r'ring\B',text)
print("Result for \\B=",res)
print("-"*79)

res=re.findall("\d",text)
print("result for \d=",res)
print("-"*79)

res=re.findall("\D",text)
print("result for \D=",res)
print("-"*79)

res=re.findall('\s',text)
print("result for \s=",res)
print("-"*79)

res=re.findall('\S',text)
print("result for \S=",res)
print("-"*79)

res=re.findall('\w',text)
print("Result for \w=",res)
print("-"*79)

res=re.findall('\W',text)
print("Result for \W=",res)
print("-"*79)

res=re.findall('London.\Z',text)
print("Result for \Z=",res)








