#making as save and return file for your personal details
def gettime():
    import datetime
    return datetime.datetime.now()

def your_detail(d):
    if (d==1):
        e = int(input("enter 1. for food and \n2. for Drink"))
        if(e==1):
            value=input("enter your details\n")
            with open("hariom-food.txt","a") as z:
                z.write(str([str(gettime())])+":"+value+"\n")
                print("your data saved successfully\n")
        elif(e==2):
            value=input("enter your details\n")
            with open("hariom-drink.txt","a") as z:
                z.write(str([str(gettime())]) + ":" + value + "\n")
                print("your data saved successfully\n")
    elif(d==2):
        e=int(input("enter 1 for food and \n 2 for drink\n"))
        if(e==1):
            value=input("enter your details\n")
            with open("mayank-food.txt","a") as z:
                z.write(str([str(gettime())]) + ":" +  value + "\n")
                print("your data saved successfully\n")
        elif(e==2):
            value=input("enter your details\n")
            with open("mayank-drink.txt", "a") as z:
                z.write(str([str(gettime())]) + ":" + value + ":")
                print("your data saved successfully")
    elif(d==3):
        e=int(input("enter 1 for food and\n 2 for drink\n"))
        if(e==1):
            value=input("enter your details\n")
            with open("alok-food.txt", "a") as z:
                z.write(str([str(gettime())]) +":" + value + "\n")
                print("your data saved successfully\n")
        elif (e == 3):
            value = input("enter your details\n")
            with open("alok-drink.txt", "a") as z:
                z.write(str([str(gettime())]) + ":" + value + ":")
                print("your data saved successfully")
    else:
        print("enter correct input\n")



def printout(d):
    if(d==1):
        e=int(input("enter 1 for food and\n 2 for drink\n"))
        if(e==1):
            with open("hariom-food.txt") as z:
                for text in z:
                    print(text, end="")
        elif(e==2):
            with open("hariom-drink.txt") as z:
                for text in z:
                    print(text, end="")
    elif(d==2):
        e = int(input("enter 1 for food and\n 2 for drink\n"))
        if(e == 1):
            with open("mayank-food.txt") as z:
                for text in z:
                    print(text, end="")
        elif(e == 2):
            with open("mayank-drink.txt") as z:
                for text in z:
                    print(text, end="")

    elif(d == 3):
        e = int(input("enter 1 for food and\n 2 for drink\n"))
        if(e == 1):
            with open(("alok-food.txt")) as z:
                for text in z:
                    print(text, end="")
        elif(e == 2):
            with open("alok-drink.txt") as z:
                for text in z:
                    print(text, end="")
    else:
        print("enter correct input\n")

print("Welcome to daily health management system\n")
a=int(input("enter 1 for adding your detail\n"
                "enter 2 for seeing your detail\n"))
if a==1:
        k=int(input("enter 1. for hariom\n 2. for mayank and \n 3.for alok"))
        your_detail(k)
else:
        k=int(input("enter 1. for hariom\n 2. for mayank and \n 3.for alok"))
        printout(k)
