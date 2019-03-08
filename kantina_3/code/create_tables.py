import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users" \
               "(id INTEGER PRIMARY KEY, username text, password text, email text)"
# for auto increment use INTEGER, otherwise int is enough
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS meals" \
               "(name text, price text)"
# for auto increment use INTEGER, otherwise int is enough
cursor.execute(create_table)


connection.commit()
connection.close()

