import sqlite3
from initialize_db import initialize_database

DB_NAME = 'bank.db'

def create_account(name, email):
    with sqlite3.connect(DB_NAME) as conn:
     cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    print("Account created successfully.")

def delete_account(account_id):
    with sqlite3.connect(DB_NAME) as conn:
     cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE account_id = ?", (account_id,))
    conn.commit()
    print("Account deleted.")

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
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_id = ?", (amount, account_id))
    conn.commit()
    print(f"Deposited ${amount:.2f}.")

def make_withdrawal(account_id, amount):
    with sqlite3.connect(DB_NAME) as conn:
     cursor = conn.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_id = ?", (account_id,))
    balance = cursor.fetchone()
    if balance and balance[0] >= amount:
        cursor.execute("UPDATE accounts SET balance = balance - ? WHERE account_id = ?", (amount, account_id))
        conn.commit()
        print(f"Withdrew ${amount:.2f}.")
    else:
        print("Insufficient funds or account not found.")

def main():
    initialize_database()
    while True:
        print("\nWelcome to the Bank System")
        print("1. Create an account")
        print("2. Delete an account")
        print("3. Check balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Exit")

        choice = input("Choose an option: ")

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
            make_deposit(acc_id, amount)
        elif choice == '5':
            acc_id = int(input("Enter account ID: "))
            amount = float(input("Enter amount to withdraw: "))
            make_withdrawal(acc_id, amount)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
   main()