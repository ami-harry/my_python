# break and continue
# continue will check the condition unitill its gets true and will escape printing statement till true condition
i=1
while(True):
    if i+1 <10:
        i+=1
        continue
    print(i, end=" ")
    if(i==44):
        break
    i+=1