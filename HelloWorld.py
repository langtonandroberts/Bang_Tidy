from textwrap import fill
from tkinter import *
import tkinter # Downloads tkinter all.
#from PIL import ImageTk,Image
#,,,,,,,,, Creates a window on screen ,,,,,,,,,,,,,,,,,,,,,
root=Tk() 
#,,,,,,,,,,, Name on top of window.(left corner) ,,,,,,,,,,
root.title("HELLO WORLD")

       #root.iconbitmap(),,,,,finds logo for left corner,,,,,,,,,,
root.geometry("550x550") #,,,,defines size of window when ran,,,.

# ,,,,,,,,,,,,,,,, Creating a Label widget .,,,,,,,,,,,,,,,,
#myLabel=Label(root,text="Do not click this button") # could add .grid(row=0, column=0)

#,,,,,,,,,,,,,,,, placeing the Label on screen.,,,,,,,,,,,,
# myLabel.grid(row=1,column=1)
#myLabel.pack() 

#def myClick():# tell it to do something.(create a function),,,,,,,,,
     #myLabel=Label(root,text="Stop Clicking")
     #myLabel.pack(side=LEFT)
    
# Creates Button... padx=50 makes button longer.padx=20 for higher.
#myButton=Button(root, text="Click me", command=myClick,padx=10,pady=10) # State=DISABLED Could be added.
#myButton.pack() # Puts button on Label under text.


#,,,,,,,,,,,,,, Menu Bar ,,,,,,,,,,,,,,,,,,
def doNothing():
     print("Its working ok for now")

#root=Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label="BANK",menu=subMenu)
subMenu.add_command(label="MONEY OUT,,",command=doNothing)
subMenu.add_command(label="MONEY IN,,",command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit menu",command=doNothing)

editMenu=Menu(menu)
menu.add_cascade(label="RECORDS",menu=editMenu)
editMenu.add_command(label="Customers,,",command=doNothing)

editMenu=Menu(menu)
menu.add_cascade(label="INCOME",menu=editMenu)
editMenu.add_command(label="Customers,,",command=doNothing)


toolbar=Frame(root,bg="blue")
toolbar.pack(side=TOP,padx=2,pady=2,fill=X)
insertButt=Button(toolbar,text="SAVE",command=doNothing)
insertButt.place(x=53,y=2)#pack(side=TOP,padx=2,pady=2)
printButt=Button(toolbar,text="PRINT",command=doNothing)
printButt.pack(padx=2,pady=2)
#my_image= ImageTk.PhotoImage(Image.open("logo.png"))
#my_label=Label(image=my_image)
#my_label.pack()

#,,,,,,,,,,,, status bar on bottom ,,,,,,,,,,,,,,,,,,,,
status=Label(root,text="Year End Solutions,,,,",bd=2,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)

root.mainloop()# enter everything between this.
