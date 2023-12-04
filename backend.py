import sqlite3
conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()

def all_books():
    cur.execute('SELECT Title FROM booksTB LIMIT 50 offset 5')
    return [a[0] for a in cur.fetchall()]


def check_availabiliy(book):
    cur.execute('SELECT Title FROM booksTB where Title LIKE ?', ('%' + book + '%',))
    return [results[0] for results in cur.fetchall()]

# print(all_books())




    

