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
#Strings are immutable-we cannot update,delete the characters from a string.A string cannot be updated/deleted but can be assigned an entirely new value to #the same name.
#We can change strings but we cannot change them in-place.
#Functions that we can apply using/on strings
#stringname.upper()-Converts all the characters present in the string to uppercase.
a="Harry"
a=a.upper()#New value assigned
print(a)
#stringname.lower()-converts all the characters present in the string to lowercase.
a=a.lower()
print(a)
#Strip function-It is used to remove whitespaces before and after the string
a=" Silver  Spoon.    "
a=a.strip()
print(a)
#Rstrip function-It is used to remove all occurences of any trailing character
str2="Silver!!!! Spo!!!on !!!!!"
str2=str2.rstrip("!")
print(str2)
#replace function-This function is used to replace all the occurences of the string present to another string.
str1="Silver Spoon"
str1=str1.replace("Sp","M")
print(str1)
#Spilt function-It is used to convert the string into elements of list by splitting them at specified instances.
str0="!!Aarush Lets code"
print(str0.split(" "))#specified instance is " ".
#Capitalize function-It is used to return a string which has converted the first character of the previous string to uppercase and the rest characters into #lowercase.
stg="hello welcoMe to Geeks for Geeks"
print(stg.capitalize())
#count function-it is used to tell or return the number of occurences of a value in a string
value=stg.count("Geeks")
print(value)
#find function-It is used to find the first occurence of a value in a string and return its index.
index=stg.find("o")
print(index)
#isalnum()-This is a function used in Python to return True if the string is made up of only a-z,A-z or 0 to 9.If it consits of any other character then it #return false
flag=stg.isalnum()
print(flag)
#endswith function-It is used to find whether a string ends with a particular character or a set of characters or not.
print(stg.endswith("Aarush"))
print(stg.endswith("Geeks"))
#this function can also be used to check for a value in-between by providing starting and ending indices.
print(stg.endswith("to",4,10))
#swapcase-This is a function used to convert the uppercase characters present in the string to lowercase and vice-versa.
print(stg.swapcase())
