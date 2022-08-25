from logging import PlaceHolder, root
from tkinter import*
from tkinter import filedialog
from turtle import left

root=Tk() # Generates window
root.title("Button and Entry widget")
# Center app in middle of monitor/screen.
app_width=1000
app_height=500
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width / 2)-(app_width / 2)
y=(screen_height /2)-(app_height / 2)
root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')#

frame=LabelFrame(root,text="This is my Frame...",padx=5,pady=5,fg="blue") # Pads (space) inside of frame.
frame.pack(padx=5,pady=5) # Pads (space) outside of frame.



# ,,,,, make's Entry widget and put on screan,,,,,,,,,,,,,,,,,,,,,,,,,,
e=StringVar()
e=Entry(frame,width=20)
e.pack()

def myClick():# Command for click on Button
        greetings="Hello " + e.get() # Gets the info in Entry box. (Look into Insert command)
        e.delete(0,END) # Clears Entry box after Click.
        myLabel=Label(root,text=greetings,fg="blue") # Prints to Label.
        myLabel.pack()


# ,,,,, Makes Button widget and puts on screan ,,,,,,,,,,,,,,,,,,,,,,,,
myButton=Button(frame,text="Enter your name",command=myClick)
myButton.pack(padx=5,pady=5)






root.mainloop()#,,keeps window on screen.
