l=[10,20,30,40,50,60,70]
print("before reverse :",l)
n=len(l)
s=n//2
for i in range(n//2):
  l[i],l[n-1-i]=l[n-1-i],l[1]
print("after reverse :",l)
