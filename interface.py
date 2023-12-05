import tkinter as tk
import backend
import time

root = tk.Tk()
root.title("Library Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

def insert_into_listbox(lst):

    
    for row in lst:
        sp = 8 - len(str(row[0]))  # Calculate space for numbers with different number of digits
        bk_padding = '_' * (65 - len(row[1]))
        listbox.insert(tk.END, f"{row[0]:<{sp}} | {row[1]}{bk_padding} {row[2]}")


def item_selected(event=None):
    try:
        new_window.destroy()
        time.sleep(0.1)
    except:
        pass
    select = (listbox.get(listbox.curselection()))
    new_window = tk.Toplevel(root)
    new_window.title('Book details')
    new_window.geometry("800x400+500+200")
    new_window_label = tk.Label(new_window, text = select)
    new_window_label.pack()



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
frame.place(relx=0.475, rely=0.135, anchor=tk.CENTER)


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
header.place(relx=0.532, rely=0.206, anchor=tk.CENTER)

header_label = tk.Label(header, text=f"ID{'':<5}|   Title {'':>95}          Genre", width=92, font=('Arial', 13), anchor=tk.W)
header_label.pack()



#SCROLLBAR for listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.place(relx=0.9, rely=0.55, anchor=tk.CENTER, height=555, width=18)
# Create a Listbox widget
listbox = tk.Listbox(root, width=92, height= 26, yscrollcommand=scrollbar.set, font=('Arial', 13))  # Width and height can be adjusted
listbox.place(relx=0.53, rely=0.55, anchor=tk.CENTER)
scrollbar.config(command=listbox.yview)
insert_into_listbox(data_list)

#selection
listbox.bind("<Return>", item_selected)
listbox.bind("<Button-1>", item_selected)





close_button = tk.Button(root, text="close", command=close_system, bd=4, height=2, width=8)
close_button.place(relx=0.5, rely=0.9)


# Run the Tkinter main loop
root.mainloop()
