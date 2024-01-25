########################################################################LISTS############################################################################
'''Lists-it is a datatype that is used for storing multiple elements.If we want to store marks of all students of a class in an examination we can store it in a single entity called as Lists.'''
'''The main goal of creating lists is to store multiple values in a single entity or single name.'''
'''Syntax for creating list in python
listname=[value1,value2,value3.....]
'''
#Printing a list
mylist=[10,20,30,40,50,60,70]
print(mylist)
print(type(mylist))#Type of datatype
#Indexing in List
print(mylist[0])
print(mylist[1])
#Note:List is an ordered collection of items the way we store it in same order we get it.it cannot be that 10 is now at 0 index while printing and next time it will be at 5th index.
#Elements are stored in square brackets and seperated from other elements with the use of commas.
#Lists are mutable.Means we can alter/change them after creation.
mylist[0]=100
print(mylist)
list1=['apple',100,[4,5],[6,8,[100,[50]]],True]  #Example of a list
print(list1)
#Are 2-D lists possible?
'''YES'''
#Difference between python and other programming languages is that they have arrays which store only a single datatype while python has lists which can store different datatypes together.
#error when accessing element out of range means accessing index not in the defined list.
print(mylist[50])
#Python has another unique feature of negative indexing
list2=["Red","Orange","Blue","Yellow","Green"]
'''      -5     -4      -3      -2      -1       <-indices of respective positions.Their working is in the sense that index -1 is length of list-1.
'''  #How to find length of list??
size=len(list1)
print("The length or the number of elements in",list1,"is:",size)
#check whether a value is present in a list or not.
if [4,5] in list1:
  print("Present")
else:
  print("Absent")
"""Range of list"""
#We can print a range of items of list by specifying where you want to start,where you want to end and if you want to skip elements in between.

