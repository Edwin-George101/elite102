import sqlite3


def main():
    connection = sqlite3.connect('bank.db')
    cursor = connection.cursor()

    # Get all rows from the students table
    print("Fetching all rows from the students table...")
    results = cursor.execute('''
        SELECT * FROM students
    ''')

    print("Results:")
    for row in results:
        print(row)

    # Get all students with a GPA greater than 3.5
    print("Fetching students where last name is Kirk...")
    results = cursor.execute('''
        SELECT * FROM students WHERE lName = 'George'
    ''')
    print("Results:")
    for row in results:
        print(row)

    connection.close()


if __name__ == "__main__":
    main()
