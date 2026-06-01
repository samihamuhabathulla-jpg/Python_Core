def circle(radius):
    print("Area of the circle is ",3.14*radius*radius)

def rectangle(Length,breadth):
    print("Area of the rectangle is ",Length*breadth)

def square(side):
    print("Area ",side*side)

while True:
    print("Menu Driver Program")
    print("1.Area of Circle")
    print("2.Area of Rectangle")
    print("3.Area of Square")
    print("4.Exit")
    choice=int(input("Enter your choice : "))
    if(choice ==1):
        radius = int(input("Enter the radius of the circle : "))
        circle(radius)
    elif(choice == 2):
        Length = int(input("Enter the length of the rectangle : "))
        breadth = int(input("Enter the breadth of the rectangle : "))
        rectangle(Length,breadth)
    elif(choice ==3):
        side = int(input("Enter the side of the square : "))
        square(side)

    elif(choice == 4):
        break
    else:
        print("Wrong Choice")
