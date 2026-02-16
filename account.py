class account:
    def __init__(self,acc_no,balance,out,inm):
        self.acc=acc_no
        self.balance=balance
        self.out=out
        self.inm=inm

    def debit(self):
        
        money=self.balance-self.out
        print(money)
    
    def credit(self):
        money=self.balance+self.inm
        print(money)
    def showbal(self):
        print(self.balance)

user=input("enter w to withdraw , a to add,c to check balance:")
if(user=="w"):
    s1=account(122312,500,1,1)
    s1.out=int(input("enter the amount to withdraw:"))
    s1.debit()

elif(user=="c"):
    s1=account(122312,500,1,1)
    s1.showbal()
   

else:
    s1=account(122312,500,1,1)
    s1.inm=int(input("enter the amount to add"))
    s1.credit()
