# making daily life expense routine
def gettime():
    import datetime
    return datetime.datetime.now()

def give_data(d):
    if(d==1):
        c=int(input("enter options to save details\n"
                    "1. item name\n"
                    "2. price\n"
                    "3. method of payment\n"
                    "4. others\n"))
        if(c==1):
            value=input("enter item name :\n-")
            with open("item.txt","a") as data:
                data.write(str([str(gettime())])+":"+value+"\n")
                print("your item name is successfully added\n")
        elif(c==2):
            value=input("enter price of the item\n")
            with open("price.txt", "a") as data:
                data.write(str([str(gettime())])+":"+value+"\n")
                print("your price has been successfully added\n")
        elif(c==3):
            value=input("enter your method of payment\n")
            with open("mode-of-payment.txt","a") as data:
                data.write(str([str(gettime())])+":"+value+"\n")
                print("your mode of payment has benn successfully saved\n")
        elif(c==4):
            value= input("enter your other items name\n")
            with open("other.txt","a") as data:
                data.write(str([str(gettime())])+":"+value+"\n")
    else:
        print("enter correct input\n")

def pri(p):
    if(p==1):
        c=int(input("choose the options to see the details of\n"
                    "1.item name\n"
                    "2.price of the item\n"
                    "3.method of payment\n"
                    "4.other items\n"))
        if(c==1):
            with open("item.txt") as data:
                for text in data:
                    print(text)
        elif(c==2):
            with open("price.txt") as data:
                for text in data:
                    print(text)
        elif(c==3):
            with open("mode-of-payment.txt") as data:
                for text in data:
                    pri(text)
        elif(c==4):
            with open("other.txt") as data:
                for text in data:
                    print(text)
    else:
        pri("enter correct input\n")
"""def all(z):
    if(z==1):

       a=int(input("enter 1 to see all details at once"))
       if(a==1):
            with open("item.txt") as d:
                for t in d:
                    print(t)
            with open("price.txt") as a:
                for e in a:
                    print(e)
            with open("mode-of-payment.txt") as t:
                for x in t:
                    print(x)
            with open("other.txt") as a1:
                for t1 in a1:
                    print(t1)

    else:
        pri("enter valid input")"""



print("Welcome to daily life expense diary\n")


i=int(input("choose the option:\n"
            "1.to add your data\n"
            "2.to see your data\n"))
            # "3.to see all details"))

if i==1:
    d=int(input("choose the option to add:\n"
            "1. Item name\n"
            "2. Price of the item\n"
            "3. Mode of payment\n"
            "4. Other items\n"))
    give_data(d)
elif i==2:
    p = int(input("choose the option to know about:\n"
                  "1. Item name\n"
                  "2. Price of the item\n"
                  "3. Mode of payment\n"
                  "4. Other items\n"))
    pri(p)
# elif i==3:
#     z=int(input("enter 1 to see all details at once"))
#     all(z)
else:
    print("enter valid input")

