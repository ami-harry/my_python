# when we use writing mode, if the file name exists then the new content will replace the old and will save the new content, it file name
# doesn't exists then a new file will be created and the content will be saved into it
f= open("harry1.txt","w")
a= f.write("hello harry, you are using wirte function and writing this line")
#  by storing this file into a variable, the variable will store the no of characters in that file and we can print it later
print(f) #it will print details about the file system .
print(f) #it will print no of characters in that file .
f.close()
# this 'w' mode will allow you to add only a single line at once. if you tried to add more than one line it will replace the old one
#  if we want to add many lines in a file we have to open the file in append 'a' mode
# we must return any value so that it will know that how many characters we have added

