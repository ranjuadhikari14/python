class BankAccount:
   def __init__(self,name,phone,balance=0.0):
      self.name=name 
      self.phone=phone
      self.balance=balance

   def deposit(self,amount):
        if amount>=0:
            self.balance +=amount
            print(f"successfully deposit amount is {amount} to {self.name} account")
        else:
            print(f"invalid transcation,something went wrong")

   def withdraw(self,amount):
        if 0<amount<= self.balance:
            self.balance-=amount
            print (f"withdraw ${amount:.2f} from {self.name}'s account")
        else:
            print("invalid balance or Insufficient balance")

   def get_amount(self):
       return f"{self.name}'s current balance : ${self.balance:.2f}"

ram=BankAccount(name="ranju adhikari",phone=9876545667)
ram.deposit(500000)
ram.withdraw(20000)
print(ram.get_amount())

hari=BankAccount(name="hari thapa",phone=987772722)
hari.deposit(30000)
hari.withdraw(20000)
print(hari.get_amount())