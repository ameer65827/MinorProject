import tkinter as tk

root = tk.Tk()
root.title("Library Management System")


data_list = [
    "Apple", "Banana", "Orange", "Grapes", "Strawberry", "Watermelon",
    "Pineapple", "Mango", "Peach", "Kiwi", "Apricot", "Pear", "Plum",
    "Cherry", "Blueberry", "Raspberry", "Blackberry", "Lemon", "Lime",
    "Cranberry", "Coconut", "Pomegranate", "Fig", "Guava", "Papaya",
    "Lychee", "Passion Fruit", "Star Fruit", "Dragon Fruit", "Persimmon",
    "Durian", "Avocado", "Jackfruit", "Kumquat", "Nectarine", "Tangerine",
    "Clementine", "Rambutan", "Melon", "Honeydew", "Cantaloupe", "Soursop",
    "Barberry", "Currant", "Gooseberry", "Elderberry", "Mulberry", "Quince"
]

def on_button_click():
    label.config(text="Button clicked!")



def perform_search(event=None):
    try:
        search_word = (entry.get()).lower()  # Get data entry field
        similar  = []
        for word in data_list:
            if search_word in word.lower():
                similar.append(word)
                
        if similar:
            result_label.config(text=f"{search_word} found !")

            #showing result
            listbox.delete(0, tk.END)
            for result in similar:
                listbox.insert(tk.END, result)
        else:
            result_label.config(text=f"{search_word} not found")
            listbox.delete(0, tk.END)
    except ValueError:
        result_label.config(text="Not Valid")

# Create the main window


#frame to hold widget
frame = tk.Frame()
frame.pack(fill=tk.BOTH)

root.geometry("1100x720")

# Create a label
label = tk.Label(root, text="Welcome to Our Library")
label.pack(pady=20)

#search
entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=5, pady=5)


# Create a search button
search_button = tk.Button(frame, text="search", command=perform_search, bd=2)
search_button.pack(side=tk.LEFT, padx=5, pady=10)

entry.bind('<Return>', perform_search)


#create a label to show search result
result_label = tk.Label(root, text="")
result_label.pack(pady=70)


# Create a Listbox widget
listbox = tk.Listbox(root, width=100, height= 24)  # Width and height can be adjusted
listbox.pack(padx=10, pady=10)


but1 = tk.Button(root, text="close", command=root.destroy, bd=4)
# but1.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
but1.pack(pady=5)


#place frame
frame.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

for item in data_list:
    listbox.insert(tk.END, item)

# Run the Tkinter main loop
root.mainloop()
