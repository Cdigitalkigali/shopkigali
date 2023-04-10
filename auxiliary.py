import sqlite3

def dbinit():
    connection = sqlite3.connect('database.db')
    with open('database-schema.sql') as f:
        connection.executescript(f.read())
    cur = connection.cursor()
    connection.commit()
    connection.close()