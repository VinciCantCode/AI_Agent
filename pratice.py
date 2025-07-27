class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount) -> int:
        self.balance += amount
        return self.balance

    def withdraw(self, amount) -> bool:
        if amount < self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance


if __name__ == "__main__":

    acc = BankAccount(100)
    print(acc.deposit(50))
    print(acc.get_balance())
    print(acc.withdraw(20))
    print(acc.get_balance())

