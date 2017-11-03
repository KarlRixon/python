dict1={}
dict1=dict1.fromkeys(range(10),'赞')
for eachkey in dict1.keys():
    print(eachkey)
    
for eachvalue in dict1.values():
    print(eachvalue)
    
for eachitem in dict1.items():
    print(eachitem)
    
print(dict1.get(32,'木有！'))
print(31 in dict1)
dict1.clear()
print(dict1)
a={'a':1}
b=a
a={}
print(a,'\n',b)
a=b
b.clear()
print(b,'\n',a)
c=a.copy()
print(id(a),id(b),id(c))
