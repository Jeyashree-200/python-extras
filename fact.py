num=int(input("enter the number"))
factorial=1
if num<0:
    print("factorial of negative number is not possible")
elif num==0:
    factorial=1
else:
    factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print("factorial",factorial)
