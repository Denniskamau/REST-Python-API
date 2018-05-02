import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'dento', 'pass')

insert_quary = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_quary, user)

users = [
    (1, 'dento', 'pass'),
    (1, 'kama', 'pass1')
]

cursor.executemany(insert_quary,users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)
connection.commit()
connection.close()