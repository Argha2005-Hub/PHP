s=input("enter a single charecter string/n")
vowel_str="aeiouAEIOU"
consonent_str="bcdfghjklmnpqrstwxyzBCDFGHJKLMNPQRSTWXYZ"
if s in vowel_str:
    print("it is vowel")
elif s in consonent_str:
     print("it is consonent")
else:
    print("it is invalid charecter")
