# here we are trying to access our text file harry.txt
# opening files in read mode. by default any file is open in 'rt' mode, means read text mode

# f=open("harry.txt")
# data= f.read()
# print(data)
# f.close()
# print("here we are handling our text file using python open function")


# printing data by passing no of character

# f=open("harry.txt", "rt")
# data= f.read(10) # it will print only 10 character from starting, it will print \n also.
# print(data, "\nhere we have printed 10 characters")
# data= f.read(15) #it will print next 15 character
# print(data, "\nhere we have printed next 15 characters")
#if no if character is more than the characters in the file. it will escape the second print statement
# f.close()
# print("here we are handling our text file using python open function")

#printing content of the file line by line
# f=open("harry.txt", "rt")
# for line in f: #here line method is printing the content of the file line by line with \n space between lines
#     print(line,end="") # to avoid an extra new line we use end="" to print normal flow

# printing content by lines
# f=open("harry.txt","rt")
# print(f.readline())
# print(f.readline()) # we can also pass the no of character in the argument ot get those character
# print(f.readline())
# this will print the output with an new line space
# print(f.readlines()) # this will print the content of the file in a list and will print \n after every line becuase
# in the original file new line is aviliable
# readlines() method will return a list . meanwhile the output will be in a list


