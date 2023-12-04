import csv
import sqlite3

conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS booksTB (
                  ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  Title TEXT,
                  Author TEXT
                )'''
            )


with open('DATA/books.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)


    for row in csv_reader:
        cur.execute('INSERT INTO booksTB (Title, Author) VALUES (? , ?)', (row[0], row[1]))
    

conn.commit()
conn.close()





