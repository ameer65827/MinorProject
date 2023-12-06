import csv
import sqlite3
import random
import os

if os.path.exists('DATA/booksDB.db'):
    os.remove('DATA/booksDB.db')

conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS booksTB (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                genre TEXT,
                publisher
                Stocks INTEGER
                )'''
            )
cur.execute(''' CREATE TABLE IF NOT EXISTS Customer (
            book_id INTEGER,
            customer_name TEXT,
            FOREGN KEY(book_id) REFERENCES booksTB
)''')


with open('DATA/books1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)


    for row in csv_reader:

        cur.execute('INSERT INTO booksTB (title, author, genre, stocks) VALUES (? , ?, ?, ?)', (row[0], row[1], row[2]), random.randint(0,10))
        bkid = cur.lastrowid()
        print(bkid)

        

conn.commit()
conn.close()





