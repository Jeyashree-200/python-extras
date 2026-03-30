print("enetr 5 subject marks")
t=0
for i in range(1,6):
    m=int(input("enter the mark"))
    t=t+m
print("aggregate(total)=",t)
per=(t/500)*100
print("per",per)
if per>=90:
    print("grade 0")
elif per>=80:
    print("grade A+")
elif per>=70:
    print("grade A+")
elif per>=60:
    print("grade B+")
elif per>=55:
    print("grade B")
elif per>=50:
    print("grade C")
else:
    print("invalid")
