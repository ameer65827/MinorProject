import csv
import sqlite3
import random
import os

# !!!! CAUTION !!!!
# !!Execution this code again will delele the old TABLES
if os.path.exists('DATA/booksDB.db'):
    os.remove('DATA/booksDB.db')

conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS booksTB (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                publisher TEXT,
                Stock INTEGER
                )'''
            )

cur.execute(''' CREATE TABLE IF NOT EXISTS customer (
            book_id INTEGER,
            customer_name TEXT,
            FOREIGN KEY(book_id) REFERENCES booksTB(id)
)''')


with open('DATA/books1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)


    for row in csv_reader:

        cur.execute('INSERT INTO booksTB (title, author, genre, publisher, stock) VALUES (? , ?, ?, ? ,?)', (row[0], row[1], row[2], row[4], random.randint(0,10)))


        

conn.commit()
conn.close()





