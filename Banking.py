# Instance variable : Name,Amount,Address,AccountNO

class Bank_Account:

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(Self):
        print("Enter your name : ")
        Self.Name = input()

        print("Enter your intial amount : ")
        Self.Amount = int(input())

        print("Enter your Address : ")
        Self.Address = input()

        print("Enter your Account Number : ")
        Self.AccountNo = int(input())


    def DisplayAccountInfo(self):
        print("------Your Account information is as Below -------")
        print("Name of Account Holder :",self.Name)
        print(" Account Number :",self.AccountNo)
        print("Address of Account Holder :",self.Address)
        print("Current Amount in account :",self.Amount)

def main():
    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the First Account")
    User1.CreateAccount()

    print("Creating the Second Account")
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

if __name__ =="__main__":
    main()