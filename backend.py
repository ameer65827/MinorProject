import sqlite3
import csv

conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()

def all_books():
    cur.execute('SELECT id, title, genre FROM booksTB')
    return [a for a in cur.fetchall()]


def check_availabiliy(book):
    cur.execute('SELECT id, title, genre FROM booksTB where Title LIKE ?', ('%' + book + '%',))
    return [results for results in cur.fetchall()]

def borrow_book(book):
    cur.execute("SELECT stock FROM booksTB WHERE title = (?)", book)
    out = cur.fetchone
    id, stock = (out[0], out[4])

    if not stock:
        return "Out Of Stock"
    #in stock
    else:
        #decrease stock
        cur.execute("UPDATE booksTB SET stock = stock - 1 WHERE id = (?)", id)
        return id







    

