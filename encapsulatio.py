class Account:

    def __init__(self,balance):
        self.___balance = balance

    def get_balance(self):
        return self.___balance

account = Account(5000)
print(account.get_balance()) 
