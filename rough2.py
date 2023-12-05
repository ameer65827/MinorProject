import tkinter as tk

root = tk.Tk()
root.title("Centered Listbox with Scrollbar")
root.geometry("400x300")

# Create a frame to center the Listbox
frame = tk.Frame(root)
frame.pack(expand=True)

# Create a vertical scrollbar
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a Listbox and attach the scrollbar
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=20, height=8)
listbox.pack(padx=10, pady=10)

scrollbar.config(command=listbox.yview)

# Inserting sample data into the Listbox
for i in range(20):
    listbox.insert(tk.END, f"Item {i+1}")

root.mainloop()