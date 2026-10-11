class BankAccount:
    def __init__(self,balance):
        self.__balance=balance #Private __ variable
    def deposit(self,amount):
        self.__balance+=amount
    def check_balance(self):
        return self.__balance
        
p1= BankAccount(6000)
p1.deposit(10000)
print(p1.check_balance())
