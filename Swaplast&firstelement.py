#Taking input in a list
n=int(input("Enter the number of elements you want in the list\n"))
list1=[]
for i in range(1,n+1,1):
  x=int(input("Enter the element you want to add in your list\n"))
  list1.append(x)
print("This is the list",list1)
#Interchanging the first and last element of the list
temp=list1[0]
list1[0]=list1[n-1]
list1[n-1]=temp
#Printing the new list
print(list1)


  
