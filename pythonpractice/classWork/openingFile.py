with open("text.txt","r+")as myObject:
    content =myObject.read()
    myObject =open("test.txt","w")
    myObject.write("Hey i have started using files in python\n")
    myObject.close()
 
    myObject =open("text.txt","w")
lines =["Hello everyone\n","Writing #multiline strings\n","This is the #third line"]
myObject.writelines(lines)
myObject.close()

myObject =open("text.txt",'r')
print(myObject.readline())
myObject.close()

myObject = open("text.txt","r")
d=myObject.readlines()
for line in d:
    words = line.split()
    print(words)
    ['Hello','Everyone']
    ['Writing','multiline','Strings']
    ['This','is','the','third','line']

    print("Now reading the contents of the file:")
    fobject=open("text.txt","r")
    for str in fobject:
        print(str) 




