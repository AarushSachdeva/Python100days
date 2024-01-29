'''In Python,we can handle files.We can open,close,read,write,append and do various more operations on file.We can also handle binary files in Python.'''
#Before we can perform any operations on file we have to open it using the open() function which return file object.It takes two arguemnts one is the name of the file and second is the mode in which we want to open.
READING A FILE(WE CAN READ ALL CONTENTS WRITTEN IN FILE BY THIS METHOD)
f=open("file.txt","r")#if no parameter is given as input for mode then the r mode is used by default.
content=f.read()
print(content)
f.close()                                               
WRITING IN A FILE(WE CAN WRITE IN THE FILE USING THIS METHOD BUT ONE THING TO NOTE IS THAT THIS MODE WILL WRITE IN FILE AND OVERWRITE THE PREVIOUS CONTENT IN THE FILE)
f=open("file.txt","w")
f.write("Hey My name is Suresh I am Aarush's friend")
f.close()
APPENDING IN A FILE(WE CAN ADD TEXT AT THE END OF THE FILE AND THE PREVIOUS CONTENT WILL REMAIN INTACT)
f=open("file.txt","a")
f.write("Hey My name is Aarush I am a second year student in Mait")
f.close()
CREATING A FILE(WE CAN CREATE A FILE USING THIS MODE)
f=open("file2.txt","x")
f.close()
Alternative way for closing the file automatically after work is done
with open("file.txt","r") as f:
  text=f.read()
  print(text)
  
