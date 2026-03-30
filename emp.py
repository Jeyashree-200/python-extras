sal=int(input("enter empl salary"))
t=int(input("enter no of leave days"))
if t<=2:
   print("no deduction")
   print("final salary")
else:
   ded=(t-2)*500
   fsal=sal-ded
   print("final salary after deduction",fsal)
