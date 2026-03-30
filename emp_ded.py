sal=int(input("enter empl salary"))
t=int(input("enter no of leave days"))
if t<=2:
   print("no deduction")
   print("final salary")
else:
   ded=(t-2)*500
   fsal=sal-ded
   print("final salary after deduction",fsal)


[25bcs140@mepcolinux py]$cat py14.py
for i in range(1,5):
      for j in range(1,i+1):
              print(j,end='\t')
              print(end='\n')
