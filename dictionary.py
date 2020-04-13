# dictonary is nothing but a key value pair
"""
d1=()
print(type(d1))
d2=[]
print(type(d2))
d3={}
print(type(d3))


dic={"harry":"hariom", "alok":"feku", "mayank":"gaperi", "pandey":"dhilu", "stud":{"morning":"breakfast", "afternoon":"lunch","evening":"study"}}
print(dic["harry"],"\n")
print( dic,"\n")
print(dic["stud"],"\n")
print(dic["stud"]["afternoon"])

har={"mayank":"friend", "alok":"friend", "pandey":"music", "harry":{"hobby1":"python", "hobby2":"music", "hobby3":"arijit"} }
print(har,"\n")

print(har["harry"]["hobby3"])
#this means thst har ek dictonary hai, usme harry ek  key hai jiska value khud ke dictonay contain kr rha hai.
#sub dictionary ko access krne ke liye, main dictorany[key][subkey]

#adding and removing elements from dictonary
a={"mayank":"friend", "alok":"friend", "pandey":"music", "harry":{"hobby1":"python", "hobby2":"music", "hobby3":"arijit"}}
a["mohak"]="dost"

print(a ,"\n")
print(a["harry"]["hobby3"],"\n")
print("adding dictionary nitish")
a["nitish"]="dost1" #a["key"]=["value"]  --> to add an item to dict
print(a,"\n")

print("deleting nitish by del method")
del a["nitish"] #del a[key] --> to delete an item from dict
print(a) """
"""
print("copy method observations\n\n")
h={10:15,36:856,"hariom":"hk", "harry":"hariom"}
print("printing value of h", h["harry"],"\n\n")
h1=h
print("copying the value of h into h1 and will print the same value of h and if we remove data from h1 the same will be removed from h too\n\n")
print(h1)
print("now deleting the values from h1 and the value will be removed from h also \n\n")
print("before deleting the value of h are:- \n",h,"\n \n")
del h1[10]
print("after deleting the values of h are:-\n",h,"\n \n")

print("if we want to perform copy function but din't allow to change in the original value using copied dict\n\n")
print("for this we have to write like that dict2.dict.copy() , this will restrict any changes into the original value\n\n")
h1=h.copy()
print("value of h1:-\n\n",h1)
print("value of h:-\n\n",h)
print("now deleting values from copied dict, lets see the is the original value getting affected or not?\n\n")
print("before deleting the original values are:-\n ", h,"\n \n")
del h1["hariom"]
print("after deleting the value of h1 are :-\n ", h1,"\n \n")
print("after deleting the original values are did't get affected:-\n ", h,"\n \n")

print("now perfoming another type of copy method dict3=dict2.copy():-\n \n, it will not let change the original value if we made any change in the copied value")
h2=h.copy()
print("beofe deleting the value of h2(copied) is:-\n", h2,"\n \n")
print("beofe deleting the the original value is:-\n ", h,"\n \n")
del h2[36]
print("after deleting the copied value is:-\n", h2,"\n \n")
print("after deleting from the copied value the,  original value didn't affected:-\n", h,"\n \n") """

# updating the dictonary,, adding new keys and values in dictonary
hh = {10: 15, 36: 856, "hariom": "hk", "harry": "hariom"}
print("before update the dict hh has value:-\n", hh, "\n\n")
hh.update({"moni": "das", "tonu": "das"})
print("after updating the dict hh has new value:-\n", hh, "\n\n")
hh.update({"ravi": "brother", "jit": "elder-brother"})
print("updating the dict again\n")
print(hh)
print("printing all the keys")
print(hh.keys())

print("printing all the values")
print(hh.values())
print("printing all the items")
print(hh.items(),"\n\n")
hh.pop(36)
print("pop(key) will remove particular key value\n ")
print(hh)

