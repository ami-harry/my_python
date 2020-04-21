# take input from user and print start in ascending form otherwise print in descending order

first=int(input("enter how many time you want to print"))
second=int(input("enter 1 for true"))
new=bool(second)
if new == True:
    for i in range(1, first+1):
        for j in range(1, i+1):
            print("*", end="")
        print()
elif new == False:
    for i in range(first,0, -1):
        for j in range(1,i+1):
            print("*", end="")
        print()
