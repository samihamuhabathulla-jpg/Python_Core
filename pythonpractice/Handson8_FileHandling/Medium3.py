def merge_files(file1,file2,output_file):
    f1=open(file1,"r")
    f2=open(file2,"r")

    data1=f1.read()
    data2=f2.read()

    f1.close()
    f2.close()

    f3=open(output_file,"w")
    f3.write(data1+"\n"+data2)
    f3.close()

    f3=open(output_file,"r")
    print(f3.read())
    f3.close()

file1=input("Enter first file: ")
file2=input("Enter second file: ")
output_file=input("Enter output file: ")
merge_files(file1,file2,output_file)