l=[10,20,30,40,50]
print("before sort : ",l)
for i in range(len(l)-1):
        if l[i]<l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
print("after sort : ",l)
