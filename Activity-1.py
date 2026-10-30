
balance = 5000
transactions = []

while True:
    print("\n----- ATM MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = int(input("Enter deposit amount: "))

        if amount >= 100:
            balance = balance + amount
            transactions.append("Deposited: Rs." + str(amount))
            print("Amount deposited successfully.")
        else:
            print("Minimum deposit amount is Rs.100")

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))

        if amount < 100:
            print("Minimum withdrawal is Rs.100")

        elif amount > balance:
            print("Insufficient balance.")

        else:
            balance = balance - amount
            transactions.append("Withdrawn: Rs." + str(amount))
            print("Please collect your money.")

    elif choice == 3:
        print("\n----- ACCOUNT SUMMARY -----")
        print("Final Balance: Rs.", balance)

        print("\nTransaction History:")
        for item in transactions:
            print(item)

        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice. Try again.")
