#global variable and global keywords
# i=10 #--> here 'i' is global(scope) variable which can be used anywhere in the program
# def fun1(n):
#     i=5 #local scope
#     j=10
#     print(i,10) # here the output will be 5, 10 becuase for this function i and j are his local variable and will access those only.
#     print(n,"hello harry")
# local variables cant be print outside the function.
# global variable cannot be modified inside the function , becuase locally the global function read only access.
# if we wish to modify the global variable as locally, we have to use 'global' keyword , thenafter we can change the value.
# fun1("this is harry ")
# print(i)


# nesting of function--> calling a function inside another funciton.

def fun2():
    x=20
    def fun3():
        global x
        x=30
        print("before calling fun3 ",x)
        fun3()
        print("after calling fun3", x)
        # here the output for x will be same in both the cases, becuase 'global x' is not present, it will search for
        # global search .
# suppose if we define a global scope x outside the function then the value can be modified.

x = 45
def fun2():
    x=20

    def fun3():
        global x
        x=30
        # print("before calling fun3 ",x)
        fun3()
        print("after calling fun3", x)
# here a global variable x is 45. and we are changing it in locally and it will do change this time.
fun2()
