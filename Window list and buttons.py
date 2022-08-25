# This code Opens a window, puts basic buttons and labels on it.
from sqlite3.dbapi2 import SQLITE_CREATE_TABLE
from tkinter import *
from tkinter import ttk
#from tkinter import Optional





root = Tk() #This is the startup window, must go first. Place things on this.
root.title("Year End Solutions first window")
root.geometry("700x400")


#,,,,,,,,, inport files ,,,,,,,,,,,,,(NOT WORKING PROPERLY)
#root.filename = filedialog.askopenfilename(initialdir="c/users",title="Select a file",filetypes=(("all files","*.*")))



#,,,,,,,, checkboxes ,,,,,,,,,,
var=IntVar()

# ,,,,,,, dropdown box ,,,,,
clicked=StringVar()
clicked.set("Options")
drop=OptionMenu(root,clicked,"Option 1", "Option 2", "Option 3")
drop.grid(column=0,row=0)


#,,,,,, second window ,,,,,,,,,

def open():
    top=Toplevel()
    #lbl= Label(top,text="Second Window").pack()
    top.title("Year End Solutions Second Window")
    #btn2=Button(top,text="close window",command=top.destroy).pack
    top.geometry("400x400")
    ttk.Button(top, text="Exit", command=top.destroy).pack()
    

c=Checkbutton(root,text="Check this box",variable=var)
c.grid(column=1,row=5)

#btn=Button(root, text="Open second window",command=open).grid(column=1)

frm = ttk.Frame(root,padding=10) # puts a border in the frame = to 10 pixels,,,,
frm.grid() # grid setting,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

#,,,,,, second window ,,,,,,,,,

#top=Toplevel()
#lbl= Label(top,text="Second Window").pack()
#top.title("Year End Solutions Second Window")

#,,,,,,, Places a label on grid ,,,,,,,,,,,,,,,,,,,,,,,

ttk.Label(frm, text="Label 1").grid(column=2)
ttk.Label(frm, text="label 2").grid(column=2)
ttk.Label(frm, text="label 3").grid(column=2)
ttk.Label(frm, text="label 4").grid(column=2)



#,,,,,, Places a basic Button on frame top left corner,,,,,,,
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="Close", command=root.destroy).grid(column=1, row=1)
ttk.Button(frm, text="Return", command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text="Button 4", command=root.destroy).grid(column=1, row=3)
ttk.Button(frm, text="Open second window",command=open).grid(column=3,row=6)







root.mainloop() #This must go at the end. 
