def menu():
    my_list=[]
    while True:
        print("Menu Driven program")
        print("1.Add an element to the list")
        print("2.Display the list")
        print("3.Append a list to the existing list")
        print("4.Modify an existing element")
        print("5.Delete an existing element from its position")
        print("6.Delete an existing element from a given value")
        print("7.sort the list in ascending order")
        print("8.sort the list in descending order")
        print("9.Display the list")
        print("10.Exit")

        choice=input("Enter your choice(1-10):")   
        if choice=='1':
            item =input("Enter a element to append")
            my_list.append(item)
            print("Element added ")
        elif choice=='2':
            item=input("Enter element to insert:")
            position=int(input("Enter the position to insert:"))
            my_list.insert(position,item)
            print("Element added at position ",position)
        elif choice=='3':
            new_list=input("Enter the list to append (separated by comma):").split(",")
            my_list.extend(new_list)
            print("List appended")
        elif choice=='4':
            position=int(input("Enter the position to modify:"))
            if position < len(my_list):
                new_value=input("Enter the new value:")
                my_list[position]=new_value
                print("Element modified at position ",position)
            else:
                print("Invalid position")
        elif choice=='5':
            position=int(input("Enter the position to delete:"))
            if position < len(my_list):
                del my_list[position]
                print("Element deleted from position ",position)
            else:
                print("Invalid position")
        elif choice=='6':
            value=input("Enter the value to delete:")
            if value in my_list:
                my_list.remove(value)
                print("Element with value ",value," deleted")
            else:
                print("Value not found in the list")
        elif choice=='7':
            my_list.sort()
            print("List sorted in ascending order")
        elif choice=='8':
            my_list.sort(reverse=True)
            print("List sorted in descending order")
        elif choice=='9':
            print("The list is: ",my_list)
        elif choice=='10':
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 10.")
menu()

        