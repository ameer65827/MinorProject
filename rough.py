import tkinter as tk

# Sample list of book names
book_names = [
    "Book 1",
    "Book 2",
    "Book 3",
    "Book 4",
    "Book 5",
    "Book 6",
    "Book 7",
    "Book 8",
    "Book 9",
    "Book 10"
]

root = tk.Tk()
root.title("List of Books")

# Create a Listbox widget
listbox = tk.Listbox(root, width=50, height=10)  # Width and height can be adjusted
listbox.pack(padx=10, pady=10)

# Add book names to the Listbox
for book in book_names:
    listbox.insert(tk.END, book)

root.mainloop()
