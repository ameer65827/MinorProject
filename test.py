import tkinter as tk

def close_window():
    root.destroy()  # Close the Tkinter window

root = tk.Tk()
root.title("Close Window Example")

# Button 1 to close window
button1 = tk.Button(root, text="Close Window 1", command=close_window)
button1.pack()

# Button 2 to close window
button2 = tk.Button(root, text="Close Window 2", command=close_window)
button2.pack()

root.mainloop()
