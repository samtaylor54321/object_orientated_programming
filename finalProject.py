################ FINAL PROJECT - SIMULATING A BANKING SYSTEM ##################

# Prompt which lets the user access a current account or set up a new one.

# if it's a new account the user needs to be able to set up the account,
# add their name and initial deposit and be given a random account number

# if it's an existing account it needs to take their name and account
# number and give them options to withdraw, deposit or display their balance

import random

class newAccount:
    def __init__(self, name, initialDeposit, accountNumber):
        self.name = name
        self.initialDeposit = initialDeposit
        self.accountNumber = accountNumber

    def DisplayAccountDetails(self):
        print("Account Name:", self.name)
        print("Account Number:", self.accountNumber)
        print("Your current balance is £", self.initialDeposit)

class existingAccount:
    def __init__(self):
        self.name = 'Sam'
        self.accountNumber = 12345
        self.balance = 1000

    def makeWithdrawal(self, amount):
        if self.balance - amount < 0:
            print("You do not have the funds to make this withdrawal")
        else:
             self.balance = self.balance - amount

    def makeDeposit(self, amount):
        self.balance = self.balance + amount

    def DisplayAccountDetails(self):
        print("Account Name:", self.name)
        print("Account Number:", self.accountNumber)
        print("Your current balance is £", self.balance)

while True:
    print("Welcome to the bank - how may we help you today?")
    print("Press 1 to set up a new account")
    print("Press 2 to view an existing account")
    print("Press 3 to exit")

    userChoice = int(input())
    if userChoice == 1:
        print("Please enter your name")
        name = input()
        print("Please enter your initial deposit")
        initialDeposit = input()
        accountNumber = ''.join(random.sample('0123456789', 5))
        account = newAccount(name, initialDeposit, accountNumber)
        print("Thank you for setting up your new account, please see your details below")
        account.DisplayAccountDetails()
    elif userChoice == 2:
        print("Please confirm your name")
        name = input()
        print("Please confirm your account number")
        accountNumber = input()
        account = existingAccount()
        while True:
            print("Thank you, what service would you like?")
            print("Press 1 to view your balance")
            print("Press 2 to make a deposit")
            print("Press 3 to make a withdrawal")
            print("Press 4 to exit")
            secondChoice = int(input())
            if secondChoice == 1:
                account.DisplayAccountDetails()
            elif secondChoice == 2:
                print("How much would you like to deposit?")
                deposit = int(input())
                account.makeDeposit(deposit)
            elif secondChoice == 3:
                print("How much would you like to withdraw?")
                withdrawal = int(input())
                account.makeWithdrawal(withdrawal)
            elif secondChoice == 4:
                break
    elif userChoice == 3:
        quit()
