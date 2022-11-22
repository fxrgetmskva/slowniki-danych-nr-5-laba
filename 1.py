values=[10,20,30]
keys=["Ten","Twenty","Thirty"]
#D1=dict(zip(keys,values))
#print(D1)
#print(list(zip(keys,values)))
D1={}
#for i in range (len(keys)):
#    D1[keys[i]]=values[i]
#print(D1)
D1={keys[i]:values[i] for i in range (len(keys))}
print(D1)

D2 = dict(trzydzieśći=30,czterdzieśći=40,pięćdziesiąt=50)
print(D2)


D3 ={}
D3=D1.copy()
D3.update(D2)
print(D3)