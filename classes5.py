class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        deposit = int(input("Enter the number of deposit here: "))
        self.balance = self.balance + deposit
        print(self.owner+", your balance is: "+ str(self.balance)+"$")
    def withdraw(self):
         withdraw = int(input("Enter the amount of money you want to withdraw: "))
         if(withdraw > self.balance):
             print("Your withdrawal is exceeding the available balance, deposit to withdraw ")
             return Account.deposit(self)
         if(withdraw == self.balance or withdraw<self.balance):
             self.balance = self.balance - withdraw
             print("-"+str(withdraw)+"$")
             print("Your current balance is:" + str(self.balance)+"$") 
txt = input("Enter account name: ")
acc1 = Account(owner = txt, balance=0)
acc1.deposit()
i = 1
while i != 0:
    operation = input("Enter the next operation; type 'd' to deposit;type 'w' to withdraw; type 'e' to exit: ")
    if(operation == "d"):
        acc1.deposit()
    elif(operation == "w"):
        acc1.withdraw()
    elif(operation == "e"):
        break
    else:
        print("invalid operation!")
