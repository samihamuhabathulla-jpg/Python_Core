def find_and_replace(file_path,old_text,new_text):
    f=open(file_path,"r")
    data=f.read()
    f.close()

    data=data.replace(old_text,new_text)

    f=open(file_path,"w")
    f.write(data)
    f.close()

    f=open(file_path,"r")
    print(f.read())
    f.close()
file_path=input("Enter file name: ")
old_text=input("Enter old text: ")
new_text=input("Enter new text: ")
find_and_replace(file_path,old_text,new_text)