class BankAccount:
    #We define the atributes
    def __init__ (self,account_number,balance=0):
        self.account_number = account_number
        self.balance = balance
    #Adds the money the user says to the balance
    def deposit(self):
        self.balance += (float(input("How much money do you want to deposit")))
    #Removes the inputted money of the account
    def withdraw(self):
        self.balance -= (float(input("How much money do you want to retire")))
    #Prints the balance
    def get_balance(self):
        print("Your actual balance is",self.balance)
    #Prints all the data of the account
    def __str__(self):
        print("Your account number is",self.account_number,"and you actual balance is" , self.balance)
    def welcome(self):
        print("Hi account number",self.account_number)
class savings_account(BankAccount):
    def interest_rate(self):
        self.balance += self.balance*0.05
        print(self.balance)
account1= BankAccount("1")
account2= savings_account("1")


