# #using append mode we use to add more data to or file. meanwhile adding some new lines
f=open("harry.txt","a")
# f.write("you are writing and new lines using append mode\n") #this content will be added after the last of the old file.
a=f.write("you are writing and new lines using append mode\n") #this will return how many characters we have added
print(a)
f.close()
#if we wish to know how many character did we have added. we must return value into a variable.
# the no of time we will run this program , the no of times these will be added to the file
# here 'f.write()' function will return no of characters into a variable

