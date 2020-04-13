#using tell() and seek()
# tell() function will give out the nos of char it is pointing at.
# every time we call tell() method after printing line it will say its char no

# f=open("harry1.txt")
# print(f.tell()) # here it is now pointing at 0th char
# print(f.readline()) # here we are reading first line
# print(f.tell()) # here it will say that after first line at which char it is now
# print(f.readline())
# print(f.tell())

# printing out line from few character. meanwhile escaping some chars and printing the content
# by using seek() method we can avoid or take the printing control n no of chars before and will print after that.
#  by using tell() and seek() we can find at where we are currently printing at and will print by escaping some chars.

# f=open("harry1.txt")
# f.seek(0) # the o/p will be only last 0 chars
# print("we are at 0th char",f.tell()) # this will tell us that where our printing control is
# print(f.readline()) # this will print the o/p from beginning becuase we are ecaping 0 char
# # print(f.seek(10)) --> this no of avoiding char will be printed and we can easily get to know that how many chars we have escaped
# print("her are are escaping 10 cars from staring using seek() methods",f.seek(10))
# print("here it showing the at which char our print control is..",f.tell())
# print(f.readline())
# print("now we are this ",f.tell(),"char")
# f.close()
