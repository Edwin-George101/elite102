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
        CREATE TABLE IF NOT EXISTS students
            (id integer primary key, 
            fName text, 
            lName text, 
            email text, 
            phone_number text)
    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO students (fName, lName, email, phone_number) VALUES
        ('Alice', 'Hark', 'alicehark@test.com', '555-555-5555'),
        ('Bob', 'Marley', 'bobby@test.com', '555-555-5553'),
        ('Charlie', 'George', 'charlie@test.com', '123-123-1234')
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_database()

