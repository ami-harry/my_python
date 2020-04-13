# function in python
# inside a python function it must contain a list/tuple/or an iterable input
# functions are of two types
# a. pre-defined functions and
# b. user defined functions

# to make a user defined functions we have to use 'def' keyword before the function name and
# must return value from the function otherwise it will return none.:)
#  for our simplicity we can give its doc_string means describing functionality of the function,
#  actually what it is defined for
# to see the doc_string of the function, don't use () after function name while printing
# use fun[dot]_doc_ --> to see its description

#def fun1():
#print("hello, you are in fun1")
# print(fun1())

#here the output will be --> hello, you are in fun1....none  ,, becuase we didn't return anything so
#bydefault it returned none


# def fun2(a,b):
#     sum=a+b
#     print("the sum of a and b is",a+b)
#     return sum
# c=fun2(4,5)
# print(c)
# here the function is taking two nos and it is call by value function and returning the sum of a and b and storing the
# sum in another variable c and printing the c to see the sum result


# def fun2(a,b):
   # """this function will add two number
   # and will not work for three numbers"""
    # sum=a+b
    #print("the sum of a and b is",a+b)
#     return sum
# c=fun2(4,5)
# print(c,fun2.__doc__)
# here the sum of a abd b will be printed then after doc_script of the function will be printed
