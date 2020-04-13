set1={10,15,20,25}
print("elements of the set is:-",set1)
print("type of the set is:-", type(set1))
print("lenght of the set is- ",len(set1))
print("maximum element of the set is:- ",max(set1))
print("minimum element of the set is:- ",min(set1))
print("adding elements to the set--> set1.add(element)-")
set1.add(11)
set1.add(14)
print("the updated set after adding element:-",set1)
print("removing elements from the set--> set1.remove(element)-")
set1.remove(14)
print("the updated set after removing elemnt:-",set1)

print("if we add same value for twice it will add only once, becuase set always retains unique value")
set1.add(29)
set1.add(29)
print("the updated set is:-", set1)
#set2={55,56,57,58}
#uniom of sets
print("union will add the elements of loacting set after the union elemnts")
set2={11,12,14,15}
set3=set2.union({55,56})
print(set3,set2)


