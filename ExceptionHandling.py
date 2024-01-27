"""Exception Handling-It is the process of responding to unwanted or unexpected events when a computer program runs.Exception handling deals with these events to avoid the program or system crashing,
and without this process,exceptions would disrupt the normal execution of the program.
Python has many inbuilt exceptions that are raised when your program encounters an error.When these exceptions occur,the Python interpreter stops the current process and passes it to the calling process,
until it is handled.If not handled the program will crash."""
a=int(input("Enter a number"))
try:
  b=0
  c=a//b
  print("The division of",a,"by",b,"is",c)
except Exception as e:
  print("Error occured which is",e)
print("Finally we have successfully executed the program and handled the error")
We can handle specific type of errors
try:
  num=int(input("Enter the number"))
  print(num)
  a=[6,3]
  print(a[num])
except ValueError:
  print("ValueError occured")
except IndexError:
  print("Index error occured")
  
