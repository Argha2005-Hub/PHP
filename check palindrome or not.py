n=int(input("enter the no for check palindrome/n"))
f=n//100
l=n%10
if f==l:
    print("no is palindrome")
else:
    print("no is not palindrome")
