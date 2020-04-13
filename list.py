"""list=["pen", "paper", "book", 100, "biscuits" ]
print("the list items are" , list)
print("at 5 index the item is , indexing begins from 0", list[4])
num=[10,2,4,6,2,6,33,66,44]
print(num)
print("num at 4 is", num[5])
#print(num.sort()) will give none. becuase we have to sort it before printing
num.sort()
print("numbers after sorting ", num)
num.reverse()
print("numbers after reverse ",num)
print("if we use sort, reverse method , the original list gets changed but while slicing the list the original value didn't get affected")
nm=[10,1,3,5,6,7,22,34,6,7,88]
print(nm[0:4])
print(nm[::])
print(nm[::-1]) #this will reverse the string
print(nm[::-2])
print(nm[2:4])
print("do not use more than -1  value while slicing the values, otherwise you will face error")
nbr=[1,2,5,667,3,23,2342,53]
#nbr.append(55)
#nbr.append(99) #append add a number at the end  of the list
print(nbr)
print(len(nbr))
print(max(nbr))
print(min(nbr))
to add new numbers--> use append
#--> by using insert() we can add a digit by index no
digit=[10,37,42,48,38,20]
print(digit)
digit.insert(3,11)
print(digit)
digit.remove(11)
print(digit)
digit.pop()#this will remove last digit
print(digit)
digit[3]=100
print(digit)
digit[2]=20
digit.pop()
print(digit)

tp=(1,)
print(tp)
#swapping of two numbers
a=1
b=2
temp=a
a=b
b=temp
print(a,b) """

a=1
b=2
print("before swap the values are- ",a,b)
a,b=b,a
print("after swap the values are- ",a,b)