#Local variables are those variables that are defined within a function and are created when a function is called and get destroyed when a function is returned.They can be accessed only within
#the function and when we try to access them outside the function then they the Python interpreter will throw an error.
#Global variables are those variables which are defined outside the function and are created and can be used inside the scope of the variable as well as outside it.A global variable can be used
#inside the function until there is no variable of the same name as global variable in the function.
x=5
print(f"The global variable x has value {x}")
def square():
  x=3
  y=2
  print(f"The value of local variable x has value {x}")
  print(f"The value of local varibale y has value {y}")
square()
print(f"The value of globl variable x is {x}")
print(f"Lets print y and its  value {y}")#Will throw an error as y is a local variable and has been destroyed after the function returned.
'''We can use to change of value of global variable x using the GLOBAL keyword'''
x=10
print(f"The value of the global variable x is {x}")
def square():
  global x      #Used for telling the function that global variable x wil be used so dont create local variable of x
  x=100
  print(f"The value of global variable x is {x}")
  y=20
square()
print(f"The value of global variable x is {x}")
