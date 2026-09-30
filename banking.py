import random
from datetime import datetime

# ==========================================
# BANKING SYSTEM MINI PROJECT
# ==========================================

# Dictionary to store all accounts
accounts = {}


# ==========================================
# 1. GENERATE UNIQUE ACCOUNT NUMBER
# ==========================================

def generate_account_number():
    while True:
        account_number = str(random.randint(10000000, 99999999))

        if account_number not in accounts:
            return account_number


# ==========================================
# 2. GET VALID NAME
# ==========================================

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()

        if name == "":
            print("❌ Name cannot be empty.")
        elif not all(char.isalpha() or char.isspace() for char in name):
            print("❌ Invalid name. Please enter letters only.")
        else:
            return name.title()


# ==========================================
# 3. GET VALID PHONE NUMBER
# ==========================================

def get_valid_phone():
    while True:
        phone = input("Enter your phone number: ").strip()

        if not phone.isdigit():
            print("❌ Phone number must contain digits only.")

        elif len(phone) != 10:
            print("❌ Phone number must contain exactly 10 digits.")

        else:
            return phone


# ==========================================
# 4. GET VALID PIN
# ==========================================

def get_valid_pin():
    while True:
        pin = input("Create a 4-digit PIN: ").strip()

        if not pin.isdigit():
            print("❌ PIN must contain numbers only.")

        elif len(pin) != 4:
            print("❌ PIN must contain exactly 4 digits.")

        else:
            return pin


# ==========================================
# 5. GET VALID AMOUNT
# ==========================================

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("❌ Invalid amount. Please enter numbers only.")


# ==========================================
# 6. CREATE ACCOUNT
# ==========================================

def create_account():

    print("\n========================================")
    print("          CREATE NEW ACCOUNT")
    print("========================================")

    name = get_valid_name()
    phone = get_valid_phone()
    pin = get_valid_pin()

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("\n✅ Account created successfully!")
    print("----------------------------------------")
    print("Account Holder :", name)
    print("Phone Number   :", phone)
    print("Account Number :", account_number)
    print("Initial Balance: ₹0.00")
    print("----------------------------------------")
    print("⚠️ Please remember your account number.")
    print()


# ==========================================
# 7. LOGIN
# ==========================================

def login():

    print("\n========================================")
    print("              LOGIN")
    print("========================================")

    account_number = input("Enter account number: ").strip()

    if account_number not in accounts:
        print("❌ Account not found.")
        return None

    pin = input("Enter PIN: ").strip()

    if accounts[account_number]["pin"] != pin:
        print("❌ Incorrect PIN.")
        return None

    print("\n✅ Login successful!")
    print("Welcome,", accounts[account_number]["name"])

    return account_number


# ==========================================
# 8. CHECK BALANCE
# ==========================================

def check_balance(account_number):

    balance = accounts[account_number]["balance"]

    print("\n========================================")
    print("           ACCOUNT BALANCE")
    print("========================================")
    print(f"Available Balance: ₹{balance:.2f}")


# ==========================================
# 9. DEPOSIT MONEY
# ==========================================

def deposit(account_number):

    print("\n========================================")
    print("             DEPOSIT MONEY")
    print("========================================")

    amount = get_valid_amount()

    accounts[account_number]["balance"] += amount

    transaction = (
        f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - "
        f"Deposited ₹{amount:.2f}"
    )

    accounts[account_number]["transactions"].append(transaction)

    print(f"\n✅ ₹{amount:.2f} deposited successfully.")
    print(f"New Balance: ₹{accounts[account_number]['balance']:.2f}")


# ==========================================
# 10. WITHDRAW MONEY
# ==========================================

def withdraw(account_number):

    print("\n========================================")
    print("            WITHDRAW MONEY")
    print("========================================")

    amount = get_valid_amount()

    balance = accounts[account_number]["balance"]

    if amount > balance:
        print("❌ Insufficient balance.")
        print(f"Available Balance: ₹{balance:.2f}")
        return

    accounts[account_number]["balance"] -= amount

    transaction = (
        f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - "
        f"Withdrawn ₹{amount:.2f}"
    )

    accounts[account_number]["transactions"].append(transaction)

    print(f"\n✅ ₹{amount:.2f} withdrawn successfully.")
    print(f"Remaining Balance: ₹{accounts[account_number]['balance']:.2f}")


# ==========================================
# 11. TRANSFER MONEY
# ==========================================

def transfer_money(account_number):

    print("\n========================================")
    print("            TRANSFER MONEY")
    print("========================================")

    receiver = input("Enter receiver account number: ").strip()

    if receiver not in accounts:
        print("❌ Receiver account does not exist.")
        return

    if receiver == account_number:
        print("❌ You cannot transfer money to your own account.")
        return

    amount = get_valid_amount()

    sender_balance = accounts[account_number]["balance"]

    if amount > sender_balance:
        print("❌ Insufficient balance.")
        print(f"Available Balance: ₹{sender_balance:.2f}")
        return

    # Deduct money from sender
    accounts[account_number]["balance"] -= amount

    # Add money to receiver
    accounts[receiver]["balance"] += amount

    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    sender_transaction = (
        f"{current_time} - "
        f"Transferred ₹{amount:.2f} to Account {receiver}"
    )

    receiver_transaction = (
        f"{current_time} - "
        f"Received ₹{amount:.2f} from Account {account_number}"
    )

    accounts[account_number]["transactions"].append(
        sender_transaction
    )

    accounts[receiver]["transactions"].append(
        receiver_transaction
    )

    print("\n✅ Money transferred successfully.")
    print(f"Amount Transferred: ₹{amount:.2f}")
    print(f"Receiver Account: {receiver}")
    print(
        f"Your New Balance: "
        f"₹{accounts[account_number]['balance']:.2f}"
    )


# ==========================================
# 12. TRANSACTION HISTORY
# ==========================================

def transaction_history(account_number):

    print("\n========================================")
    print("          TRANSACTION HISTORY")
    print("========================================")

    transactions = accounts[account_number]["transactions"]

    if len(transactions) == 0:
        print("No transactions found.")
        return

    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}. {transaction}")


# ==========================================
# 13. CHANGE PIN
# ==========================================

def change_pin(account_number):

    print("\n========================================")
    print("              CHANGE PIN")
    print("========================================")

    old_pin = input("Enter current PIN: ").strip()

    if old_pin != accounts[account_number]["pin"]:
        print("❌ Incorrect current PIN.")
        return

    new_pin = get_valid_pin()

    confirm_pin = input("Confirm new PIN: ").strip()

    if new_pin != confirm_pin:
        print("❌ PINs do not match.")
        return

    if new_pin == old_pin:
        print("❌ New PIN cannot be the same as the old PIN.")
        return

    accounts[account_number]["pin"] = new_pin

    transaction = (
        f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} - "
        f"PIN changed successfully"
    )

    accounts[account_number]["transactions"].append(transaction)

    print("✅ PIN changed successfully.")


# ==========================================
# 14. ACCOUNT MENU
# ==========================================

def account_menu(account_number):

    while True:

        print("\n========================================")
        print("             ACCOUNT MENU")
        print("========================================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("========================================")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit(account_number)

        elif choice == "3":
            withdraw(account_number)

        elif choice == "4":
            transfer_money(account_number)

        elif choice == "5":
            transaction_history(account_number)

        elif choice == "6":
            change_pin(account_number)

        elif choice == "7":
            print("\n✅ Logged out successfully.")
            print("Returning to main menu...")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 7.")


# ==========================================
# 15. MAIN MENU
# ==========================================

def main():

    while True:

        print("\n")
        print("========================================")
        print("        🏦 YOUR BANKING SYSTEM")
        print("========================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("========================================")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            create_account()

        elif choice == "2":

            account_number = login()

            if account_number is not None:
                account_menu(account_number)

        elif choice == "3":

            print("\n========================================")
            print("Thank you for using Your Banking System!")
            print("Have a great day! 👋")
            print("========================================")
            break

        else:

            print("❌ Invalid choice. Please enter 1, 2, or 3.")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()