#swapping of list having 2 values
print("using slicing  method of list")
swap=[2,4]
print("before swapping the values of list are-", swap)
print("after swap the value of list are:-", swap[::-1])
print("\n")
#swapping of string having two values
print("using slicing method of string")
swap1="h,k"
print("before swap the string is:-", swap1)
print("after swapping the string is:- ", swap1[::-1])

print("\n using temp")
a=1
b=2
print("before swapping the values are:- ", a,b)
temp=a
a=b
b=temp
print("after swapping the values are:-", a,b)
print("\n using python simple method")
a=1
b=2
print("before swapping the values are:-", a,b)
a,b=b,a
print("after swapping the values are:-", a,b)