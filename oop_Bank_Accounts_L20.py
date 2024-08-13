# add an expression to continue the logic for widthdrawing from the Bank Account it has to first check if the Account has the funds to pull.
class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

# add a method to the class
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account'{self.name}' only has a balance of ${self.balance:.2f}"
            )

    #  we are going to first add a try bc we want to catch an error if we actually raise exception
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer..🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Complete! ✅\n\n**********')
        except BalanceException as error:
            print(f'\nTransfer interrupted.❌ {error}')

# this class is going to have inheritance from the bank account class


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite Complete.")
        self.getBalance()

# this class is going to inherit from the InterestRewardsAcct


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):  # <--- override the withdraw method
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Completed.")
            self.getBalance()
        except BalanceException as error:  # <--- add the exception if there is not enough funds
            print(f'\n Withdraw interrupted: {error}')
