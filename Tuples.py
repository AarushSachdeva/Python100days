'''Tuples in Python'''
'''Tuples are ordered collection of data items.They store multiple elements in a single variable.Tuples items are seperated by commas and enclosed within round brackets().Tuples are unchangeable or immutable means we cannot change them after creation.'''
tup=(1,5,6)
print(type(tup),tup)
'''Common confusion to python developers is that if we write tup=(1) and then print type of tup we get <class int> thats because it will think of tup as int if we dont put comma in it.'''
tup1=(1)#This will print <class int>
print(type(tup1),tup1)
tup2=(1,)#This will print <class tuple>
print(type(tup2),tup2)
#Tuples cannot be altered
#tup[0]=10 this will give an error
'''Indexing in tuple'''
print(tup[0])
'''Tuples also have negative indexing'''
'''tup=('apple','banana','orange')
          -3      -2        -1      '''
print(tup[-3])
'''Length of tuple'''
print(len(tup))
'''Check for item in tuple'''
if 5 in tup:
  print("Yes",5,"is present in",tup,sep="~",end="This line has ended")
else:
  print("No 5 is not present in tup")
'''Range of Index'''
#You can print a range of tuple items by specifying where you want to start,where you want to end and what jump or how many elements you want to skip.
tuple123=("Aarush","Raj","Salman","Jacob","Nana","Raina"]
print(tuple123[1:5:2])#New Tuple
print(tuple123[0:6:3])
'''WE CANNOT ADD A VALUE,DELETE A VALUE OR CHANGE A VALUE IN TUPLE DIRECTLY'''
'''IF WE WANT TO DO THE ABOVE THREE OPERARTIONS WE HAVE TO MAKE A COPY OF THE TUPLE IN THE FORM OF A LIST,PERFORM THE OPERATION AND CONVERT THE LIST BACK TO THE TUPLE'''
countries=("Spain","Italy","India","England","Germany")
temp=list(countries)#Conversion of tuple to list
temp.append("Russia")
temp.pop(3)#Remove the 3 index element
temp[2]="Finland"
countries=tuple(temp)
print(countries)
'''HOWEVER,WE CAN CONCATENATE TWO TUPLES WITHOUT CONVERTING THEM TO LISTS'''
countries2=("Afghanistan","Saudi Arabia","China")
countries3=countries+countries2#(Addition of two tuples actually concatenation of tuples not addition) in this countries2 will be added at the back of countries this is happening because we 
#are creating a new tupple thats why they are being concatenated otherwise if we try to concatenate tuple 2 in tuple 1 thats not allowed
print(countries3)
'''COUNT METHOD'''
'''This method is used for returning the number of times an element or a value occurs in a tuple'''
tuple0=(1,1,1,4,5,7,3,2,1,1,3,5,3)
print(tuple0.count(1))
'''INDEX METHOD'''
#The index method is used to return the first occurence of a value in the tuple
print(tuple0.index(3))
#We can also specify the range in which we are finding the first occurence in a tuple
print(tuple0(5,-4,-1))
