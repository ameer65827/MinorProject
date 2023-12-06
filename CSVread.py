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
# d = cur.execute(''' CREATE TABLE IF NOT EXISTS ''')


with open('DATA/books1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)


    for row in csv_reader:
        d = cur.execute('INSERT INTO booksTB (Title, Author, Genre) VALUES (? , ?, ?)', (row[0], row[1], row[2]))
        print([a for a in d])

conn.commit()
conn.close()





