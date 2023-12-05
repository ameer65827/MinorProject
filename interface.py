import tkinter as tk
import backend

root = tk.Tk()
root.title("Library Management System")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

def insert_into_listbox(lst):
    for row in lst:
        sp = (8 - len(str(row[0]))) # calculate space for numbers with different no. of digits
        listbox.insert(tk.END, f"{row[0]:<{sp}}  |   {row[1]}")

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
frame.place(relx=0.45, rely=0.135, anchor=tk.CENTER)


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

#SCROLLBAR for listbox
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.place(relx=0.9, rely=0.55, anchor=tk.CENTER, height=555, width=18)
# Create a Listbox widget
listbox = tk.Listbox(root, width=100, height= 26, yscrollcommand=scrollbar.set, font=('Arial', 13))  # Width and height can be adjusted
listbox.place(relx=0.53, rely=0.55, anchor=tk.CENTER)
scrollbar.config(command=listbox.yview)
insert_into_listbox(data_list)




but1 = tk.Button(root, text="close", command=close_system, bd=4)
but1.place(relx=0.5, rely=0.9)


# Run the Tkinter main loop
root.mainloop()
