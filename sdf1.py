import sqlite3

# Connect to the database
conn = sqlite3.connect('employee.db')
c = conn.cursor()

# Create the employee table
c.execute('''CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY,
                name TEXT,
                leaves INTEGER,
                absent INTEGER
            )''')

# Get user input
action = input("Enter 'insert', 'update', or 'remove': ")

if action == 'insert':
    # Get user input
    name = input("Enter the employee name: ")
    leaves = input("Enter the number of leaves: ")
    absent = input("Enter the number of absent days: ")

    # Add a new employee
    c.execute(f"INSERT INTO employee (name, leaves, absent) VALUES ('{name}', {leaves}, {absent})")
elif action == 'update':
    # Get user input
    employee_id = input("Enter the employee id: ")
    leaves = input("Enter the number of leaves: ")
    absent = input("Enter the number of absent days: ")

    # Update the employee's leaves and absent days
    c.execute(f"UPDATE employee SET leaves = {leaves}, absent = {absent} WHERE id = {employee_id}")
elif action == 'remove':
    # Get user input
    employee_id = input("Enter the id of the employee you want to remove: ")

    # Remove the employee
    c.execute(f"DELETE FROM employee WHERE id = {employee_id}")

# Get all employees
c.execute("SELECT * FROM employee")
print(c.fetchall())

# Commit changes and close the connection
conn.commit()
conn.close()
