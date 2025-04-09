n=int(input("enter a number to check perfect\n"))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print("number is perfect")
else:
    print("number is not perfect")
