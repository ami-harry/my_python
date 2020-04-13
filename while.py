# printing a range of numbers using while loop
# wap to print 1 to 10 using while loop

# i=0
# while(i<10):
#     print(i)
#     i+=1

# printing table of a number

# i=2
# while(i<11):
#     print(i)
#     i+=2;

# printing table as per user input
n=int(input("enter a number\n"))
i=1
while(i<n):
    print("the table of ",n,"is:", i)
    i+=n * i
