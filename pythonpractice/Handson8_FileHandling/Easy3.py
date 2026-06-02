def append_to_file(file_path,msg):
    f=open(file_path,"a")
    f.write("\n"+msg)
    f.close()

    f=open(file_path,"r")
    print(f.read())
    f.close()

file_path=input("Enter file name: ")
msg=input("Enter message: ")
append_to_file(file_path,msg)