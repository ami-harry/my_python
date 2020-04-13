#taking input from the user and printing different types of output
print("enter a number")
inp=input()
#print("your number is:",inp+10) this will through an error becuase both are of different type. str and int
#to get output after adding something in it, we have to typecast it into int
print("your number is as int:",int(inp) + 10)
print("your number is as float:",float(inp) + 10.5)
print("your number is as string:",(inp) + str(10.5))

