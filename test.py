import tkinter as tk

def show_book_details(book_info):
    sub_window = tk.Toplevel(root)
    sub_window.title(f"Book Details: {book_info['title']}")

    # Creating a big box using a Text widget
    text_box = tk.Text(sub_window, width=50, height=10)
    text_box.pack()

    # Organizing book details in columns
    details = [
        ("Title:", book_info['title']),
        ("Reference ID:", book_info['reference_id']),
        ("Author:", book_info['author']),
        ("Publisher:", book_info['publisher']),
        ("Reference Number:", book_info['reference_number'])
        # Add more book details here
    ]

    # Inserting book details into the text box in columns
    for detail, value in details:
        text_box.insert(tk.END, f"{detail:<20}{value}\n")

    close_button = tk.Button(sub_window, text="Close", command=sub_window.destroy)
    close_button.pack()

# Sample book information (replace this with your actual book data)
book_data = {
    'title': 'Book Title',
    'reference_id': '12345',
    'author': 'Author Name',
    'publisher': 'Publisher Name',
    'reference_number': '6789'
    # Add more book details as needed
}

root = tk.Tk()
root.title("Library Management System")

show_details_button = tk.Button(root, text="Show Book Details", command=lambda: show_book_details(book_data))
show_details_button.pack()

root.mainloop()
