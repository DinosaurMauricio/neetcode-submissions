class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    
    total_balance = 0 
    total_accounts = 0
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
# TODO: Print the information using the mentioned format

bob = BankAccount("Bob", 2000)
alice = BankAccount("Alice", 1000)

print(f"Alice's balance: ${alice.balance}")
print(f"Bob's balance: ${bob.balance}")
print(f"Total Accounts: {alice.total_accounts}")
print(f"Total Balance: ${alice.total_balance}")