import sqlite3
import csv

conn = sqlite3.connect('DATA/booksDB.db')
cur = conn.cursor()

def all_books():
    cur.execute('SELECT id, title, genre FROM booksTB ORDER BY title')
    return [a for a in cur.fetchall()]


def check_availabiliy(book):
    cur.execute('SELECT id, title, genre FROM booksTB where Title LIKE ? ORDER BY title', ('%' + book + '%',))
    return [results for results in cur.fetchall()]

# def borrow_book(book, cust_name):
#     cur.execute("SELECT stock FROM booksTB WHERE title = (?)", book)
#     out = cur.fetchone
#     id, stock = (out[0], out[4])

#     #decrease stock and add customer data
#     cur.execute("UPDATE booksTB SET stock = stock - 1 WHERE id = (?)", id)
#     cur.execute('INSERT INTO customer VALUES (?, ?)', (id, cust_name))
#     return id

def get_book_info(id):
    cur.execute("SELECT * FROM booksTB where id = (?)", (id,))
    return cur.fetchone()









    

