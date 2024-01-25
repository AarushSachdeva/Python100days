def fact(n):
  #base case
  if (n==0 or n==1):
    return 1
  #recursive case
  return n*fact(n-1)
n=int(input("Enter the number"))
print(fact(n))
