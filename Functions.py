#We are going to learn about functions
#Function is a block of code which is used to perform a specific task whenever it is called.
#In python,syntax of creation of a function is as follows
#def functionname(parameters):
  #statement
def calculate(a,b):
  print(a+b)
#Functions are of two types:
#1.Built-In-These are functions for which we dont have to write its implementation.These come in-handy with Python.
#2.User-Defined-These are functions whose implementation we have to write.We have to define this function.
def geometricmean(a,b):
  gm=(a*b)/(a+b)
  print(gm)
#Function can be called using:
def geometricmean(a,b):
  gm=(a*b)/(a+b)
  print(gm)
a=10
b=5
geometricmean(a,b)
#We have to name a function before using it/calling it
#We can define it later but for that we need to use pass keyword otherwise we will get an error





