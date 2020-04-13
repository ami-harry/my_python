var1="hello harry "
var2=10
var3=20.91
var4="mmm"
var5="21"
var6="323"
print(var1 + var4)
print(var2 + var3)
print(type(var1))
print(type(var2))
print(type(var3))
print(var1 + var5)
print(var5 + var6)#in this both strings gets concantinate. so add function wasn't happend.
#to see the sum as output of the string we have to use typecast.
print(int(var5) + int(var6))
"""
int()   string()    float()///////print(int(var))
"""
#to print any statement many times.
#simply multiply the string by that no.
print(100*"hariom\t")
var7="10"
var8="15"
print(10 * int(var7) + int(var8)); """this will simply get multipled by first variable and will
not print the desired output, we have to typecast it to string"""
print(10 * str(int(var7) + int(var8)))


