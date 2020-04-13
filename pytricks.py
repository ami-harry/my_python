dic={'a':10, 'b':1, 'c':15}


import operator
sorted(dic.items(), key=operator.itemgetter(1))
print("original dic is-\n",dic)
print("\n",dic.keys())
print("\n",dic.values())
