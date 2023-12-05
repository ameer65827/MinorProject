import tkinter as tk

root = tk.Tk()

# Create a vertical scrollbar
v_scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a horizontal scrollbar
h_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Create a Listbox
listbox = tk.Listbox(root, width=20, height=1, xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
listbox.pack()

# Link the scrollbars to the Listbox
h_scrollbar.config(command=listbox.xview)
v_scrollbar.config(command=listbox.yview)

# Insert items into the Listbox (for demonstration)
for i in range(1, 21):
    listbox.insert(tk.END, f"Item {i}")

root.mainloop()
