def gettime():
    import datetime
    return datetime.datetime.now()

def give(v):
    if v==1:
        c=int(input("enter   1. for exercise\n"
                    "2. for food\n"))
        if(c==1):
            value=input("enter your detail")
            with open("Harry-ex","a") as data:
                data.write(str([str(gettime())]) + ":" + value + "\n")
            print("your data have been saved successfully")
        elif(c==2):
            value=input("enter your detail")
            with open("Harry-food.txt","a") as data:
                data.write(str([str(gettime())]) + ":" + value + "\n")
        print("your data have been saved successfully")
    if(v==2):
        c = int(input("enter   1. for exercise\n"
                                "2. for food\n"))
        if(c == 1):
            value = input("Enter your detail")
            with open("Mayank-ex", "a") as data:
                data.write(str([str(gettime())]) + ":" + value + "\n")
            print("your data have been saved successfully")
        elif(c==2):
            value = input("enter your detail")
            with open("Mayank-food.txt", "a") as data:
                data.write(str([str(gettime())]) + ":" + value + "\n")
            print("your data have been saved successfully")
    if(v==3):
        c = int(input("enter   1. for exercise\n"
                               "2. for food\n"))
        if(c == 1):
            value = input("Enter your detail")
            with open("Alok-ex", "a") as data:
                data.write(str([str(gettime())]) + ":" + value + "\n")
            print("your data have been saved successfully")
        elif(c==2):
            value = input("enter your detail")
            with open("Alok-food.txt", "a") as data:
                data.write(str([str(gettime())]) + ":" + value + "\n")
            print("your data have been saved successfully")
    else:
        print("enter valid input")


def print(v):
    if(v==1):
        c=int(input("Enter 1. for exercise" 
                            "2. for food "))
        if(c==1):
               with open("Harry-ex.txt") as data:
                for i in data:
                    print(i)
        elif(c==2):
            with open("Harry-food.txt") as data:
                for text in data:
                    print(text)
    if(v==2):
        c=int(input("Enter 1. for exercise" 
                           "2. for food "))
        if(c==1):
               with open("Mayank-ex.txt") as data:
                for text in data:
                    print(text)
        elif(c==2):
            with open("Mayank-food.txt") as data:
                for text in data:
                    print(text)

    if(v==3):
        c=int(input("Enter    1. for exercise" 
                             "2. for food "))
        if(c==1):
               with open("Alok-ex.txt") as data:
                for text in data:
                    print(text)
        elif(c==2):
            with open("Alok-food.txt") as data:
                for text in data:
                    print(text)
    # else:
    #         print("enter a valid input")

print("welcome to health management\n ")
a=int(input("enter   1. for saving the details\n"
                    "2 for seeing the details.\n"))
if(a == 1):
     b=int(input("press 1. for Harry\n"
                        "2. for  Mayank\n"
                        "3 for Alok\n"))
     give(b)
else:
    b = int(input("press 1. for Harry\n"
                        "2. for  Mayank\n"
                        "3 for Alok\n"))
    print(b)
