# for loop is auto-adjusting in nature for a string it converts itself into character for list into element
name="Aarush"
for i in name:
  print(i)
mylist=["apple","banana","mango"]
for i in mylist:
  print(i)
#There basically exists two kinds of loops in python
        #1.for loop
        #2.while loop
#for loop is used to iterate over a sequence like list,tuple,set,dictionary,string
#while loop is used to execute a set of statements as long as a condition is true
# for i in range(10):
#   print(i)
# for i in range(1,100):
#   print(i)
for i in range(1,100,1):
  print(i)
#Python while loop is used for terminating when a set of conditions fail
i=0
while(i<5):
  print(i)
  i=i+1
#We can also use with while
i=0
while(i<5):
  print(i)
  i=i+1
else:
  print("I am here in else")
#In python,emulate do-while loop
while(True):
  print(i)
  i=i+1
  if(i%100==0):
    break
  else:
    continue
  
