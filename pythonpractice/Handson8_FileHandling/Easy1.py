def read_file(file_path):
    f=open(file_path,"r")
    print(f.read())
    f.close()
file_path=input("Enter file name: ")
read_file(file_path)