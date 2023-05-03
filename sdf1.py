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
employee_id = input("Enter the employee id: ")
name = input("Enter the name of employee: ")
leaves = input("Enter the number of leaves: ")
absent = input("Enter the number of absent days: ")

# Add new employee name 
c.execute(f"INSERT INTO employee (name, leaves, absent) VALUES ('{name}', {leaves}, {absent})")

# Update the employee's leaves and absent days
c.execute(f"UPDATE employee SET leaves = {leaves}, absent = {absent} WHERE id = {employee_id}")

# Get all employees
c.execute("SELECT * FROM employee")
print(c.fetchall())

# Commit changes and close the connection
conn.commit()
conn.close()
