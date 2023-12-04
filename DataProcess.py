import sqlite3

def check_availabiliy(book):


    conn = sqlite3.connect('DATA/booksDB.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM booksTB where Title = ?', (book,))

    bk = cur.fetchone()
    conn.close()

    if bk:
        print(f"{book} is in Stock")
    else:
        print(f"{book} is Out of Stock")


inp = input("Enter book Title: ")
check_availabiliy(inp)




