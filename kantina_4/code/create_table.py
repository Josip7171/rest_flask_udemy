import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# MUST BE INTEGER
# This is the only place where int vs INTEGER matters—in auto-incrementing columns
create_table = "CREATE TABLE IF NOT EXISTS users (" \
               "id INTEGER PRIMARY KEY," \
               "username text," \
               "email text," \
               "password text" \
               ")"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (" \
               "id INTEGER PRIMARY KEY," \
               "name text," \
               "price real" \
               ")"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS user_info (" \
               "id INTEGER PRIMARY KEY," \
               "first_name text," \
               "last_name text," \
               "full_name text," \
               "adress text," \
               "postal_code int," \
               "phone_number text," \
               "birth_date text," \
               "gener text," \
               "avatar text," \
               "active boolean DEFAULT TRUE," \
               "role text," \
               "created_at DATETIME DEFAULT CURRENT_TIMESTAMP," \
               "updated_at DATETIME DEFAULT CURRENT_TIMESTAMP" \
               ")"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS meals (" \
               "id INTEGER PRIMARY KEY," \
               "name text," \
               "price real," \
               "description text" \
               ")"

connection.commit()
connection.close()
