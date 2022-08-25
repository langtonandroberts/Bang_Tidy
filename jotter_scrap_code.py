
import tkinter as tk

root = tk.Tk()

amount = tk.Label(root,text = "£0.00")
amount.grid(row=1,column=0)

def updat():
    try:amount.config(text="£{:,.2f}".format(float(entry.get())))
    except:amount.config(text = "£0.00")
entry = tk.Entry(root)
entry.grid(row=0,column=0)
entry.bind("<Key>",lambda v: root.after(10,updat))



root.mainloop()























