def increment(list2):
    for i in range(0,len(list2)):
        list2[i]+=5
        print("Reference of list inside function is",id(list2))

        list1=[10,20,3,40,50]
        print("Reference of list in main",id(list1))
        print("The list before the function call")
        print(list1)

        increment(list1)
        print("The list after the function call")
        print(list1)
        

        def increment(list2):
            print("\nID of list inside function before assignment:", id(list2))
            list2=[1,2,3,4,5]
            for i in range(0,len(list2)):
                list2[i]+=5
                print("ID of list changes inside function after assignment" ,id(list2)) 
                print("The list inside the function is",list2) 
                list1=[1,2,3,4,5]
                print("\nID of list in main before function call:", id(list1))
                print("The list before the function call is",list1)  
            