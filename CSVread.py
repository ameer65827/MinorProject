import csv
import sqlite3

conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS booksTB (
                  ID INTEGER PRIMARY KEY,
                  Title TEXT,
                  Author TEXT,
                  Genre TEXT
                )'''
            )


with open('DATA/books1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)


    for row in csv_reader:
        print(row)
        cur.execute('INSERT INTO booksTB (Title, Author, Genre) VALUES (? , ?, ?)', (row[0], row[1], row[2]))
    

conn.commit()
conn.close()





