

#https://youtu.be/mn7mYdKln5Q?list=PL6lxxT7IdTxEloArZ2ZSRWCy5jQpD5VtT

class Account:
    def __init__(self, balance, name):#double underscore.
        self.balance=balance
        self.name=name
        
    def credit(self, deposit):
        self.balance=self.balance + deposit
        
    def debit(self, withdrawl):
        self.balance=self.balance - withdrawl
        
    def get_balance(self):# NOT NEEDED
        return self.balance
    
    def get_name(self):# NOT NEEDED
        return self.name
    
    def set_name(self, name):# NOT NEEDED
        self.name=name
        
customer=Account(0,"Rita Jones") 
   
'''print(customer.get_name(), "has a balance of", customer.get_balance())
customer.credit(100) 
print(customer.get_name(), "has a balance of", customer.get_balance())
customer.debit(45)
print(customer.get_name(), "has a balance of", customer.get_balance())
customer.set_name("Rita Hartley")
print(customer.get_name(), "has a balance of", customer.get_balance())'''

print(customer.name, "has a balance of", customer.balance)
customer.credit(100) 
print(customer.name, "has a balance of", customer.balance)
customer.debit(45)
print(customer.name, "has a balance of", customer.balance)
customer.name=("Rita Smith")#changes name.
print(customer.name, "has a balance of", customer.balance)
        
        