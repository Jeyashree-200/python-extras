a=int(input("enter the 1st num"))
b=int(input("enter the 2nd num"))
n=a*b
if n<=1000:
   print("the product is",n)
elif n>1000:
   n=a+b
   print("the sum is",n)
else:
   print("invalid")
