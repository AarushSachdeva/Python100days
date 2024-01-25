'''Fibonacci Sequence'''
n1=0
n2=1
n=int(input("Enter the term which you want to generate of Fibonacci sequence"))
for i in range(1,n):
  n3=n1+n2
  n1=n2
  n2=n3
print("The",n,"th term of the Fibonacci sequence is",n1)

'''Recursive Method'''
def fibo(n):
  #Base Case
  if(n==1 or n==2):
    return n-1
  return fib(n-1)+fib(n-2)
  
n=int(input("Enter the term which you want to generate of Fibonacci sequence"))
print(fibo(n))
