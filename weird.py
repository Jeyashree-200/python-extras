n=int(input("enter n"))
if n%2==1:
   print("it is weird")
elif n>=0 and n<=20:
   print("it is not weird")
elif n>=21 and n<=40:
   print("weird")
elif n>40:
   print("not weird")
else:
   print("negative no")
