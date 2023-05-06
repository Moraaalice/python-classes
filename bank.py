class Bank:
    bank_name="Equity"
    def __init__(self,account_name,account_number,amount):
        self.account_name=account_name
        self.acount_number=account_number
        self.amount=amount
        
    def bank_details(self):
        return f"Your account name is {self.account_name},{self.acount_number},has a balance of {self.amount}"
    def account_balance_after_deposit(self,deposit):
        new_balance=deposit+self.amount
        return f"Your new balance is {new_balance}"
    def account_balance_after_withdrawal(self,withdrawal):
        balance=self.amount-withdrawal
        return f"Your new balance is {balance}"