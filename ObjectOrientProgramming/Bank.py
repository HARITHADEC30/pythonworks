class bank:
    name:str
    account_no:int
    ac_type:str
    customer_name:str
    balance:int

    def __init__(self,name,account_no,ac_type,customer_name,balance):

        self.name=name
        self.account_no=account_no
        self.ac_type=ac_type
        self.customer_name=customer_name
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"your account {self.account_no} has been credited with amount {amount} avl balance {self.balance}")

    def withdraw(self,amount):
        if self.balance<amount:
            print("insufficiant balance")
        else:
            self.balance-=amount
            print(f"youe account {self.account_no} has been debited with amount {amount}")

    def get_balance(self):
        print("your avliable balnce",self.balance)

bank_instanse=bank("SBI",6326734847,"International","Haritha dasan k",8000)
bank_instanse.deposit(2000)
bank_instanse.withdraw(5000)
bank_instanse.get_balance()

        
