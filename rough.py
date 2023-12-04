import tkinter as tk

def on_button_click():
    label.config(text="Button clicked!")

def close_window():
    root.destroy()
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
root.title("Libraray Management System")

root.geometry("1000x600")

# Create a label
label = tk.Label(root, text="Welcome to the interface")
label.pack()

#search
entry = tk.Entry(root)
entry.pack()

# Create a button
search_button = tk.Button(root, text="search", command=perform_search)
search_button.pack()

#create a label to show search result
result_label = tk.Label(root)
result_label.pack()

but1 = tk.Button(root, text="close", command=close_window)
but1.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


# Run the Tkinter main loop
root.mainloop()
