import tkinter as tk
import backend
import time

root = tk.Tk()
root.title("Library Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")


def show_book_details(event = None):
    global text_box
    item = listbox.curselection()

    if not item:
        text_box.delete('1.0', tk.END)
        return None
    items = listbox.get(item[0])
    items_no = int(items.split()[0]) - 2753

    text_box.delete('1.0', tk.END)

    
    book_info = backend.get_book_info(items_no)
    
    details = [
        ("Title:", book_info[1]),
        ("Author:", book_info[2]),
        ("genre:", book_info[3]),
        ("Publisher:", book_info[4]),
        ("Stock:", book_info[5]),
        ("Reference id:", book_info[0] + 2753)
     
       # Add more book details here
    ]

    # Inserting book details into the text box in columns
    for detail, value in details:

        text_box.insert(tk.END, f"{detail:<20}{value}\n\n")


def insert_into_listbox(lst):
    for row in lst:
        nm = row[0]+2753
        sp = 10 - len(str(nm))  # Calculate space for numbers with different number of digits
        bk_padding = '_' * (65 - len(row[1]))
        listbox.insert(tk.END, f"{nm:<{sp}} | {row[1]}{bk_padding} {row[2]}")


def close_system():
    root.destroy()
    backend.conn.close()

data_list = backend.all_books()  #load default data

def perform_search(event=None):
    try:
        search_word = entry.get()  # Get data entry field
        similar  = backend.check_availabiliy(search_word)
                
        if similar:
            result_label.config(text=f"{len(similar)} results found !")

            #showing result
            listbox.delete(0, tk.END)
            insert_into_listbox(similar)
        else:
            result_label.config(text="0 results found")
            listbox.delete(0, tk.END)
    except ValueError:
        pass



#frame to hold widget
frame = tk.Frame()
frame.pack(fill=tk.BOTH)
#place frame
frame.place(relx=0.525, rely=0.135, anchor=tk.CENTER)


# Create a label
label = tk.Label(root, text="Welcome to Our Library")
label.pack(pady=10)
#label to show result type
ln = len(data_list)
result_label = tk.Label(frame, text=f'{ln} books available')
result_label.pack(side=tk.BOTTOM)

#search
entry = tk.Entry(frame, width=83)
entry.pack(side=tk.LEFT, padx=5, pady=5)


# Create a search button
search_button = tk.Button(frame, text="search", command=perform_search, bd=2)
search_button.pack(side=tk.LEFT, padx=5, pady=10)

entry.bind('<Return>', perform_search)

#header for list box
header = tk.LabelFrame(root)
header.place(relx=0.582, rely=0.206, anchor=tk.CENTER)

header_label = tk.Label(header, text=f"ID{'':<5}|   Title {'':>95}          Genre", width=92, font=('Arial', 13), anchor=tk.W)
header_label.pack()



#SCROLLBAR for listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.place(relx=0.88, rely=0.55, anchor=tk.CENTER, height=555, width=18)
# Create a Listbox widget
listbox = tk.Listbox(root, width=92, height= 26, yscrollcommand=scrollbar.set, font=('Arial', 13))  # Width and height can be adjusted
listbox.place(relx=0.58, rely=0.55, anchor=tk.CENTER)
scrollbar.config(command=listbox.yview)
insert_into_listbox(data_list)

#selection
listbox.bind("<Button-1>", show_book_details )
listbox.bind("<<ListboxSelect>>", show_book_details )


close_button = tk.Button(root, text="close", command=close_system, bd=4, height=2, width=8)
close_button.place(relx=0.5, rely=0.9)





#BOOK DETAILS FRAME
details_win = tk.Frame(root, relief=tk.SOLID, borderwidth=4)
details_win.place(relx=0.145, rely=0.3, height=400, width=400, anchor=tk.N)

det_head = tk.LabelFrame(details_win)
det_head.pack()
det_head_label = tk.Label(det_head, text="BOOK details", width=60)
det_head_label.pack()

#details
text_box = tk.Text(details_win)
text_box.pack()



# Run the Tkinter main loop
root.mainloop()
