# Minimum balance constant
MIN_BALANCE = 500
SAVINGS_INTEREST_RATE = 7.25

# List to store all accounts
accounts = []

# Function to find account
def find_account(acc_no):# Minimum balance constant
MIN_BALANCE = 500
SAVINGS_INTEREST_RATE = 7.25

# List to store all accounts
accounts = []


# Function to find account
def find_account(acc_no):
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            return True, acc
    return False, None


# Function to create account
def create_account():
    acc_no = input("Enter Account Number: ")

    found, _ = find_account(acc_no)

    if found:
        print("Account already exists!")
        return

    name = input("Enter Name: ")

    print("Account Type:")
    print("1. Savings Account")
    print("2. Current Account")

    acc_type_choice = input("Choose account type: ")

    if acc_type_choice == '1':
        acc_type = "Savings"
    elif acc_type_choice == '2':
        acc_type = "Current"
    else:
        print("Invalid account type!")
        return

    balance = float(input(f"Enter Initial Deposit (Minimum ₹{MIN_BALANCE}): "))

    if balance < MIN_BALANCE:
        print(f"Minimum balance of ₹{MIN_BALANCE} is required!")
        return

    account = {
        "acc_no": acc_no,
        "name": name,
        "balance": balance,
        "type": acc_type
    }

    accounts.append(account)

    print(f"{acc_type} Account Created Successfully!")


# Deposit function
def deposit():
    acc_no = input("Enter Account Number: ")

    found, acc = find_account(acc_no)

    if found:
        amount = float(input("Enter Amount to Deposit: "))

        if amount <= 0:
            print("Deposit amount must be greater than ₹0.")
            return

        acc["balance"] += amount

        print("Deposit Successful!")
        print(f"Updated Balance: ₹{acc['balance']:.2f}")

    else:
        print("Account Not Found!")


# Withdraw function
def withdraw():
    acc_no = input("Enter Account Number: ")

    found, acc = find_account(acc_no)

    if found:
        amount = float(input("Enter Amount to Withdraw: "))

        if amount <= 0:
            print("Withdrawal amount must be greater than ₹0.")
            return

        # Calculate maximum amount that can be withdrawn
        max_withdraw = acc["balance"] - MIN_BALANCE

        # Check withdrawal limit
        if amount > max_withdraw:

            print(f"Cannot withdraw ₹{amount:.2f}!")
            print(f"You can only withdraw ₹{max_withdraw:.2f}.")
            print(f"Minimum balance of ₹{MIN_BALANCE} must be maintained.")

        else:
            acc["balance"] -= amount

            print("Withdrawal Successful!")
            print(f"Remaining Balance: ₹{acc['balance']:.2f}")

    else:
        print("Account Not Found!")


# Check balance
def check_balance():
    acc_no = input("Enter Account Number: ")

    found, acc = find_account(acc_no)

    if found:
        print("Account Holder:", acc["name"])
        print("Account Type:", acc["type"])
        print(f"Balance: ₹{acc['balance']:.2f}")

    else:
        print("Account Not Found!")


# Display all accounts
def display_all():
    if not accounts:
        print("No accounts available.")
        return

    print("\nAll Accounts:")

    for acc in accounts:
        print(
            f"Acc No: {acc['acc_no']}, "
            f"Name: {acc['name']}, "
            f"Type: {acc['type']}, "
            f"Balance: ₹{acc['balance']:.2f}"
        )


# Calculate interest
def calculate_interest():
    acc_no = input("Enter Account Number: ")

    found, acc = find_account(acc_no)

    if found:

        if acc["type"] != "Savings":
            print("Interest is only available for Savings Accounts!")
            return

        years = float(input("Enter number of years: "))

        if years <= 0:
            print("Number of years must be greater than 0.")
            return

        interest = (
            acc["balance"]
            * SAVINGS_INTEREST_RATE
            * years
        ) / 100

        print(f"Interest Rate: {SAVINGS_INTEREST_RATE}%")
        print(f"Interest for {years} years: ₹{interest:.2f}")

    else:
        print("Account Not Found!")


# Main program
while True:

    print("\n---- Bank Management System ----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Calculate Interest (Savings)")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()

    elif choice == '2':
        deposit()

    elif choice == '3':
        withdraw()

    elif choice == '4':
        check_balance()

    elif choice == '5':
        display_all()

    elif choice == '6':
        calculate_interest()

    elif choice == '7':
        print("Thank you!")
        break

    else:
        print("Invalid Choice!")
        
    for acc in accounts:
        if acc["acc_no"] == acc_no:
            return True, acc
    return False, None


# Function to create account
def create_account():
    acc_no = input("Enter Account Number: ")

    found, _ = find_account(acc_no)
    if found:
        print("Account already exists!")
        return

    name = input("Enter Name: ")
    
    print("Account Type:")
    print("1. Savings Account")
    print("2. Current Account")
    acc_type_choice = input("Choose account type: ")

    if acc_type_choice == '1':
        acc_type = "Savings"
    elif acc_type_choice == '2':
        acc_type = "Current"
    else:
        print("Invalid account type!")
        return

    balance = float(input(f"Enter Initial Deposit (Minimum ₹{MIN_BALANCE}): "))

    if balance < MIN_BALANCE:
        print(f"Minimum balance of ₹{MIN_BALANCE} is required!")
        return

    account = {
        "acc_no": acc_no,
        "name": name,
        "balance": balance,
        "type": acc_type
    }

    accounts.append(account)
    print(f"{acc_type} Account Created Successfully!")


# Deposit function
def deposit():
    acc_no = input("Enter Account Number: ")
    found, acc = find_account(acc_no)

    if found:
        amount = float(input("Enter Amount to Deposit: "))
        acc["balance"] += amount
        print("Deposit Successful!")
    else:
        print("Account Not Found!")


# Withdraw function
def withdraw():
    acc_no = input("Enter Account Number: ")
    found, acc = find_account(acc_no)

    if found:
        amount = float(input("Enter Amount to Withdraw: "))
        
        if acc["balance"] - amount < MIN_BALANCE:
            print(f"Cannot withdraw! Minimum balance of ₹{MIN_BALANCE} must be maintained.")
        else:
            acc["balance"] -= amount
            print("Withdrawal Successful!")
    else:
        print("Account Not Found!")


# Interest calculator (Savings only)
def calculate_interest():
    acc_no = input("Enter Account Number: ")
    found, acc = find_account(acc_no)

    if found:
        if acc["type"] != "Savings":
            print("Interest is only available for Savings Accounts!")
            return
        
        years = float(input("Enter number of years: "))
        interest = (acc["balance"] * SAVINGS_INTEREST_RATE * years) / 100
        print(f"Interest for {years} years: ₹{interest:.2f}")
    else:
        print("Account Not Found!")


# Check balance
def check_balance():
    acc_no = input("Enter Account Number: ")
    found, acc = find_account(acc_no)

    if found:
        print("Account Holder:", acc["name"])
        print("Account Type:", acc["type"])
        print("Balance: ₹", acc["balance"])
    else:
        print("Account Not Found!")


# Display all accounts
def display_all():
    if not accounts:
        print("No accounts available.")
        return

    print("\nAll Accounts:")
    for acc in accounts:
        print(f"Acc No: {acc['acc_no']}, Name: {acc['name']}, Type: {acc['type']}, Balance: ₹{acc['balance']}")


# Main program
while True:
    print("\n---- Bank Management System ----")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display All Accounts")
    print("6. Calculate Interest (Savings)")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        display_all()
    elif choice == '6':
        calculate_interest()
    elif choice == '7':
        print("Thank you!")
        break
    else:
        print("Invalid Choice!")
