balance=1000
while True:
    print("\nATM Menu")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")

    choice=input("Enter You choice (1-4):")
    if choice=="1":
        def credit():
            global balance
            amount=float(input("Enter amount to be credited:"))
            if amount<=0:
                print("Please enter a positive amount")
            else:
                balance+=amount
                print(f"${amount} credited to your account.")
        credit()
    elif choice=="2":
        def debit():
            global balance
            amount=float(input("Enter amount to be debited:"))
            if amount<=0:
                print("Please enter a positive amount")
            else:
                balance-=amount
                print(f"${amount} debited from your account.")
        debit()
    elif choice=="3":
        def show_balance():
            global balance
            print(f"Your current balance is: ${balance}")
        show_balance()
    elif choice=="4":
        print("Thank you for using the ATM . Goodbye!")
        break
    else:
        print("Invalid choice. Please Try again.")





