#firstly printing a statment using both loops

#k=0
#while(k<45):
#	print(k,"hello harry")

#	k+=1
#	print("\t")

#for i in range(45):
#	print(i,"hello hariom")
#	print("\t")

#now finding time taken by these loops to execute.
#for this we have to import the time module and a function inside time will
#measure time in seconds...time.time()
#for this we will make a initializtion time and will subtract execution from main time

#time.sleep(n) -->by passing the n in seconds the execution will take that much time of interna to execute
#search for time module documentation
import time

whiletime=time.time()
k=0
while(k<10):
	print("Harry! this is line no-",k)
	print("the next line will be print after 2 seconds")
	time.sleep(2)
	k+=1
print("time taken by while loop is", time.time()-whiletime,"seconds")

fortime=time.time() 
for i in range(10):
	print("Hariom! this is line no ", i)
print("time taken by for loop is ", time.time()-fortime,"seconds")

"""
#finding our local time
import time
ltime=time.asctime(time.localtime(time.time()))
print(ltime)
#here it will print our computer local time .
#time.localtime(time.time() this returns a tuple
#asctime will convert the returning value into a standard format.
"""
