class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"we just added {amount} to your account")
        print(f"balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("not enough balance!!!")
        else:
            print("withdraw accepted")
            self.balance -= amount
            print(f"balance: {self.balance}")

    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"


my_Account = Account("Omer", 50000)
print(my_Account)
my_Account.deposit(600)
print(my_Account)
my_Account.withdraw(3000)
my_Account.withdraw(300000)
