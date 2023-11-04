import mysql.connector

# Function to establish a database connection
def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root',
        database='avi'
    )

# Function to insert a new record
def insert_record(cursor, conn):
    cursor.execute("INSERT INTO Employees (first_name, last_name, salary) VALUES (%s, %s, %s)",
                   ('John', 'Doe', 60000))
    conn.commit()
    print("Record inserted successfully!")

# Function to select and display records
def select_records(cursor):
    cursor.execute("SELECT first_name, last_name, salary FROM Employees")
    for row in cursor.fetchall():
        print(row)

# Function to update a record
def update_record(cursor, conn):
    cursor.execute("UPDATE Employees SET salary = %s WHERE first_name = %s", (65000, 'John'))
    conn.commit()
    print("Record updated successfully!")

# Function to delete a record
def delete_record(cursor, conn):
    cursor.execute("DELETE FROM Employees WHERE first_name = %s", ('John',))
    conn.commit()
    print("Record deleted successfully!")

def main():
    conn = connect_to_database()
    cursor = conn.cursor()

    print("Inserting a new record...")
    insert_record(cursor, conn)

    print("\nSelecting records...")
    select_records(cursor)

    print("\nUpdating a record...")
    update_record(cursor, conn)

    print("\nDeleting a record...")
    delete_record(cursor, conn)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
