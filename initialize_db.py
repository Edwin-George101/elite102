import sqlite3
import os

DB_NAME = 'bank.db'

def initialize_database():
    # Delete the database file if it exists
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Existing {DB_NAME} deleted.")
    
    # Create a new database connection
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create accounts table
    cursor.execute('''
    CREATE TABLE accounts (
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        balance REAL DEFAULT 0.0
    )
    ''')
    
    # Create transactions table (optional, for future functionality)
    cursor.execute('''
    CREATE TABLE transactions (
        transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER,
        transaction_type TEXT NOT NULL,
        amount REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES accounts (account_id)
    )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print(f"Database {DB_NAME} initialized successfully.")

if __name__ == "__main__":
    initialize_database()