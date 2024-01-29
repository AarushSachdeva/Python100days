is -this is a keyword in python.is keyword compares the exact location of an object in memory while '''==''' operator doesnt compare the memory location of objects it compares the values of the 
two objects.is refers to a single object in memory.
a=4
b="4"
print(a is b)#False because a and b are not the same objects at same memory location
print(a==b)#False because both a and b dont have same values
a=[1,2,43]
b=[1,2,43]
print(a is b)#False
print(a==b)#True
#This thing could not be done with list as list is mutable.
a=3
b=3
print(a is b)
print(a==b)
#See what happens in above code is that 3 is a constant so once we have declared a with value 3 we know that 3 is a
#constant so its value cant be tampered so we dont waste our memory and allocate or we can say we make a and b point
#the same memory location.
b=5
print(a is b)
print(a==b)
#Now as b's value has changed so we cannot make a and b point the same location and we will allocate memory to b also
#since 5 has been declared
c=5
print(b is c)
print(b==c)
#See,now with c similar case
#Similarly if we make tuple or string they are immutable so python wouldnt waste its memory again.
a=(1,2)
b=(1,2)
print(a is b)
print(a==b)
#Now,string
a="Harry"
b="Harry"
print(a is b)
print(a==b)
