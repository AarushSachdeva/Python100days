############################################SYSTEM TO CHECK FOR LEAP YEAR##############################################
N=int(input("Enter the year"))
flag=False
if(N%4==0):
  if(N%100==0):
    if(N%400==0):
      flag=True
    else:
      flag=False
  else:
    flag=True
if(flag):
  print("The year:",N,"is a leap Year")
else:
  print("The year:",N,"is not a leap Year")
  
      
