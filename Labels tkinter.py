
#https://youtu.be/qtWHBjCZQ68

import tkinter as tk
from tkinter import *

#example--var_1.set("Company Name"),,this can be set as a StringVar and changes when you use var_1.
#example--var_1.set(result)#puts the result of a calculation in label

my_w=tk.Tk()
my_w.geometry('400x100')

comp_name=StringVar()

def my_update():
    comp_name.set(e1.get())
    e1.delete(0,END)#clears entry box

label_1=tk.Label(my_w, textvariable=comp_name, width=25,bg="black",fg="white")
label_1.grid(row=1, column=3)

#label_2=tk.Label(my_w,textvariable=new_text)
#label_2.grid(row=1,column=4)

e1=tk.Entry(my_w, width=20,bd=0,relief=SOLID)
e1.grid(row=1, column=1)

b1=tk.Button(my_w, text='Update', command=lambda:my_update())#when button clicked change value of label to value of entry box..
b1.grid(row=1,column=2)

comp_name.set('Company Name Here')

my_w.mainloop()