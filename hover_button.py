from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("hover button")
root.geometry("500x400")


# ,,,,,,,,,,, Hover Button and show text on hover ,,,,,,,,,,,,,,,,,,,,
def button_hover(e):
    my_button["bg"]="white"
    status_label.config(text="I'm Hovering over the Button!")

def button_leave(e):
    my_button["bg"]="SystemButtonFace"
    status_label.config(text="")

def popup():
    response=messagebox.askyesno("This is my Popup!", "Hello world")
    #Label(root,text=response).pack()# this will returns 1 for yes & 0 for no.see what it returns.
    if response==1:
        Label(root,text="You clicked Yes").pack()
    else:
        Label(root,text="You clicked No").pack()

my_button=Button(root,text="Click Me",command=popup,font=("Helvetica",28),relief=FLAT)
my_button.pack(pady=50)
status_label=Label(root,text="",bd=1,height=1,relief=SUNKEN,anchor=E)
status_label.pack(fill=X,side=BOTTOM,ipady=2)
my_button.bind("<Enter>",button_hover)
my_button.bind("<Leave>",button_leave)
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# ,,,,,,,,,,,,, message boxes ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# ,,types of messages, showInfo,showwarning,askQuestion,askOkCancel,askYesNo,,,
#def popup():
    #response=messagebox.showinfo("This is my Popup!", "Hello world")
    #Label(root,text=response).pack()# this will returns 1 for yes & 0 for no.see what it returns.
    #if response==1:
        #Label(root,text="You clicked Yes").pack()
    #else:
        #Label(root,text="You clicked No").pack()


#Button(root,text="Popup",command=popup).pack()
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,




root.mainloop()
