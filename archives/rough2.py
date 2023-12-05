import tkinter as tk

def open_popup():
    popup = tk.Toplevel(root)
    popup.title("Buy Item")

    # Widgets for selecting item and quantity
    item_label = tk.Label(popup, text="Select Item:")
    item_label.pack()

    # Include other widgets as needed (e.g., dropdowns, entry fields)

    # Button to confirm purchase
    confirm_button = tk.Button(popup, text="Buy", command=popup.destroy)
    confirm_button.pack()

root = tk.Tk()
root.title("Main Window")

buy_button = tk.Button(root, text="Buy Item", command=open_popup)
buy_button.pack(padx=20, pady=10)

root.mainloop()
