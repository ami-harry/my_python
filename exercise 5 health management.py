def gettime():
    import datetime
    return datetime.datetime.now()
def submit(k):
    if k==1:
        c=int(input("Enter 1 for exercise"
                    " and 2 for Food"))
        if(c==1):
            value=input("Type here\n")
            with open("harry-ex.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("successfully saved your data")
        elif(c==2):
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully saved your data")
        else:
            print("enter correct input\n")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully saved your data")
        elif(c==2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully saved your data")
        else:
            print("enter correct input\n")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully saved your data")
        elif(c==2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully saved your data")
        else:
            print("enter correct input\n")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(p):
    if p==1:
        c=int(input("enter 1. for exercise and\n 2. for food"))
        if(c==1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
             print("enter correct input\n")
    elif(p==2):
        c = int(input("enter 1. for exercise and\n 2. for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
        else:
            print("enter correct input\n")
    elif(p==3):
        c = int(input("enter 1. for exercise and \n 2. for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c==2):
            with open("hammad-food.txt") as op:
                for i in op:
                   print(i, end="")

        else:
            print("enter correct input\n")
    else:
        print("plz enter valid input (harry,rohan,hammad)")

print("Health Management System: ")
a=int(input("enter 1 to enter your detail and \n 2. to see your details \n"))
if a == 1:
    b = int(input("press 1. for Harry\n 2. for Rohan \n 3. for Hammad\n "))
    submit(b)
else:
    p = int(input("press 1. for Harry\n 2. for Rohan \n 3. for Hammad\n "))
    retrieve(p)