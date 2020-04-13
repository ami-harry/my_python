# input no is prime or not
num=int(input("enter a number\n"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not prime")
            break
        else:
            print(num,"number is prime")

if num<=1:
    print(num," is not prime")












