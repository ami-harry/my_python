# list1=["harry", "mayannk", "alok"]
 # print(list1)
 # print(list1[2])

 # for item in list1:
 #     print(item)

#-->list of list
# h=[["hk",20],
#    ["rk", 25],
#    ["dk",36],
#    ["jk",31]]
# print("this is list of list\n")
# for name, age in h:
#     print("your name is -", name," and your age is-",age)

# #list of tuple
# h1= [(1,(2)),
#      (4,(5)),
#      (6,(7))]
# for nm in h1:
#     print("this is an example of list of tuple, here we can print valus as per indexing like-->(0(1))--< or normally")
#     # print(nm[0],"\n",nm[1])
#     print(nm)

#tuple
# h3=(1,3,4,5,6,7,8,)
# print("this is a simple tuple")
# for num in h3:
#     print(num)

# tuple of tuple
# print("this is tuple of tuple")
# h4=(('hh'),((2,(3,(4,(5,(6,(7,('hk')))))))))
# for num in h4:

# printing dict items
# list1=[["hk",21],
#        ["rk", 25],]
# dict1=dict(list1)
# print(dict1)
# for item,age in dict1.items():
#     print(item, age)
# print("to print dict we have to use dict.items() method to get the correct output")


# dict of tuple
# ls= [["6","1"],["9","value2"],
#     ["8","value1"],["7","value4"]]
# dict2=dict(ls)
# for  key, value in dict2.items():
#      print(key,value)
     # print(key)
     # print(value)

# printing items with certain condition
# list1=["harry", "hariom",1,5,6,-8,18,16,10,11,55,44]
# for numb in list1:
#     if str(numb).isnumeric() and numb>=10:
#         print(numb)


# printing only positive numbers
# list1=[10,15,6,7,8,-11,11,0,103,-11]
# print("items of the list are-", list1)
# print("\n\nall +ve numbers are ")
# for positive in list1:
#     if positive >=1:
#         print(positive)


# prrinting number from 1 to 100
#
# for i in range(1,101):
#     print(i)


# printing table of number
num=int(input("enter your number\n"))
for i in range(1,11):
    print(num,"x",i,"=", num*i)


num=int(input("enter the number again to see the table"))

for i in range(1,11):
    print(num,"x",i,"=", num*i)
