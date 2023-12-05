import sqlite3
conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()

def all_books():
    cur.execute('SELECT ID, Title FROM booksTB LIMIT 150 offset 5')
    return [a for a in cur.fetchall()]


def check_availabiliy(book):
    cur.execute('SELECT ID, Title FROM booksTB where Title LIKE ?', ('%' + book + '%',))
    return [results for results in cur.fetchall()]




    

