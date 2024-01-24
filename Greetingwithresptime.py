#Write a python program capable of greeting you with Good Morning,Good Afternoon and Good Evening according to the time.
import time #Who will tell me the time the time module which is an in-built module in python import it to your program
Name=input("Enter your Name\n")
currenttime=time.strftime('%H:%M:%S')
timestamp=int(time.strftime('%H'))
c=Name.capitalize()
if(timestamp>=4 and timestamp<12):
	print("Good Morning",c,"its",currenttime)
elif(timestamp>=12 and timestamp<17):
	print("Good afternoon",c,"its",currenttime)
else:
	print("Good evening",c,"its",currenttime)


