# wap which accepts input until the input is less than 100
# a=0
# while(a<100):
#     a=int(input("enter a number"))
#     continue
# print("congratulations, you have entered correct range")

#
print("enter a number greater than 100\n")
while(True):
    num=input("enter a number\n")
    if int(num)>100:
        print("congratulations, you have entered correct range")
        break
    else:
        print("oops!!try again!\n")
        continue