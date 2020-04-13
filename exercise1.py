#faulty calculator
#make a calculator which ask to user about opeator and will give the desired output acept these operations.
#40*3=300; 10+4=16; 10/5=23; 100-40=15

print("                                     welcome to faulty calculator")
print("choose any one\n"
      " add\n "
      "sub\n"
      "mul\n"
      "div\n")

a=input()
b = int(input("enter first number:- "))
c = int(input("enter second number:- "))

if a=="add":

    if (b==10 and c==4):
        print("the sum is 77 ")
    else:
        # b+=c
        b = b + c
        print("the sum is ",b)

    c=int(input("enter number to add again\n"))
    b= b+c
    if c:
        print("the sum is:",b)
    else:
        print("thanks for adding")


elif a=="sub":

    if (b==100 and c==40):
        print("the substraction is:- ",b-c)

    else:
        print("the substraction is:- ", b-c)
elif a=="mul":
    if (b==40 and c==3):
        print("the multiplication is - ", 300)
    else:
        print("the multiplication is- ", b*c)
elif a=="div":
        if b==0:
            print("first value can't be zero " )
            exit(1)
        elif (b==10 and c==5):
            print("the division is - ", 23)
        else:
            print("the division is- ",b/c)
else:
    print("choose the right operations option")

print("thanks for using faulty calculator")
