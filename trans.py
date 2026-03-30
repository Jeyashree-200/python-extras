iamount=int(input("enter ini balance:"))
choice=int(input("enter mode of transaction(1.deposit/2.transaction)"))
tamount=int(input("enter transaction amount"))
if choice==1:
   if tamount>=1000:
      u=iamount+tamount
      print("deposit completed")
      print("upd balance",u)
   else:
      print("not possible tamount is less than 1000")
else:
   u=iamount-tamount
   if u>=1000:
      print("withdarwal completed")
      print("upd balance",u)
   else:
      print("not possible min balance is less than 1000")
