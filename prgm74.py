
class Bank:
    def __init__(self,num=0,n='guest',t='normal',b=0):
        self.number=num
        self.name=n
        self.type=t
        self.balance=b
 
    def deposit(self):
        amount=float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\nAmount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("\nEnter amount to be withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance")
 
    def display(self):
        print("\n Account number:",self.number)
        print("\n Name=",self.name)
        print("\n Type=",self.type)
        print("\n Balance=",self.balance)
 

s = Bank(111,"Aiswarya","Savings",20000)
s.deposit()
s.withdraw()
s.display()
