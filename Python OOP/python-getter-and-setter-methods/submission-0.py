class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        if new_balance < 0:
            print("Cannot set negative balance!")
        else:
            self.__balance = new_balance
    
    # TODO: Add getter method for balance

    # TODO: Add setter method for balance




# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
