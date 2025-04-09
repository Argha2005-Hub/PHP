n=int(input("enter the no to check it is prime or not\n"))
flag=True
i=2
while i<n:
    if n%1==0:
        flag=False
        break
    i+=1
if flag:
    print("it is prime")
else:
    print("NO IS NOT PRIME")
