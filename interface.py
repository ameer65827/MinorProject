import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

number_list = [23, 56, 12, 78, 45, 90, 34, 67, 31, 55]

def perform_search():
    try:
        search_number = int(entry.get())  # Get the number from the entry field
        if search_number in number_list:
            result_label.config(text=f"Number {search_number} found!")
        else:
            result_label.config(text=f"Number {search_number} not found")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Library Management System")

#frame to hold widget
frame = tk.Frame()
frame.pack(fill=tk.BOTH)

root.geometry("1100x720")

# Create a label
label = tk.Label(root, text="Welcome to Our Library")
label.pack(pady=10)

#search
entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=5, pady=5)


# Create a search button
search_button = tk.Button(frame, text="search", command=perform_search, bd=2)
search_button.pack(side=tk.LEFT, padx=5, pady=10)


#create a label to show search result
result_label = tk.Label(root, text="")
result_label.pack(pady=40)



# Create a Listbox widget
listbox = tk.Listbox(root, width=100, height= 24)  # Width and height can be adjusted
listbox.pack(padx=10, pady=20)





but1 = tk.Button(root, text="close", command=root.destroy, bd=4)
# but1.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
but1.pack(pady=5)


#place frame
frame.place(relx=0.5, rely=0.08, anchor=tk.CENTER)

# Run the Tkinter main loop
root.mainloop()
