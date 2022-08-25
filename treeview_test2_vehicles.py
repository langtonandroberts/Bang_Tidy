

# Treeview
# https://youtu.be/lqHcKT7ZwOo
# https://tkdocs.com/tutorial/tree.html
# https://youtu.be/KAgffQ6MWE0
# https://youtu.be/yICGS9Lv86s
# https://youtu.be/EKpRxK5EEcM

#selection modes
# .focus()method selects 1 item.
# .selection()method 1 or more selected items.
#selectmode=tk.EXTENDED, (default mode) this lets you select more than 1 row.
#selectmode=tk.BROWSE, this selects 1 row.
#selectmode=tk.NONE, NO selection at all.


import tkinter as tk
from tkinter import ttk
from turtle import bgcolor
from PIL import Image, ImageTk

# create root window
root = tk.Tk()

style = ttk.Style()
style.configure("Treeview.Heading",
                foreground ="red",
                )


#style.map("Treeview.Heading",background=[("active", "black")])
#print(style.map("Treeview.Heading","background"))

#load an image
with Image.open('download.png') as img, \
    Image.open('yes.ico') as img_2, \
    Image.open('settings.ico') as img_3:
    download_image=ImageTk.PhotoImage(img)
    download_image_2=ImageTk.PhotoImage(img_2)
    download_image_3=ImageTk.PhotoImage(img_3)


# create a treeview
column_names = ('vehicle_name', 'year', 'colour')
treeview_vehicle = ttk.Treeview(root)#, columns=column_names)
treeview_vehicle.configure(columns=column_names)#displaycolumns=("vehicle_name", "colour")#This hides columns.


# Headings you can use the treeview index instead of the column name,ie year= index 1. vehicle_name=index 0.
treeview_vehicle.heading('#0', text="Vehicle Type",
                         image=download_image,
                         anchor=tk.W)
treeview_vehicle.heading('vehicle_name', text="Vehicle Name")
treeview_vehicle.heading('year', text="Year")
treeview_vehicle.heading('colour', text="Colour")

# Align text in column.
treeview_vehicle.column("vehicle_name", anchor=tk.W)
# width of column
treeview_vehicle.column("year",width=70,minwidth=50)
# Fix size
treeview_vehicle.column("#0",stretch=False)

# Parent row
sedan_row=treeview_vehicle.insert(parent="",
                        index=tk.END,
                        text="Sedan",
                        )
ford_row=treeview_vehicle.insert(parent="",
                        index=tk.END,
                        text="Ford",
                        )
nissan_row=treeview_vehicle.insert(parent="",
                        index=tk.END,
                        text="Nissan",
                        )


# child row.
treeview_vehicle.insert(parent=sedan_row,
                        index=tk.END,
                        values=("Nissan Versa", "2010", "Silver"))
treeview_vehicle.insert(parent=sedan_row,
                        index=tk.END,
                        values=("Nissan Juke", "2021", "Black"))

treeview_vehicle.insert(parent=ford_row,
                        index=tk.END,
                        values=("Toyota Camry", "2012", "Blue"))

treeview_vehicle.insert(parent=nissan_row,
                        index=tk.END,
                        values=("Duke", "2022", "Red"))


# Fills the window with the treeview.
treeview_vehicle.pack(fill=tk.BOTH,expand=True)



# run the window.
root.mainloop()