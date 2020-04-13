#wap to check whether input number is greater or lesser
"""
print("enter value for a\n")
a=int(input())
print("enter value for b\n")
b=int(input())
if b>a:
    print("b is greater")
elif b==a:
    print("both are equal")
else:
    print("b is lesser")

#in keyword
print(" 'in' keyword simply do a search in list that the enterd no is present in the list or not")
print("if no is present in the list, it will return true , otherwise false\n\n")
list1=[5,22,55,6,7,4,222]
print("the values of list are -->",list1,"\n")
print(5 in list1,  "becuase 5 in present in the list") #--> it will return true becuase 5 is present in the list
print(11 in list1, "becuase 11 is not present in the list") #--> it will say false becuase 11 is not in the list
if 5 in list1:
    print("\nyes, 5 is present in list\n") """

#not in keyword
print(" 'not in' keyword simply do a search in list that the enterd no is present in the list or not")
print("if no is present in the list, it will return true , otherwise false\n\n")
list1=[5,22,55,6,7,4,222]
print("the values of list are -->",list1,"\n")
print(5 not in list1,  "becuase 5 in present in the list") #--> it will return true becuase 5 is present in the list
print(11 not in list1, "becuase 11 is not present in the list") #--> it will say false becuase 11 is not in the list
if 15 not in list1:
 print("\nyes, 15 is not is not in the list")

