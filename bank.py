class Bank:
    bank_name="Equity"
    def __init__(self,account_name,account_number,amount):
        self.account_name=account_name
        self.acount_number=account_number
        self.amount=amount
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
        
        
        
    def bank_details(self):
        return f"Your account name is {self.account_name},{self.acount_number},has a balance of {self.amount}"
    
    
    def account_balance_after_deposit(self,deposit):
        new_balance=deposit+self.amount
        return f"Your new balance is {new_balance}"
    
    
    def account_balance_after_withdrawal(self,withdrawal):
        balance=self.amount-withdrawal
        return f"Your new balance is {balance}"
    
    
    
    def check_balance(self):
        return f"Your account balance is {self.amount}"
    
    
    def deposit(self, amount):
        transaction = {
            "amount": amount,
            "narration": "deposit"
        }
        self.deposits.append(transaction)
        
        
    def withdrawal(self, amount):
        transaction = {
            "amount": amount,
            "narration": "withdrawal"
        }
        self.withdrawals.append(transaction)    
        
        
    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            amount = transaction["amount"]
            narration = transaction["narration"]
            print(f"{narration} - {amount}")
            
            
    def borrow_loan(self, loan_amount):
        if self.loan_balance == 0 and loan_amount > 100 and len(self.deposits) >= 10:
            total_deposits = sum(transaction["amount"] for transaction in self.deposits)
            if loan_amount <= total_deposits / 3:
                self.loan_balance += loan_amount
                print("Loan approved. Your loan balance has been increased.")
            else:
                print("Loan amount exceeds the limit.")
        else:
            print("Unable to borrow loan. Please check the conditions.")
            
    
    def transfer(self, amount, other_account):
        if amount <= self.amount:
            self.withdrawal(amount)
            other_account.deposit(amount)
            print(f"Successfully transferred {amount} to {other_account.account_name}'s account.")
        else:
            print("Insufficient balance to transfer the requested amount.")
        
            
               
    
    
        