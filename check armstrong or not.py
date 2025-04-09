n=int(input("enter a number to check armstrong/n"))
d1=n%10
d2=n//10%10
d3=n//100
new_n=d1**3+d2**3+d3**3
if n==new_n:
    print("number is armstrong")
else:
    print("number is not armstrong")
