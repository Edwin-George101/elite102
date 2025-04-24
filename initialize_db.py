import sqlite3

DB_NAME = 'bank.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts
            (account_id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL, 
            email TEXT NOT NULL UNIQUE, 
            balance REAL DEFAULT 0.0)
    ''')

    print("Table created.")
    connection.commit()
    connection.close()