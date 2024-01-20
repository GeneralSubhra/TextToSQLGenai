import sqlite3

connection = sqlite3.connect('student.db')
cursor = connection.cursor()
table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25))
"""
cursor.execute(table_info)
cursor.execute('''Insert into STUDENT VALUES ('subhra','CSE','4C')''')
cursor.execute('''Insert into STUDENT VALUES ('pranit','CSE','4B')''')
cursor.execute('''Insert into STUDENT VALUES ('Rishu','CSBS','1C')''')
cursor.execute('''Insert into STUDENT VALUES ('Swarup','CSE','2C')''')
cursor.execute('''Insert into STUDENT VALUES ('Gourav','CSE','4C')''')

print("The inserted table is:\n")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()
