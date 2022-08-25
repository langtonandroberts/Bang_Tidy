from tkinter import *
from tkinter import ttk
from tkinter import font
from types import WrapperDescriptorType
from typing import Literal
import sqlite3
#from PIL import ImageTk,Image



# ,,,,,,,, window config ,,,,,,,,,,,,,,,,
window=Tk()
#window.iconbitmap("yes.ico")
window.title("Expense Window,,, Year End Solutions ")
window.geometry("1000x500+0+0")
window.config(background="#fcfcfa")

#,,,,place a photo on the screen
#my_img=ImageTk.PhotoImage(Image.open("___.png"))
#my_label=Label(image=my_image)
#my_label.pack()


# ,,,,,,,,,, database ,,,,,,,,,,,,,,
# ,,,,,,,,, create database ,,,,,,,,
conn=sqlite3.connect("expense_data.db")#(conn)connect to sqlite3
c=conn.cursor()#(c)create cursor
#c.execute("""CREATE TABLE data(
        #date integer,
        #exp_type text,
        #amount integer,
        #descrip text
        #)""")


conn.commit()#commit changes
conn.close()#close connection
# ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,


# ,,,,, tabs ,,(NOT working),,,,,,,,
#notebook=ttk.Notebook(window)
#tab1=Frame(notebook,bg="#fcfcfa")#,,new frame for tab1.
#tab2=Frame(notebook,bg="#fcfcfa")#,,new frame for tab1.
#notebook.add(tab1,text="Home Screen")
#notebook.add(tab2,text="Expenses")
#notebook.pack(expand=True,fill=BOTH)

# ,,,,,,,,,,,,,,, frames  ,,,,,,,,,,,,,,,,,,,,,,
frame3=Frame(window,bg="#e2f723",height=20,width=1400,bd=1,relief=FLAT)
frame3.place(x=160,y=0) #pack(side=LEFT,fill=Y,ipadx=2)
frame4=Frame(window,height=774,width=160,bg="#e2f723",bd=1,relief=FLAT)
frame4.place(x=0,y=0)#pack(side=LEFT,fill=Y,ipady=2)
frame5=Frame(window,height=40,width=600,bg="#e2f723",bd=1,relief=FLAT)
frame5.place(x=193,y=90)
frame6=Frame(window,height=40,width=600,bg="#e2f723",bd=1,relief=FLAT)
frame6.place(x=860,y=90)
frame7=Frame(window,height=500,width=600,bg="white",bd=1,relief=FLAT)
frame7.place(x=193,y=130)
frame8=Frame(window,height=500,width=600,bg="white",bd=1,relief=FLAT)
frame8.place(x=860,y=130)

# ,,,,,,,,,,,,,,,, title headings ,,,,,,,,,,,,,,,,,,,
exp_title_lbl=Label(window,text="Expenses",bg="#fcfcfa",font="verdana 20")#bold
exp_title_lbl.place(x=190,y=40)
exp_heading_lbl=Label(window,text="Expenses",bg="#e2f723",fg="black",font="verdana 12")
exp_heading_lbl.place(x=195,y=100)
add_exp_heading_lbl=Label(window,text="Enter New Expenses Hear",bg="#e2f723",fg="black",font="verdana 12")
add_exp_heading_lbl.place(x=865,y=100)

# ,,,,,,,,,,,,,,,, labels left side ,,,,,,,,,,,,,,,,,,,,,
lbl_ent_date=Label(window,text="Date",bg="white",font="verdana 11")
lbl_ent_date.place(x=200,y=148)
lbl_exp_ttl=Label(window,text="Expense",bg="white",font="verdana 11")
lbl_exp_ttl.place(x=295,y=148)
lbl_val_ttl=Label(window,text="Amount",bg="white",font="verdana 11")
lbl_val_ttl.place(x=415,y=148)
lbl_descr_ttl=Label(window,text="Description",bg="white",font="verdana 11")
lbl_descr_ttl.place(x=515,y=148)

# ,,,,,,,,,,,,,,,, labels right side ,,,,,,,,,,,,,,,,,,,,,
lbl_exp_ent_date=Label(window,text="Date:",bg="white",font="verdana 11")
lbl_exp_ent_date.place(x=864,y=134)
lbl_exp_ttl=Label(window,text="Expense Title:",bg="white",font="verdana 11")
lbl_exp_ttl.place(x=864,y=200)
lbl_amount=Label(window,text="Amount:",bg="white",font="verdana 11")
lbl_amount.place(x=864,y=266)
lbl_pay_type=Label(window,text="Payment Type:",bg="white",font="verdana 11")
lbl_pay_type.place(x=864,y=332)
lbl_discr=Label(window,text="Short Discription:",bg="white",font="verdana 11")
lbl_discr.place(x=864,y=398)

# ,,,,,,,, Text Boxes left side ,,,,,,,,,,,,,,,
first_box=Text(window,height=14,width=10,bg="white",fg="black",bd=1,relief=SUNKEN,font="verdana 10")
first_box.place(x=200,y=174)
second_box=Text(window,height=14,width=14,bg="white",fg="black",relief=SUNKEN,font="verdana 10")
second_box.place(x=288,y=174)
third_box=Text(window,height=14,width=12,bg="white",fg="black",relief=SUNKEN,font="verdana 10")
third_box.place(x=410,y=174)
fourth_box=Text(window,height=14,width=33,bg="white",fg="black",relief=SUNKEN,font="verdana 10")
fourth_box.place(x=515,y=174)

# ,,,,,,,,,,,,,, button commands ,,,,,,,,,,,
def submit():
    username=entry.get()
    print("Hello "+username)
    #entry.config(state=DISABLED)#,,disabels box after entry.

def delete():
    entry.delete(0,END) #which part to delete,,(0)start to end.

def backspace():
    entry.delete(len(entry.get())-1,END)#,deletes last caracter in string

entry=Entry(window,
            font=("Arial",11),
            fg="#828385",
            bg="#f0eeeb")
entry.insert(0,"DD/MM/YYYY")#, puts prompt text in box.
entry.place(width=500,x=868,y=160)

# ,,,,,,,,,,,, buttons for SAVE, DELETE, BACK SPACE ,,,,,,,,,,,,
submit_button=Button(window,text="Save/Continue",font=1,bg="black",fg="white",command=submit)#bd=2,relief=RIDGE
submit_button.place(x=900,y=550)#(pady=10)#,padx gives space between buttons.
delete_button=Button(window,text="Delete",font=1,bg="black",fg="white",command=delete)#,deletes everything in box.
delete_button.place(x=1050,y=550)
backspace_button=Button(window,text="Back Space",font=1,bg="black",fg="white",command=backspace)
backspace_button.place(x=1132,y=550)

# ,,,,,,,,,,,,, buttons on side frame (Menu) ,,,,,,,,,,,,,,,,,,,,,
button_1=Button(window,text="Home Screen",font=1,bg="#e2f723",fg="#888d94",bd=0,activebackground="#e2f723")#command=submit
button_1.place(x=10,y=148)#(pady=10)#,padx gives space between buttons.
button_2=Button(window,text="Income",font=1,bg="#e2f723",fg="#888d94",bd=0,activebackground="#e2f723")#command=submit
button_2.place(x=10,y=188)#(pady=10)#,padx gives space between buttons.
button_3=Button(window,text="Expenses",font=1,bg="#e2f723",fg="#888d94",bd=0,activebackground="#e2f723")#command=submit
button_3.place(x=10,y=228)#(pady=10)#,padx gives space between buttons.
button_4=Button(window,text="Bank",font=1,bg="#e2f723",fg="#888d94",bd=0,activebackground="#e2f723")#command=submit
button_4.place(x=10,y=268)#(pady=10)#,padx gives space between buttons.
button_5=Button(window,text="Payroll",font=1,bg="#e2f723",fg="#888d94",bd=0,activebackground="#e2f723")#command=submit
button_5.place(x=10,y=308)#(pady=10)#,padx gives space between buttons.
button_6=Button(window,text="Account",font=1,bg="#e2f723",fg="#888d94",bd=0,activebackground="#e2f723")#command=submit
button_6.place(x=10,y=348)#(pady=10)#,padx gives space between buttons.
button_7=Button(window,text="Vat",font=1,bg="#e2f723",fg="#888d94",bd=0,activebackground="#e2f723")#command=submit
button_7.place(x=10,y=388)#(pady=10)#,padx gives space between buttons.
button_8=Button(window,text="Help!",font=1,bg="#e2f723",fg="#888d94",bd=0,activebackground="#e2f723")#command=submit
button_8.place(x=10,y=428)#(pady=10)#,padx gives space between buttons.


#,,,,,,,,,,,, status bar on bottom ,,,,,,,,,,,,,,,,,,,,
status=Label(window,text="Year End Solutions,,,,",background="#e2f723",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X,ipady=2)


window.mainloop() # ,,, this puts window on screen ,,,,,,
