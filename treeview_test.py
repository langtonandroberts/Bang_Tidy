import tkinter as tk
from tkinter import ttk


# create root window
root = tk.Tk()
root.title('Treeview Demo - Hierarchical Data')
root.geometry('400x200')

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# create a treeview
tree = ttk.Treeview(root)
tree.heading('text', text='Departments', anchor='w')


# adding data
tree.insert('', tk.END, text='Administration', open=False)
tree.insert('', tk.END, text='Logistics', open=False)
tree.insert('', tk.END, text='Sales', open=False)
tree.insert('', tk.END, text='Finance', open=False)
tree.insert('', tk.END, text='IT', open=False)

# adding children of first node
tree.insert('', tk.END, text='John Doe', open=False)
tree.insert('', tk.END, text='Jane Doe', open=False)
tree.move(5, 0, 0)
tree.move(6, 0, 1)

# place the Treeview widget on the root window
tree.grid(row=0, column=4, sticky='nsew')

# run the app
root.mainloop()