import sqlite3
import csv

conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()

def all_books():
    cur.execute('SELECT ID, Title, Genre FROM booksTB')
    return [a for a in cur.fetchall()]


def check_availabiliy(book):
    cur.execute('SELECT ID, Title, Genre FROM booksTB where Title LIKE ?', ('%' + book + '%',))
    return [results for results in cur.fetchall()]
print('hai')






    

