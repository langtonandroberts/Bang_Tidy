from tkinter import *
from tkinter import ttk
from tkinter import font
from types import WrapperDescriptorType
from datetime import datetime
import pytz
import time
from typing import Literal
IST=pytz.timezone()

# ,,,,,,,, window config ,,,,,,,,,,,,,,,,
window=Tk()
window.title("start of programming FIRST WINDOW")
window.geometry("1000x500+0+0")
window.config(background="#cbf2f0")


# ,,,,,,,,,,,,Tab window ,,,,,,,,,,,,,,,,,
notebook=ttk.Notebook(window)

tab1=Frame(notebook,bg="#cbf2f0")#,,new frame for tab1.
tab2=Frame(notebook,bg="#cbf2f0")#,,new frame for tab2.
tab3=Frame(notebook,bg="#cbf2f0")#,,new frame for tab3.
tab4=Frame(notebook,bg="#cbf2f0")#,,new frame for tab4.
tab5=Frame(notebook,bg="#cbf2f0")#,,new frame for tab5.

notebook.add(tab1,text="Expenses")
notebook.add(tab2,text="Vat")
notebook.add(tab3,text="Income")
notebook.add(tab4,text="Bank")
notebook.add(tab5,text="Vat",padding=10,)#,,padding gives a boarder.
notebook.pack(expand=True,fill=BOTH)

#Label(tab1,text="Hello, this is Tab 1",bg="#cbf2f0").pack()#expand=True,fill=BOTH)#width=50,height=25
Label(tab2,text="You are not subscribed to VAT",bg="#cbf2f0").pack()#expand=True,fill=BOTH)
Label(tab3,text="Hello, this is Tab 3",bg="#cbf2f0").pack()#expand=True,fill=BOTH)
#Label(tab4,text="Goodbye, this is Tab 4",bg="#cbf2f0").pack()#expand=True,fill=BOTH)
#Label(tab5,text="Hello, this is Tab 5",bg="#cbf2f0").pack()#expand=True,fill=BOTH)


# ,,,,,,,,,,,,,,, frames within tab4 ,,,,,,,,,,,,,,,,,,,,,
frame1=Frame(tab4,height=120,width=180,bg="#cbf2f0",bd=1,relief=SUNKEN)#frame and every thing placed in it.
frame1.place(x=0,y=0)
frame2=Frame(tab4,height=120,width=520,bg="#cbf2f0",bd=1,relief=SUNKEN)#frame and every thing placed in it.
frame2.place(x=180,y=0)
frame3=Frame(tab4,height=30,width=700,bg="#cbf2f0",bd=1,relief=RAISED)#frame and every thing placed in it.
frame3.place(x=0,y=120)
# ,,,,,,,,,,,,,,, frames within tab 1 ,,,,,,,,,,,,,,,,,,,,,,
frame4=Frame(tab1,height=750,width=160,bg="#6182fa",bd=1,relief=RAISED)
frame4.place(x=1,y=1)#pack(side=LEFT,fill=Y,ipady=2)
frame5=Frame(tab1,height=40,width=600,bg="#6182fa",bd=1,relief=RAISED)#frame and every thing placed in it.
frame5.place(x=193,y=90)
frame6=Frame(tab1,height=40,width=600,bg="#6182fa",bd=1,relief=RAISED)#frame and every thing placed in it.
frame6.place(x=860,y=90)
frame7=Frame(tab1,height=500,width=600,bg="#bee6da",bd=1,relief=FLAT)#frame and every thing placed in it.
frame7.place(x=193,y=130)
frame8=Frame(tab1,height=400,width=600,bg="#bee6da",bd=1,relief=FLAT)#frame and every thing placed in it.
frame8.place(x=860,y=130)

frame11=Frame(tab1,bg="#6182fa",height=13,width=1400,bd=1,relief=RAISED)
frame11.place(x=160,y=1) #pack(side=LEFT,fill=Y,ipadx=2)

# ,,,,,,,,,,,,,,,,, Buttons function on click ,,,,,,,,,,,,,,,,,,
count=0
def click():
    global count
    count+=1
    print (count)
    #print("You clicked the button")
    #photo=PhotoImage()

def select():
    notebook.select(4)
    
# ,,,,,,,,,,,, button creation ,,,,,,,,,, 
#button=Button(tab5,
              #text="click me!",
              #command=select,
              #font=("Comic Sans",10),
              #fg="black",
              #bg="white",
              #activeforeground="blue",
              #activebackground="white",
              #state=ACTIVE,
              #relief=RAISED,# SUNKEN
              #bd=3,
              #padx=5,
              #pady=5)
              #,,,DISABLED
              #image=photo,
              #compound="bottom")
#button.pack()

buton=Button(tab2,text="Navigate to tab 5",command=select).pack()

# ,,,,,,,,,,,,,,, entry box for ,,,,,,,,,,,,,,,,,,,,,,
pincode_text_var=StringVar()
pincode_text=Entry(tab4,width=11,bg="white",fg="black",font="verdana 11",textvariable=pincode_text_var)
pincode_text.place(x=220,y=40)
pincode_text["textvariable"]=pincode_text_var

# ,,,,, date box tab4 ,,,,,,,,,,
date_text_var=StringVar()
date_text=Entry(tab4,width=11,bg="white",fg="black",font="verdana 11",textvariable=pincode_text_var)
date_text.place(x=380,y=40)
date_text["textvariable"]=date_text_var

# ,,,,,,,, (Hover on mouse) button tabe1 tab1 ,,,,,,,,
#add_expense_btn=Button(tab1,text="Add Expense",font=("Helvetica",15),bg="#3bf7b6")
#add_expense_btn.place(x=860,y=550)




# ,,,,,,,,,,,,,, button on tab4 ,,,,,,,,,,,,
search_vaccine_btn=Button(tab4,text="Submit",bg="#cbf2f0",relief=RAISED)
search_vaccine_btn.place(x=600,y=25)

# ,,,,,,,,,,,,,,,, labels for tab1 ,,,,,,,,,,,,,,,,,,,,,
menu_lbl_1=Label(tab1,text="HOME PAGE",bg="#6182fa",fg="white",font="verdana 12")
menu_lbl_1.place(x=20,y=140)
menu_lbl_2=Label(tab1,text="INCOME",bg="#6182fa",fg="white",font="verdana 12")
menu_lbl_2.place(x=20,y=180)
menu_lbl_3=Label(tab1,text="EXPENSES",bg="#6182fa",fg="white",font="verdana 12")
menu_lbl_3.place(x=20,y=220)
menu_lbl_4=Label(tab1,text="BANK",bg="#6182fa",fg="white",font="verdana 12")
menu_lbl_4.place(x=20,y=260)


exp_title_lbl=Label(tab1,text="Expenses",bg="#cbf2f0",font="verdana 20")#bold
exp_title_lbl.place(x=190,y=40)
exp_heading_lbl=Label(tab1,text="Expenses",bg="#6182fa",fg="white",font="verdana 12")
exp_heading_lbl.place(x=195,y=100)
add_exp_heading_lbl=Label(tab1,text="Enter New Expenses Hear",bg="#6182fa",fg="white",font="verdana 12")
add_exp_heading_lbl.place(x=865,y=100)

# ,,,,,,,,,,,,,,,, labels for tab1 ,,,,,,,,,,,,,,,,,,,,,
lbl_ent_date=Label(tab1,text="Date",bg="#bee6da",font="verdana 11")
lbl_ent_date.place(x=200,y=134)
lbl_exp_ttl=Label(tab1,text="Expense",bg="#bee6da",font="verdana 11")
lbl_exp_ttl.place(x=295,y=134)
lbl_val_ttl=Label(tab1,text="Amount",bg="#bee6da",font="verdana 11")
lbl_val_ttl.place(x=415,y=134)
lbl_descr_ttl=Label(tab1,text="Description",bg="#bee6da",font="verdana 11")
lbl_descr_ttl.place(x=515,y=134)



lbl_exp_ent_date=Label(tab1,text="Date:",bg="#bee6da",font="verdana 11")
lbl_exp_ent_date.place(x=864,y=134)
lbl_exp_ttl=Label(tab1,text="Expense Title:",bg="#bee6da",font="verdana 11")
lbl_exp_ttl.place(x=864,y=200)
lbl_amount=Label(tab1,text="Amount:",bg="#bee6da",font="verdana 11")
lbl_amount.place(x=864,y=266)
lbl_pay_type=Label(tab1,text="Payment Type:",bg="#bee6da",font="verdana 11")
lbl_pay_type.place(x=864,y=332)
lbl_discr=Label(tab1,text="Short Discription:",bg="#bee6da",font="verdana 11")
lbl_discr.place(x=864,y=398)

label_date=Label(tab4,text="Date",bg="#cbf2f0",font="verdana 11")
label_date.place(x=380,y=15)
label_dateformat=Label(tab4,text="[dd-mm-yyyy]",bg="#cbf2f0",fg="black",font="verdana 7")
label_dateformat.place(x=420,y=18)

label_search=Label(tab4,text="Search \n Please Press",bg="#cbf2f0",font="verdana 8")
label_search.place(x=584,y=70)

label_head_result=Label(tab4,text=" Status      \tCenter-Name\t                        Age-Group     Vaccine        Dose_1        Dose_2          Total",bg="#cbf2f0",fg="black",font="verdana 8")
label_head_result.place(x=10,y=125)

# ,,,,,,,, Text Boxes for tab1 ,,,,,,,,,,,,,,,
first_box=Text(tab1,height=14,width=10,bg="#f0eeeb",fg="black",bd=1,relief=SUNKEN,font="verdana 10")
first_box.place(x=200,y=174)

#=Text(tab4,height=20,width=31,bg="white",fg="red",relief=RAISED,font="verdana 10")
#label_time_now.place(x=73,y=152)

second_box=Text(tab1,height=14,width=14,bg="#f0eeeb",fg="black",relief=SUNKEN,font="verdana 10")
second_box.place(x=288,y=174)

third_box=Text(tab1,height=14,width=12,bg="#f0eeeb",fg="black",relief=SUNKEN,font="verdana 10")
third_box.place(x=410,y=174)

fourth_box=Text(tab1,height=14,width=33,bg="#f0eeeb",fg="black",relief=SUNKEN,font="verdana 10")
fourth_box.place(x=515,y=174)

#result_box_d2=Text(tab1,height=2,width=10,bg="#f0eeeb",fg="black",relief=SUNKEN,font="verdana 10")
#result_box_d2.place(x=196,y=334)

#result_box_total=Text(tab1,height=2,width=10,bg="#f0eeeb",fg="black",relief=SUNKEN,font="verdana 10")
#result_box_total.place(x=196,y=374)

# ,,,,,,,,,, check box ,,,,,,,,,,,,,,,,,
#def update_clock():
    #raw_TS=datetime.now()# IST
    #date_now=raw_TS.strftime("%d %B %y")
    #time_now=raw_TS.strftime("%H:%M:%S %p")
    #label_date_now.config(text=date_now)
    #label_time_now.config(text=time_now)
    #label_time_now.after(1000,update_clock)
    
#update_clock

def insert_today_date():
    raw_TS=datetime.now()# IST
    formatted_now=raw_TS.strftime("%d-%m-%y")
    date_text_var.set(formatted_now)

#update_clock

chkbox_today_var=IntVar()
today_date_chkbox=Checkbutton(tab4,text="Today",bg="#cbf2f0",variable=chkbox_today_var,onvalue=1,offvalue=0,command=insert_today_date)
today_date_chkbox.place(x=375,y=65)



# ,,,,,,,,,,,,,, entry box with submit button tab1 Expenses ,,,,,,,,,,,
def submit():
    username=entry.get()
    print("Hello "+username)
    #entry.config(state=DISABLED)#,,disabels box after entry.

def delete():
    entry.delete(0,END) #which part to delete,,(0)start to end.

def backspace():
    entry.delete(len(entry.get())-1,END)#,deletes last caracter in string
    
 

entry=Entry(tab1,
            font=("Arial",11),
            fg="#828385",
            bg="#f0eeeb")
entry.insert(0,"enter amount")#, puts prompt text in box.
entry.place(width=140,x=865,y=300)



# ,,submit buttons for tab1 ,,,,,,,,,,,,
submit_button=Button(tab1,text="Save/Continue",font=5,bg="#6182fa",fg="white",command=submit)
submit_button.place(x=900,y=550)#(pady=10)#,padx gives space between buttons.
delete_button=Button(tab1,text="Delete",font=5,bg="#6182fa",fg="white",command=delete)#,deletes everything in box.
delete_button.place(x=1050,y=550)
backspace_button=Button(tab1,text="Back Space",font=5,bg="#6182fa",fg="white",command=backspace)
backspace_button.place(x=1132,y=550)


# ,,,,,,,,, Wrappers ,,,,,,,,,,,,,

opts=StringVar()
#wrapper1=LabelFrame(frame4,text="Wrapper 1",bg="#cbf2f0")
#wrapper2=LabelFrame(frame4,text="Wrapper 2",bg="#cbf2f0")
#wrapper3=LabelFrame(tab1,text="Wrapper 3",bg="#cbf2f0")
#wrapper1.pack(padx=10,pady=10,fill="both",expand="yes")
#wrapper2.pack(padx=10,pady=10,fill="both",expand="yes")
#wrapper3.pack(padx=10,pady=10,fill="both",expand="yes")
#Label(wrapper1,textvariable=opts,bg="#cbf2f0").grid(row=0,column=0,padx=10,pady=5,sticky=W)
#Label(wrapper2,textvariable=opts,bg="#cbf2f0").grid(row=0,column=0,padx=10,pady=5,sticky=W)

#mycombo2=ttk.Combobox(frame8,textvariable=opts)
#mycombo2["values"]=["Supplier", "Utility", "Transport", "Rent",]
#mycombo2.place(x=4,y=239)#grid(padx=10,pady=5)
#mycombo2.current(0)

mycombo=ttk.Combobox(frame8,textvariable=opts)
mycombo["values"]=["Suplier", "Utility", "Transport", "Other"]
mycombo.place(x=4,y=100)#grid(padx=10,pady=5)
mycombo.current(0)

lbl8=Label(tab5,text="Home Page",bg="#cbf2f0")
lbl8.grid(row=0,column=0,padx=10,pady=10)
#entry8=entry(frame4,textvariable=f_name)
#entry8.grid(padx=10,pady=5)
lbl9=Label(tab5,text="Banking",bg="#cbf2f0")
lbl9.grid(row=1,column=0,padx=10,pady=5)

#lbl7=Label(wrapper2,text="Middel Name")
#lbl7.grid(row=2,column=0,padx=10,pady=5)

# ,,,,,,,,,,,,,,,,, Menue bar (File) ,,,,,,,,,,,,,,,,,,,,
def openFile():
    print("File has been opened!")
    
def saveFile():
    print("File has been saved!")    

def select2():
    notebook.select(1)#moves to tab selected in().

def select3():
    notebook.select(2)#moves to tab selected in().

def select4():
    notebook.select(3)#moves to tab selected in().


menubar=Menu(window)
window.config(menu=menubar)
fileMenu=Menu(menubar,tearoff=0,font=("Arial",10,))
menubar.add_cascade(label="What do you want to do?",font=("Arial",10),menu=fileMenu)
fileMenu.add_command(label="Pay money IN",command=select)# command moves between tabs when selected.
fileMenu.add_command(label="Pay money OUT",command=select2)# command moves between tabs when selected.
fileMenu.add_command(label="Vat summery",command=select3)# command moves between tabs when selected.
fileMenu.add_command(label="Bank summery",command=select4)# command moves between tabs when selected.

fileMenu.add_separator()# puts line between menues.
fileMenu.add_command(label="Exit",command=quit)#command quits program ie close down.


#,,,,,,,,,,,, status bar on bottom ,,,,,,,,,,,,,,,,,,,,
status=Label(window,text="Year End Solutions,,,,",background="#cbf2f0",bd=1,relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X,ipady=2)




window.mainloop() # ,,, this puts window on screen ,,,,,,