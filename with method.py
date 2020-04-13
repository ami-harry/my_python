#with method is another way to open our file.here we don't need closing statement of the file. it automatically close the file.

with open("app.txt") as b:
    # b.write("hello you are using append mode")
    for text in b:
        print(text)
    #       print(i)# it will print first 4 char of the file
    # print(b.readline()) # it will print from 5th char from the file
    # print(b.readlines()) # it will print content in a list with \n
    # a=b.read(100) # here we are storing the 100 char into a variable and printing the variable
    # print(a)
    # here no need to close the file
