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
#Now lets talk about finally keyword
#Finally is a keyword.The block of code written under this keyword gets executed irrespective of whether error has occured or not.
#Method-1
try:
  b=0
  c=a//b
  print("The division of",a,"by",b,"is",c)
except Exception as e:
  print("Error occured which is",e)
print("Finally we have successfully executed the program and handled the error")#Now this line occurs or executes everytime irrespective of whether or not error has occured or not.
#Method-2
try:
  b=0
  c=a//b
  print("The division of",a,"by",b,"is",c)
except Exception as e:
  print("Error occured which is",e)
finally:
print("Finally we have successfully executed the program and handled the error")#Now this line occurs or executes everytime irrespective of whether or not error has occured or not.
#The difference between method-1 and method-2 is that in method-2 if we wrap the whole thing in a function then also it will get executed.
def fun1():
  try:
    b=0
    c=a//b
    print("The division of",a,"by",b,"is",c)
    return 1
  except Exception as e:
    print("Error occured which is",e)
    return 0
  finally:
    print("Finally we have successfully executed the program and handled the error")#Now this line occurs or executes everytime irrespective of whether or not error has occured or not.
x=fun1() 
print(x)
#In the above scenario,we see that if we write the finally block of code without using finally then it will not get executed as the function has return written in it but with the help of finally keyword we make the program execute finally block of code even when the function has returned.
we learn about the raising custom errors using raise keyword. Sometimes, we want to impose hard and fast regulations so, we can use customer errors if something violates those regulations so, that it does not create any problem later in the program execution and that error can be handled at that point of time only. In the previous videos, we learnt about how to handle errors using exception handling with try, except and finally blocks. We can also make our custom error classes using any base case error with our defined set of rules to raise that error whenever it violates those rules.
a=int(input("Enter a value between 5 and 9"))
if(a<5 or a>9):
  raise ValueError
