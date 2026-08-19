class Account:
    def __init__(self,username,password,balance=0):
        self.username=username
        self.password=password
        self.balance=balance
        self.get_mini_statement=[]
    def deposit(self,amount):
        self.balance+=amount
        print(f"\nAmount deposited:{amount}\nTotal Balance:{self.balance}")
        self.get_mini_statement.append(f"Deposited:{amount}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"\nAmount Withdrawn:{amount}\nReamining Balance:{self.balance}")
            self.get_mini_statement.append(f"withdrawn:{amount}")
        else:
            print("Insufficient Balance")
    def get_balance(self):
        return self.balance
    def mini_statement(self):
        print("Mini statement")
        print(f"User name:{self.username}")
        print(f"Current balance:{self.balance}")
        for transaction in self.get_mini_statement:
            print(transaction)
class BankingSystem:
    def __init__(self):
        self.accounts={}
    def create_account(self,username,password):
        if username in self.accounts:
            print("username already exists")
        else:
            self.accounts[username]=Account(username,password)
            print("\nAccount created successfully")
            print("------Welcome to Python Bank-------")
    def login(self,username,password):
        if username in self.accounts:
            account=self.accounts[username]
            if account.password==password:
                print("Login success...")
                return account
            else:
                print("Invalid password")
        else:
            print("Inavlid username")
        return None
bank=BankingSystem()

while True:
    print("\n")
    print("1.create account")
    print("2.Login")
    print("3.Exit")
    choice=input("Enter your choice(1-3):")
    if choice=="1":
        username=input("Enter username:")
        password=input("Enter password:")
        bank.create_account(username,password)
    elif choice=="2":
        username=input("Enter username:")
        password=input("Enter password:")
        account=bank.login(username,password)
        if account is not None:
            while True:
                print("\n --- welcome to Python Bank----")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. check balance")
                print("4. Mini statement")
                print("5. Logout \n")
                choice=input("Enter your choice(1-5):")
                if choice=="1":
                    amount=int(input("Enter amount to deposits: "))
                    account.deposit(amount)
                elif choice=="2":
                    amount=int(input("Enter amount to withdraw:"))
                    account.withdraw(amount)
                elif choice=="3":
                    print(f"Current balnce:{account.get_balance()}")
                elif choice=="4":
                    account.mini_statement()
                elif choice=="5":
                    print("\n----THANK YOU VISIT AGAIN----")
                    break
                else:
                    print("Invalid choice")
    else:
        print("Invalid choice")




