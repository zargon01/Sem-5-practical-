# pip install mysql-connector-python
import mysql.connector

# Function to establish a database connection
def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root',
        database='avi',
    )

# Function to insert a new record
def insert_record(cursor, conn):
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    salary = float(input("Enter Salary: "))
    cursor.execute("INSERT INTO Employees (first_name, last_name, salary) VALUES (%s, %s, %s)",
                   (first_name, last_name, salary))
    conn.commit()
    print("Record inserted successfully!")

# Function to select and display records
def select_records(cursor):
    cursor.execute("SELECT first_name, last_name, salary FROM Employees")
    for row in cursor.fetchall():
        print(row)

# Function to update a record
def update_record(cursor, conn):
    first_name = input("Enter First Name of the employee to update: ")
    new_salary = float(input("Enter the new salary: "))
    cursor.execute("UPDATE Employees SET salary = %s WHERE first_name = %s", (new_salary, first_name))
    conn.commit()
    print("Record updated successfully!")

# Function to delete a record
def delete_record(cursor, conn):
    first_name = input("Enter First Name of the employee to delete: ")
    cursor.execute("DELETE FROM Employees WHERE first_name = %s", (first_name,))
    conn.commit()
    print("Record deleted successfully!")

def main():
    conn = connect_to_database()
    cursor = conn.cursor()

    while True:
        print("\nMenu:")
        print("1. Insert Record")
        print("2. Select Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            insert_record(cursor, conn)
        elif choice == '2':
            select_records(cursor)
        elif choice == '3':
            update_record(cursor, conn)
        elif choice == '4':
            delete_record(cursor, conn)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
