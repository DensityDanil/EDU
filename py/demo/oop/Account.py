class Account():
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance #note when error then some record will be executed?

    
    def deposit(self,amount):
        
        self.balance+=amount
        print(f'You receive {amount}')

    def withdraw(self,amount):
        if self.balance<0:
            0
        else:
            self.balance-=amount
            print(f'You spent {amount}')

    def show_balance(self):
        print(self.balance)
        

methods = ['deposit','withdraw']
#[method for method in dir(a) if method not star]


data = list(map(tuple,[[100,20],[100,30],[100,40],[100,50]]))


a = Account(name='Oleg',balance=0)

for val in data:
    depo,spent = val
    a.deposit(depo)
    a.withdraw(spent)
    a.show_balance()
    
