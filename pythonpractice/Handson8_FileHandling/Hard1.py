def manage_student_grades(input_file,output_file):
    f=open(input_file,"r")
    lines=f.readlines()
    f.close()
    out=open(output_file,"w")
    for line in lines:
        data=line.strip().split(",")
        sid=data[0]
        name=data[1]
        grades=list(map(int,data[2:]))
        avg=sum(grades)/len(grades)

        out.write(sid+","+name+","+str(round(avg,2))+"\n")
    out.close()
    out=open(output_file,"r")
    print(out.read())
    out.close()

input_file=input("Enter input file: ")
output_file=input("Enter output file: ")
manage_student_grades(input_file,output_file)