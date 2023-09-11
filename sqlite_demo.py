import sqlite3
from employee import Employee

# creates file if not there, else it connects
conn = sqlite3.connect('employee.db')

c = conn.cursor()

fname = input("What is your first name? ")
lname = input("What is your last name? ")
salary = input("What is your salary? ")

emp = Employee(fname, lname, salary)

# create table statement
#create_table_query = """
#CREATE TABLE employees(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    fname TEXT,
#    lname TEXT,
#    salary INTEGER
#);"""


# insert statement
insert_table_query = """
INSERT INTO employees(
    fname,
    lname,
    salary
) VALUES (
    :fname,
    :lname,
    :salary
);
"""

select_query = """
    SELECT * FROM employees;
"""

# c.execute(create_table_query)
c.execute(insert_table_query, {
    "fname": emp.fname,
    "lname": emp.lname,
    "salary": emp.salary
})
c.execute(select_query)
employees = c.fetchall()

print(employees)

conn.commit()

conn.close()

