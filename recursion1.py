# recursion means function calling itself

# lets take an example of factorial
# using iterative method
"""
def fact_int(n):
#     """
#     :param n: an integer
#     :return: n*(n-1)(n-2)*(n-3)....1
#     """
	fact=1
     	for i in range(n):
        	fact=fact*(i+1)
     	return fact
num=int(input("enter value for n\n"))
print("factorial of number using iterative method is-", fact_int(num))
"""
"""
# factorial using recursive method
"""def fact_rec(n):

     if n==1:
         return 1
     else:
         return n*fact_rec(n-1)
num=int(input("enter the value of num "))
print("the factorial of n using recursive method is ", fact_rec(num))
"""
# fibonacii series using recursion
# print("fibonacii series is 0 1 1 2 3 5 8 13 21 34 55 ... indexing starts from 0")
"""def fib(n):
     if n==0:
         return 0
     elif n==1:
         return 1
     else:
         return fib(n-1)+fib(n-2)
num=int(input("enter value for n "))
print("the sum of fibonacii series of",num,"is", fib(num))
"""

















#finding factorial using recursive method
"""def fac_rev(n):
	if n==0:
		return 1
	elif n==1:
		return 1
	else:
		return n*fac_rev(n-1)

it=int(input("enter the number"))
print("the factorial of the",it,"is:", fac_rev(it))
"""
"""
def fac(n):
	facn=1
	for i in range(n):
		fac=fac*(i+1)
		return fac

ii=int(input("enter the number"))
print("the factorial of",ii," is ",fac(ii))
	"""
	



