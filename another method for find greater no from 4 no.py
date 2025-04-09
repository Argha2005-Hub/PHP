a= float(input("Enter first number: "))
b= float(input("Enter second number: "))
c= float(input("Enter third number: "))
d= float(input("Enter fourth number: "))
if a>b and a>c and a>d:
    print("a is greater")
elif b>c and b>d :
    print("b is greater")
elif c>d:
    print("c is greater")
else:
    print("d is greater")
