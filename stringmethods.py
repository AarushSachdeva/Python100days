#########################Welcome,Here we will understand and learn more about strings and their methods###################################################
'''What is a string??
A string is like an array.It is a sequence of characters which have to be written in single quotes or double quotes in python.
'''
#Creation of a variable which contains string datatype
temp="Hi,My name is Aarush"
#Taking input of a string from user(By default the input is in string)
name=input("Enter your name\n")
print(name)
#We can create multi-line strings using """ or '''.
str="""Hi I am Aarush,
this is my github profile which you are viewing
Here you will learn more about strings"""
#Length of a string(We can find the length of a string using len() function)
len1=len(name)
print("The length of my name is:",len1)
"""Indexing in string
To access the elements of a string we use indexing.Indexing starts from 0 to len(string)-1.The first character is indexed 0 and the last one is indexed len(string)-1.
We can access each character in the string using index.
"""
print(name[0])
print(name[1])
"""Slicing in string
This is an operation or method for cutting a string from the main string.There are two types of slicing 1.Positive Slicing 2.Negative slicing
"""
print(name[0:3])
print(name[-3:-1])
