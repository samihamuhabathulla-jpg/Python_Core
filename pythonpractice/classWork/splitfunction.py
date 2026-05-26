listA=[]
n =int(input("Enter number of elements in the list: "))
for i in range(0,n):
    print("Enter element No-{}:".format(i+1))
    element=int(input())
    listA.append(element)
print("The entered list is:\n",listA)

n=int(input("Enter number of elements in the list: "))
listA =input("Enter elements separated by comma: ").split()
print("The entered list is:\n",listA)

t=list(map(int,input("Enter the list elements seperated by space:").split()))
print("The entered list is:\n",t)