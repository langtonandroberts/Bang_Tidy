from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.title("Login Form")
screen.geometry("440x440")
screen.resizable(False,False)

def ring():
    screen.bell()


def register():
    name=name_info.get()
    age=age_info.get()
    phone=phone_info.get()
    email=email_info.get()
    
    if name=="":
        messagebox.showerror("Error","Cannot be left blank \nPlease enter your name")
    elif age=="":
        messagebox.showerror("Error","Cannot be left blank \nPlease enter your Age")
    elif phone=="":
        messagebox.showerror("Error","Cannot be left blank \nPlease enter your Phone Number")
    elif email=="":
        messagebox.showerror("Error","Cannot be left blank \nPlease enter your Email") 
    else:
        #Label(screen,text="Registration Sucessfull",font="20",fg="green").place(x=135,y=285)
        name_entry.delete(0,END)
        age_entry.delete(0,END)
        phone_entry.delete(0,END)
        email_entry.delete(0,END)
        messagebox.showinfo("THANK YOU","Registration\nSucksesfull")
        name_entry.focus()

def clear():
    name_entry.delete(0,END)
    age_entry.delete(0,END)
    phone_entry.delete(0,END)
    email_entry.delete(0,END)
    
#,,,label,,,
Label(screen,text="Registration Form",font="ariel 20 bold",bg="red",fg="white").pack(fill="both")

Label(screen,text="Name",font="20").place(x=40,y=75)
Label(screen,text="Age",font="20").place(x=40,y=115)
Label(screen,text="Phone No",font="20").place(x=40,y=155)
Label(screen,text="Email Id",font="20").place(x=40,y=195)

#,,, Entry Box,,,,,
name_info=StringVar()
age_info=StringVar()
phone_info=StringVar()
email_info=StringVar()
name_entry=Entry(screen,font="10",bd=4,textvariable=name_info)
name_entry.place(x=140,y=75)
age_entry=Entry(screen,font="10",bd=4,textvariable=age_info)
age_entry.place(x=140,y=115)
phone_entry=Entry(screen,font="10",bd=4,textvariable=phone_info)
phone_entry.place(x=140,y=155)
email_entry=Entry(screen,font="10",bd=4,textvariable=email_info)
email_entry.place(x=140,y=195)

#,,, Buttons
Button(screen,text="Register",font="20",command=register).place(x=185,y=240)
Button(screen,text="Clear",font="20",command=clear).place(x=345,y=365)

name_entry.focus()

screen.bell()
screen.mainloop()

