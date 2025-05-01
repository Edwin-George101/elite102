import sqlite3
from initialize_db import initialize_database

DB_NAME = 'bank.db'

def create_account(name, email):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO accounts (name, email) VALUES (?, ?)", (name, email))
        # Get the ID of the newly created account
        account_id = cursor.lastrowid
        conn.commit()
        print(f"Account created successfully. Your account ID is: {account_id}")
        return account_id

def delete_account(account_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,))
        if cursor.rowcount > 0:
            conn.commit()
            print("Account deleted.")
        else:
            print("Account not found.")

def check_balance(account_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        result = cursor.fetchone()
        if result:
            print(f"Current balance: ${result[0]:.2f}")
        else:
            print("Account not found.")

def make_deposit(account_id, amount):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT account_id FROM accounts WHERE account_id = ?", (account_id,))
        if cursor.fetchone():
            cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, account_id))
            conn.commit()
            print(f"Deposited ${amount:.2f}.")
        else:
            print("Account not found.")

def make_withdrawal(account_id, amount):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
        result = cursor.fetchone()
        if result and result[0] >= amount:
            cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_id))
            conn.commit()
            print(f"Withdrew ${amount:.2f}.")
        else:
            if not result:
                print("Account not found.")
            else:
                print("Insufficient funds.")

def list_accounts():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT account_id, name, email, balance FROM accounts")
        accounts = cursor.fetchall()
        if accounts:
            print("\nAccount List:")
            print("ID\tName\t\tEmail\t\t\tBalance")
            print("-" * 70)
            for account in accounts:
                print(f"{account[0]}\t{account[1]}\t\t{account[2]}\t\t${account[3]:.2f}")
        else:
            print("No accounts found.")

def main():
    initialize_database()
    while True:
        print("\nWelcome to the Bank System")
        print("1. Create account")
        print("2. Delete account")
        print("3. Check balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. List all accounts")
        print("7. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == '1':
                name = input("Enter name: ")
                email = input("Enter email: ")
                create_account(name, email)
            elif choice == '2':
                acc_id = int(input("Enter account ID to delete: "))
                delete_account(acc_id)
            elif choice == '3':
                acc_id = int(input("Enter account ID: "))
                check_balance(acc_id)
            elif choice == '4':
                acc_id = int(input("Enter account ID: "))
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    make_deposit(acc_id, amount)
            elif choice == '5':
                acc_id = int(input("Enter account ID: "))
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    make_withdrawal(acc_id, amount)
            elif choice == '6':
                list_accounts()
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter valid numbers for account ID and amounts.")

if __name__ == "__main__":
    main()