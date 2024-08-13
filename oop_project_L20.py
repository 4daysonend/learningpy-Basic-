from oop_Bank_Accounts_L20 import *

Myles = BankAccount(10000, "Myles")
Camry = BankAccount(20000, "Camry")

Myles.getBalance()
Camry.getBalance()

Camry.deposit(500)

Myles.withdraw(20000)
Myles.withdraw(10)

Myles.transfer(10000, Camry)
Myles.transfer(1000, Camry)

Carolyn = InterestRewardsAcct(1000, "Carolyn")

Carolyn.getBalance()
Carolyn.deposit(100)

Carolyn.transfer(100, Myles)

Malek = SavingsAcct(1000, "Malek")

Malek.getBalance()

Malek.deposit(100)

Malek.transfer(10000, Camry)
Malek.transfer(1000, Camry)


print(f"\n")
