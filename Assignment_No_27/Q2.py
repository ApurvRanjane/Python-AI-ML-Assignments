# 2: Write a Python program to implement a class named BankAccount with the following requirements:

# • The class should contain two instance variables:
#     - Name (Account holder name)
#     - Amount (Account balance)
# • The class should contain one class variable:
#     - ROI (Rate of Interest), initialized to 10.5
# • Define a constructor (__init__) that accepts Name and initial Amount.
# • Implement the following instance methods:
#     - Display() -> displays account holder name and current balance.
#     - Deposit() -> accepts an amount from the user and adds it to the balance.
#     - Withdraw() -> accepts an amount from the user and subtracts it from the balance
#                     (show withdrawal is not possible if sufficient balance is not available).
#     - CalculateInterest() -> calculates and returns interest using the formula:
#           Interest = (Amount * ROI) / 100
# • Create multiple objects and demonstrate all methods.

class BankAccount:
    ROI = 10.5
    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Display(self):
        print(f"{self.Name} has Balance : {self.Amount}")
    
    def Deposit(self,Amnt):
        self.Amount = Amnt+self.Amount
        print(f"The new amount after deposite is :{self.Amount}")
    
    def Withdraw(self,Amnt):
        self.Amount = self.Amount-Amnt
        print(f"The new amount after withdraw is :{self.Amount-Amnt}")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI)/100
        return Interest


obj1 = BankAccount("Apurv Ranjane",50000)
obj1.Display()
obj1.Deposit(5000)
obj1.Withdraw(5000)
ret = obj1.CalculateInterest()
print(f"The rate of Intereset is : {ret}")

obj2 = BankAccount("Avdhut Ranjane",90000)
obj2.Display()
obj2.Deposit(5000)
obj2.Withdraw(5000)
ret = obj2.CalculateInterest()
print(f"The rate of Intereset is : {ret}")


