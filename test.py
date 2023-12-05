import tkinter as tk

def single_click(event):
    selected_item = listbox.get(listbox.curselection())  # Get the selected item
    print(f"Single-clicked: {selected_item}")

root = tk.Tk()

# Create a listbox
listbox = tk.Listbox(root)
listbox.pack()

# Insert items into the listbox (just an example)
for item in range(1, 11):
    listbox.insert(tk.END, f"Item {item}")

# Bind a function to the single-click event
listbox.bind("<Button-1>", single_click)  # Single-click event

root.mainloop()
