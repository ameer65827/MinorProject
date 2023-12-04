import tkinter as tk

def open_popup(event):
    selected_item = listbox.get(listbox.curselection())
    popup = tk.Toplevel(root)
    popup.title("Popup Window")
    popup.geometry("300x200")
    popup.attributes('-topmost', 'true')  # Make the popup window remain on top

    label = tk.Label(popup, text=f"Selected: {selected_item}")
    label.pack(padx=20, pady=30)

root = tk.Tk()
root.title("Main Window")

frame = tk.Frame(root)
frame.pack(padx=50, pady=20)

# Header label
header_label = tk.Label(frame, text="ID              Description")
header_label.pack(side=tk.TOP, fill=tk.BOTH)

listbox = tk.Listbox(frame, width=40, height=5)
listbox.pack()

# Sample data with two columns
data = [
    ("1. Item 1", "Description 1"),
    ("2. Item 2", "Description 2"),
    ("3. Item 3", "Description 3"),
    ("4. Item 4", "Description 4"),
]

# Insert formatted data into the listbox
for item in data:
    listbox.insert(tk.END, f"{item[0]:<15} {item[1]}")

# Bind function to listbox selection event
listbox.bind("<Double-Button-1>", open_popup)

root.mainloop()
