
from asyncio.windows_events import NULL
from cProfile import label
from cgitb import text
import imghdr
from mimetypes import common_types
from telnetlib import STATUS
import pyttsx3
import PyPDF2 
import datetime 
import datetime
from datetime import timedelta 
from distutils import text_file
import random
#from curses.textpad import Textbox
#from curses.textpad import Textbox
from distutils.command.config import config
from email.mime import image
from faulthandler import disable
from itertools import product
from msilib.schema import ComboBox
from msvcrt import setmode
from optparse import Values
from random import random
from sre_parse import State
import tkinter as tk
from tkinter import ANCHOR, W, Canvas, ttk
import time 
from tkinter import*
import sqlite3
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import font
from tkinter.tix import IMAGE
from turtle import bgcolor, fillcolor, home, pd, position, title, width
from tkinter import filedialog as fd
from typing import Counter, Literal, Type
from tkinter import ttk
from unicodedata import category
from urllib import response
from click import command
from colorama import Cursor
from numpy import integer, record
from pyparsing import col
#from click import command 
from tkcalendar import*
from PIL import Image
from datetime import date
from tkinter import filedialog
import win32api
import os,sys
import csv
import win32print
import win32api
from datetime import datetime
from PIL import ImageTk, Image
from pydoc import doc
from turtle import width
from docx import Document
from docx.shared import Inches
import win32com.client
from PIL import Image, ImageTk
import csv
import random 
import cv2 
import numpy 

LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 11)
SMALL_FONT = ("Helvetica", 10)
HEIGHT = 700
WIDTH = 500

def popupmsg(msg):
    popup = Tk()
    #popup.overrideredirect(True)
    popup.wm_title("!")
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10,padx=10)
    B1 = Button(popup, text="Close",command = popup.destroy)
    B1.pack()
    app.bell()
    popup.resizable(False,False)
    popup.geometry('300x200+700+400')
    popup.mainloop()

class HoverButton(Button):
    """ Button that changes color to activebackground when mouse is over it. """
    def __init__(self, master, **kw):
        super().__init__(master=master, **kw)
        self.default_Background = self.cget('background')
        self.hover_Background = self.cget('activebackground')
        self.bind('<Enter>', self.on_enter)
        self.bind('<Leave>', self.on_leave)

    def on_enter(self, e):
        self.config(background=self.hover_Background)

    def on_leave(self, e):
        self.config(background=self.default_Background)



def client_reg_window():#Client Registration Form Popup Window,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    #ring()
    client_reg_window = Toplevel()
    client_reg_window.title("New Client Register Form (For new client's only)")
    client_reg_window.geometry('800x310+360+240')
    client_reg_window.resizable(False,False)
    frame_1 = Frame(client_reg_window, height=HEIGHT, width=WIDTH)
    frame_1.pack()
    #booking_form.overrideredirect(True)#,,removes top title from window.
    
    #,,Master frame Quick Client Register Form,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    master_frame=LabelFrame(frame_1,text='Quick Client Registration Form')
    master_frame.grid(row=0,column=0,padx=10,pady=10)
    contact_info=LabelFrame(master_frame,text="Contact information")
    contact_info.grid(row=0,column=0,padx=10,pady=10)
    button_command=LabelFrame(master_frame,text="What next buttons")
    button_command.grid(row=1,column=0,padx=10,pady=3,ipadx=3,ipady=3,sticky="E")
    info_notes=LabelFrame(master_frame,text="Employee Info:")
    info_notes.grid(row=1,column=0,padx=10,pady=10,ipadx=3,ipady=3,sticky="W")

    #,,,add new record to database.
    def save_client_record():
        if title_combo.get()=="":
            #messagebox.showinfo("MISSING DATA", "Title needed\nAll fields needed!")
            popupmsg("Title Needed")
        elif tb_2.get()=="":
            popupmsg("First name needed.")
        elif tb_3.get()=="":
            popupmsg("Please enter\nLast name.")
        elif tb_4.get()=="":
            popupmsg("Please enter\nAddress.")
        elif tb_5.get()=="":
            popupmsg("Please enter\nTown.")
        elif tb_6.get()=="":
            popupmsg("Please enter\ncity.")
        elif tb_7.get()=="":
            popupmsg("County needed.")
        elif tb_8.get()=="":
            popupmsg("Please enter\nPostcode.")
        elif tb_9.get()=="":
            popupmsg("Phone number needed.")
        elif tb_10.get()=="":
            popupmsg("Email needed.")
        else:
            #,,, Create a database or connect to one that executes.
            conn=sqlite3.connect("tree_crm.db")
            #,,,create a cursor.
            c=conn.cursor()
            #,,,add new record.
            c.execute("INSERT INTO clients VALUES(:title,:first,:last,:id,:address,:town,:city,:county,:postcode,:phone,:email)",
                    {
                    "title":title_combo.get().capitalize(),
                    "first":tb_2.get().capitalize(),
                    "last":tb_3.get().capitalize(),
                    "id":tb_11.get(),
                    "address":tb_4.get().title(),
                    "town":tb_5.get().title(),
                    "city":tb_6.get().title(),
                    "county":tb_7.get().title(),
                    "postcode":tb_8.get().upper(),
                    "phone":tb_9.get(),
                    "email":tb_10.get(),
                    #"pet_name1":tb_11.get().capitalize(),
                    #"pet_name2":pet2_ent.get().capitalize(),
                    })
            #,,,commit the changes
            conn.commit()
            #,,, close the connection
            conn.close()
            #,,,Clear entry boxes.
            title_combo.delete(0,END)
            tb_2.delete(0,END)
            tb_3.delete(0,END)
            tb_4.delete(0,END)
            tb_5.delete(0,END)
            tb_6.delete(0,END)
            tb_7.delete(0,END)
            tb_8.delete(0,END)
            tb_9.delete(0,END)
            tb_10.delete(0,END)
            #pet1_ent.delete(0,END)
            #pet2_ent.delete(0,END)
            client_reg_window.destroy()
            messagebox.showinfo("UPDATED", "New Client Successfully\nSaved to client database!")
            
            #my_tree.delete(*my_tree.get_children())
            #query_database()
    
    
    
    #,,,clear entry
    def clear_boxes():
        #,,,Clear entry boxes.
        title_combo.delete(0,END)
        tb_2.delete(0,END)
        tb_3.delete(0,END)
        tb_4.delete(0,END)
        tb_5.delete(0,END)
        tb_6.delete(0,END)
        tb_7.delete(0,END)
        tb_8.delete(0,END)
        tb_9.delete(0,END)
        tb_10.delete(0,END)
        
    
    
    lab_1=Label(contact_info,text="Title:")
    lab_1.grid(row=0,column=0,padx=3,pady=3,sticky="w")
    title_combo=ttk.Combobox(contact_info,width=7,state="readonly")
    title_combo['values']=["Dr", "Mr", "Mrs", "Miss", "Mis"]
    title_combo.grid(row=0,column=1,padx=3,pady=3,sticky="w")
    lab_2=Label(contact_info,text="First Name:")
    lab_2.grid(row=1,column=0,padx=3,pady=3,sticky="w")
    tb_2=Entry(contact_info,width=15)
    tb_2.grid(row=1,column=1,padx=3,pady=3,sticky="w")
    lab_3=Label(contact_info,text="Last Name:")
    lab_3.grid(row=1,column=2,padx=3,pady=3,sticky="w")
    tb_3=Entry(contact_info,width=15)
    tb_3.grid(row=1,column=3,padx=3,pady=3,sticky="w")
    lab_4=Label(contact_info,text="Address:")
    lab_4.grid(row=2,column=0,padx=3,pady=3,sticky="w")
    tb_4=Entry(contact_info,width=25)
    tb_4.grid(row=2,column=1,padx=3,pady=3,sticky="w")
    lab_5=Label(contact_info,text="Town:")
    lab_5.grid(row=2,column=2,padx=3,pady=3,sticky="w")
    tb_5=Entry(contact_info,width=25)
    tb_5.grid(row=2,column=3,padx=3,pady=3,sticky="w")
    lab_6=Label(contact_info,text="City:")
    lab_6.grid(row=2,column=4,padx=3,pady=3,sticky="w")
    tb_6=Entry(contact_info,width=28)
    tb_6.grid(row=2,column=5,padx=(3,10),pady=3,sticky="w")
    lab_7=Label(contact_info,text="County:")
    lab_7.grid(row=3,column=0,padx=3,pady=3,sticky="w")
    tb_7=Entry(contact_info,width=25)
    tb_7.grid(row=3,column=1,padx=3,pady=3,sticky="w")
    lab_8=Label(contact_info,text="Postcode:")
    lab_8.grid(row=3,column=2,padx=3,pady=3,sticky="w")
    tb_8=Entry(contact_info,width=10)
    tb_8.grid(row=3,column=3,padx=3,pady=3,sticky="w")
    lab_9=Label(contact_info,text="Mobile Phone:")
    lab_9.grid(row=4,column=0,padx=3,pady=3,sticky="w")
    tb_9=Entry(contact_info,width=15)
    tb_9.grid(row=4,column=1,padx=3,pady=3,sticky="w")
    lab_10=Label(contact_info,text="Email:")
    lab_10.grid(row=4,column=2,padx=3,pady=3,sticky="w")
    tb_10=Entry(contact_info,width=30)
    tb_10.grid(row=4,column=3,padx=3,pady=3,sticky="w")
    lab_11=Label(contact_info,text="")
    lab_11.grid(row=0,column=4,padx=3,pady=3,sticky="w")
    tb_11=Entry(contact_info,width=5,relief=FLAT,bg="SystemButtonFace")
    tb_11.grid(row=0,column=5,padx=3,pady=3,sticky="w")
    lab_12=Label(info_notes,text="Once completed continue to  New Pet Registration in the ribbon menu\nPet's are regestered seperate and given a uniqe ID.",fg="brown",font=SMALL_FONT)
    lab_12.grid(row=0,column=0,padx=3,pady=3,sticky="w")
    
    #,,,Buttons,Client regestration form,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    clear_button=HoverButton(button_command,text="CLEAR ALL",cursor="hand2",font=LARGE_FONT,activebackground='#e2f723',bg="systembuttonface",fg="black",command=clear_boxes)#lambda: popupmsg('Not supported just yet!'))
    clear_button.grid(row=0,column=2,padx=2,pady=2)#,sticky="E")
    save_button=HoverButton(button_command,text="SAVE",cursor="hand2",font=LARGE_FONT,activebackground='#e2f723',bg="systembuttonface",fg="black",command=save_client_record)#lambda: popupmsg('Not supported just yet!'))
    save_button.grid(row=0,column=1,padx=(5,2),pady=2)#,sticky="E")
    exit_button=HoverButton(button_command,text="EXIT FORM",cursor="hand2",font=LARGE_FONT,activebackground='orange',bg="#e2f723",fg="black",command=client_reg_window.destroy)
    exit_button.grid(row=0,column=3,padx=2,pady=2,sticky="E")
    
#,,,Pet Booking in form Popup Window,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
def pet_window():#,Popup window
    #app.bell()
    pet_window = Toplevel()
    pet_window.title("Pet Details Form.(can be filled in on arrival)")
    pet_window.geometry('695x310+400+104')
    pet_window.resizable(False,False)
    dt_stamp=time.strftime("%d/%m/%Y")
    #,,Frames,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    frame_1 = Frame(pet_window, height=HEIGHT, width=WIDTH)
    frame_1.grid(row=0,column=0,padx=5,pady=5)
    
    widget_box_frame = LabelFrame(frame_1)#frame for combo boxes.
    widget_box_frame.pack(padx=10,pady=10,ipadx=10)
    button_frame = Frame(widget_box_frame)
    button_frame.grid(row=7,column=0,columnspan=4,pady=10)
    
    
    
    click_get=StringVar()
    click_get.set("")
    vaccin_get=StringVar()
    vaccin_get.set("")
    
    
    '''def query_pet_database():
        global pet_tree
        #,,,clear the treeview
        for record in pet_tree.get_children():
            pet_tree.delete(record)
        #,,, Create a database or connect to one.
        conn=sqlite3.connect("tree_crm.db")
        #,,,create a cursor.
        c=conn.cursor()
        #,,,get row using ID,,,,,,,
        c.execute("SELECT rowid, * FROM customer_pets")
        records=c.fetchall()
        #,,,Add Record Entry Boxes,,,
        global count
        count = 0 #,,,start of ID
        
        for record in records:
            if count % 2==0:
                pet_tree.insert(parent="",index="end",iid=count,text="",values=(record[1],record[2],record[3],record[0],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17]), tags=("evenrow",))
            else:
                pet_tree.insert(parent="",index="end",iid=count,text="",values=(record[1],record[2],record[3],record[0],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11],record[12],record[13],record[14],record[15],record[16],record[17]), tags=("oddrow",))
            #,,,increment counter adds 1 to each record entered (ID number),,,,
            count +=1   
        #,,,commit the changes
        conn.commit()
        #,,,close the connection
        conn.close()
        #petinfo.set("")
    query_pet_database()'''
        
    
    
    
    def add_pet():
        if entry_1.get()=="":
            popupmsg("Owner Name needed.")
        elif pet_name_ent.get()=="":
            popupmsg("Pet name needed.")
        elif entry_6.get()=="":
            popupmsg("Ener a status.")
        elif entry_2.get()=="":
            popupmsg("Type of Pet needed.")
        elif entry_10.get()=="":
            popupmsg("Ener the Pet's age\nIn years (aprox).")
        elif entry_7.get()=="":
            popupmsg("Ener the Pet's D.O.B.")
        elif entry_3.get()=="":
            popupmsg("Please enter Breed.")
        elif entry_11.get()=="":
            popupmsg("Size of Pet Needed.")
        elif micro_combo.get()=="":
            popupmsg("Is the Pet Micro Chipped?.")
        elif entry_9.get()=="":
            popupmsg("Do you Have the chip number?\nEnter NO if NO.")
        elif pet_gender_ent.get()=="":
            popupmsg("Please enter Gender.")
        elif entry_12.get()=="":
            popupmsg("Please enter Weight.")
        elif entry_5.get()=="":
            popupmsg("Please enter Colour.")
        elif entry_13.get()=="":
            popupmsg("Error","Please choose temper.")
        #elif pet_gender_ent.get()=="":
            #popupmsg("Date Regirstered.")
        elif entry_health.get()=="":
            popupmsg("What is the Pet\nHealth status?.")
        elif attribute_ent.get()=="":
            popupmsg("Doe's the Pat have any habits?.")
        else:
            #,,, Connect to database.
            conn=sqlite3.connect("tree_crm.db")
            #,,,create a cursor.
            c=conn.cursor()
            #,,,add new record.
            c.execute("INSERT INTO customer_pets VALUES(:pet_owner,:pet_name,:pet_age,:status,:pet_type,:pet_dob,:breed,:size,:micro_chip,:chip_number,:gender,:weight,:colour,:temper,:reg_date,:health,:attributes,:photo)",
                    {
                    "pet_owner":entry_1.get(),
                    "pet_name":pet_name_ent.get(),
                    "pet_age":entry_6.get(),
                    "status":entry_2.get(),
                    "pet_type":entry_10.get(),
                    "pet_dob":entry_7.get(),
                    "breed":entry_3.get(),
                    "size":entry_11.get(),
                    "micro_chip":micro_combo.get(),
                    "chip_number":entry_9.get(),
                    "gender":pet_gender_ent.get(),
                    "weight":entry_12.get().upper(),
                    "colour":entry_5.get(),
                    "temper":entry_13.get(),
                    "reg_date":dt_stamp,#date
                    "health":entry_health.get(),
                    "attributes":attribute_ent.get(),
                    "photo":NULL,
                    })
            #,,,commit the changes
            conn.commit()
            #,,, close the connection
            conn.close()
            #,,,Clear entry boxes.
            entry_1.set('')
            pet_name_ent.set('')
            entry_6.delete(0,END)
            entry_2.set('')
            entry_10.set('')
            entry_7.delete(0,END)
            entry_3.set('')
            entry_11.set('')
            micro_combo.set('')
            entry_9.delete(0,END)
            pet_gender_ent.set('')
            entry_12.delete(0,END)
            entry_5.set('')
            entry_13.set('')
            entry_health.current(5)
            attribute_ent.set('')
            pet_window.destroy()
            messagebox.showinfo("COMPLETED", "Pet details successfully saved!")
            #popupmsg("SAVED.")
            
        
    #,,,Clear entry boxes.
    def clear_pet():
        entry_1.set('')
        pet_name_ent.set('')
        entry_6.delete(0,END)
        entry_2.set('')
        entry_10.set('')
        entry_3.set('')
        entry_11.set('')
        micro_combo.set('')
        entry_9.delete(0,END)
        pet_gender_ent.set('')
        entry_12.delete(0,END)
        entry_5.set('')
        entry_13.set('')
        entry_health.current(5)
        attribute_ent.current(0)
        entry_9.configure(bd=0,bg="systembuttonface",state="disabled")
        click_get.set("")
        ent9_text.set("")
        vaccin_combo.current(0)
        
    
    
    def vaccin_click(e):
        if vaccin_combo.get()== "Yes":
            vaccin_get.set("Vaccine name:")
            #vaccine_date = DateEntry(widget_box_frame,setmode="day",date_pattern="dd/mm/yyyy",state='readonly',width=11)
            #vaccine_date.grid(row=6,column=3,padx=3,pady=5,sticky=W)  
            vac_name_combo=ttk.Combobox(widget_box_frame,width=11,state="normal")#,state='readonly')
            vac_name_combo['values']=['Bordetella', 'DHPP', 'Leptosirosis', 'Parvovirus', 'Hepatitis', 'Distemper', 'Kennel Cough']
            vac_name_combo.current(0)
            vac_name_combo.grid(row=6,column=3,padx=3,pady=5,sticky=W) 
        elif vaccin_combo.get()== "No":
            vac_name_combo=ttk.Combobox(widget_box_frame,width=11,state='readonly')#,state='readonly')
            vac_name_combo['values']=['N/A']
            vac_name_combo.current(0)
            vac_name_combo.grid(row=6,column=3,padx=3,pady=5,sticky=W) 
            vaccin_get.set("")
        else:
            vac_name_combo=ttk.Combobox(widget_box_frame,width=11,state='readonly')#,state='readonly')
            vac_name_combo['values']=['N/A','Bordetella', 'DHPP', 'Leptosirosis', 'Parvovirus', 'Hepatitis', 'Distemper', 'Kennel Cough']
            vac_name_combo.current()
            vaccin_get.set("")
            
    
    
    def combo_click(e):
        if micro_combo.get()== "Yes":
            click_get.set("Chip ID:")
            entry_9.delete(0,END)
            entry_9.configure(bg="white",fg="black",state="normal",bd=1)
        else:
            click_get.set("")
            entry_9.delete(0,END)
            entry_9.configure(bg="systembuttonface",fg="gray",bd=1)
            ent9_text.set("N/A")
            
    
    #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    #,,,create Pet table in database,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    conn=sqlite3.connect("tree_crm.db")
    #,,,create a cursor.
    c=conn.cursor()
    #,,,create Pet table.,,,,,,,,,,,,,,,,,,,,,,,
    c.execute("""CREATE TABLE if not exists customer_pets(
        pet_owner text,
        pet_name text,
        pet_age integer,
        status text,
        pet_type text,
        pet_dob integar,
        breed text,
        size text,
        micro_chip text,
        chip_number integer,
        gender text,
        weight real,
        colour text,
        temper text,
        reg_date integer integer,
        health text,
        attributes text,
        photo BLOB)
        """)
    #,,,commit the changes
    conn.commit()
    #,,,close the connection
    conn.close()
    
    #,,takes names from data base and appends to combo box,,,,,,,,,,,,
    conn=sqlite3.connect("tree_crm.db")
    #,,,create a cursor.
    c=conn.cursor()
    
    owners=[]
    sql5=("SELECT rowid,  first_name, last_name FROM clients")
    #,,,get row using ID,,,,,,,
    c.execute(sql5)
    ids=c.fetchall()
    for i in ids:
        owners.append(str(i[1])+" "+i[2])#+" "+i[2])#,,i[0]=ID/i[1]=first_name/i[2]=last_name

    
    pet=[]
    #,,takes pet names from Clients data base table and appends to combo box,,,,,,,,,,,,
    conn=sqlite3.connect("tree_crm.db")
    #,,,create a cursor.
    c=conn.cursor()
    
    pet=[]
    sqlpet=("SELECT rowid,  pet_name FROM customer_pets")
    #,,,get row using ID,,,,,,,
    c.execute(sqlpet)
    ids=c.fetchall()
    for i in ids:
        pet.append(str(i[1]))#+" ")+i[2])
        
    #,,labels and buttons,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
    lbl_1 = Label(widget_box_frame,text='Pet Owner:')
    lbl_1.grid(row=0,column=0,padx=3,pady=5,sticky=W)
    entry_1 = ttk.Combobox(widget_box_frame,width=15,state='readonly')
    entry_1['values']=owners
    entry_1.grid(row=0,column=1,sticky=W)
    
    lbl_2 = Label(widget_box_frame,text='Status:')
    lbl_2.grid(row=1,column=0,padx=3,pady=5,sticky=W)
    entry_2=ttk.Combobox(widget_box_frame,width=11,state='readonly')
    entry_2['values']=['active', 'not active']
    entry_2.grid(row=1,column=1,padx=3,pady=5,sticky=W)
    
    lbl_3 = Label(widget_box_frame,text='Breed:')
    lbl_3.grid(row=2,column=0,padx=3,pady=5,sticky=W)
    entry_3=ttk.Combobox(widget_box_frame,width=15,state='readonly')
    entry_3['values']=['Grayhound', 'Mixed breed', 'Pussy']
    entry_3.current()
    entry_3.grid(row=2,column=1,padx=3,pady=5,sticky=W)
    
    lbl_4 = Label(widget_box_frame,text='Gender:')
    lbl_4.grid(row=3,column=0,padx=3,pady=5,sticky=W)
    pet_gender_ent=ttk.Combobox(widget_box_frame,width=7,state='readonly')
    pet_gender_ent['values']=['Dog', 'Bitch', 'Tom', 'Queen', 'Molly', 'Other']
    pet_gender_ent.current()
    pet_gender_ent.grid(row=3,column=1,padx=3,pady=5,sticky=W)
    
    lbl_5 = Label(widget_box_frame,text='Colour:')
    lbl_5.grid(row=4,column=0,padx=3,pady=5,sticky=W)
    entry_5=ttk.Combobox(widget_box_frame,width=15,state='readonly')
    entry_5['values']=['Red', 'Brindel', 'Black', 'White', 'Blue','Gray','Brown','Spotty','Patchy']
    entry_5.current()
    entry_5.grid(row=4,column=1,padx=3,pady=5,sticky=W)
    
    lbl_6 = Label(widget_box_frame,text='Pet age:')
    lbl_6.grid(row=0,column=4,padx=3,pady=5,sticky=W)
    entry_6 = ttk.Combobox(widget_box_frame,width=10,state='readonly')
    entry_6['values']=['0.5','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
    entry_6.grid(row=0,column=5,sticky=W)
    
    lbl_7 = Label(widget_box_frame,text='Pet D.O.B:')
    lbl_7.grid(row=1,column=4,padx=3,pady=5,sticky=W)
    entry_7 = DateEntry(widget_box_frame,setmode="day",date_pattern="dd/mm/yyyy",state='readonly')
    entry_7.grid(row=1,column=5,sticky=W)
    
    lbl_8 = Label(widget_box_frame,text='Micro chip:')
    lbl_8.grid(row=2,column=4,padx=3,pady=5,sticky=W)
    micro_combo = ttk.Combobox(widget_box_frame,width=10,state='readonly')
    micro_combo['values']=['Yes','No']
    micro_combo.grid(row=2,column=5,sticky=W)
    micro_combo.bind("<<ComboboxSelected>>",combo_click)
    
    lbl_9 = Label(widget_box_frame,textvariable=click_get)
    lbl_9.grid(row=3,column=4,padx=3,pady=5,sticky=W)
    ent9_text=StringVar(value="")
    entry_9 = Entry(widget_box_frame,width=17,textvariable=ent9_text,bd=0,bg="systembuttonface",state="disabled")
    entry_9.grid(row=3,column=5,sticky=W)
    
    lbl_pet_name = Label(widget_box_frame,text='Pet name:')
    lbl_pet_name.grid(row=0,column=2,padx=3,pady=5,sticky=E)
    pet_name_ent = ttk.Combobox(widget_box_frame,width=15)
    pet_name_ent['values']=pet
    pet_name_ent.current()
    pet_name_ent.grid(row=0,column=3,sticky=W)
    
    lbl_10 = Label(widget_box_frame,text='Pet type:')
    lbl_10.grid(row=1,column=2,padx=(50,3),pady=5,sticky=E)
    entry_10 = ttk.Combobox(widget_box_frame,width=9,state='readonly')
    entry_10['values']=['Dog', 'Cat', 'Other']
    entry_10.grid(row=1,column=3,sticky=W)
    
    lbl_11 = Label(widget_box_frame,text='Size:')
    lbl_11.grid(row=2,column=2,padx=3,pady=5,sticky=E)
    entry_11=ttk.Combobox(widget_box_frame,width=9,state='readonly')
    entry_11['values']=['Giant', 'Large', 'Medium', 'Small', 'Toy']
    entry_11.grid(row=2,column=3,padx=3,pady=5,sticky=W)
    
    lbl_12 = Label(widget_box_frame,text='Wieght (kg):')
    lbl_12.grid(row=3,column=2,padx=3,pady=5,sticky=E)
    entry_12 = Entry(widget_box_frame,width=7)
    entry_12.grid(row=3,column=3,sticky=W)
    
    lbl_13 = Label(widget_box_frame,text='Temper:')
    lbl_13.grid(row=4,column=2,padx=3,pady=5,sticky=E)
    entry_13=ttk.Combobox(widget_box_frame,width=11,state='readonly')
    entry_13['values']=['Difficult', 'Exellent', 'Good', 'Nervous','Agresive']
    entry_13.current()
    entry_13.grid(row=4,column=3,padx=3,pady=5,sticky=W)
    
    lbl_health = Label(widget_box_frame,text='Health:')
    lbl_health.grid(row=5,column=0,padx=3,pady=5,sticky=W)
    entry_health=ttk.Combobox(widget_box_frame,width=11,state='readonly')
    entry_health['values']=['Un-well', 'Blind', 'Def', 'Old', 'Arthritus', 'Fit & well']
    entry_health.current(5)
    entry_health.grid(row=5,column=1,padx=3,pady=5,sticky=W)
    
    lbl_atributes = Label(widget_box_frame,text='Atributes:')
    lbl_atributes.grid(row=5,column=2,padx=3,pady=5,sticky=E)
    attribute_ent=ttk.Combobox(widget_box_frame,width=15,state='readonly')
    attribute_ent['values']=['N/A', 'Barks', 'Bites', 'Escapes', 'Not social','Fights', 'Needs company', 'Muzel']
    attribute_ent.current(0)
    attribute_ent.grid(row=5,column=3,padx=3,pady=5,sticky=W)
    
    
    lbl_v1 = Label(widget_box_frame,text='Vaccinated:')
    lbl_v1.grid(row=6,column=0,padx=3,pady=5,sticky=W)
    vaccine_date_lbl = Label(widget_box_frame,textvariable=vaccin_get)
    vaccine_date_lbl.grid(row=6,column=2,padx=2,pady=5,sticky=E)
    vaccin_combo=ttk.Combobox(widget_box_frame,width=11,state='readonly')
    vaccin_combo['values']=['No', 'Yes']
    vaccin_combo.current(0)
    vaccin_combo.grid(row=6,column=1,padx=3,pady=5,sticky=W)
    vaccin_combo.bind("<<ComboboxSelected>>",vaccin_click)
    
    vac_name_combo=ttk.Combobox(widget_box_frame,width=11,state='readonly')#,state='readonly')
    vac_name_combo['values']=['N/A']
    vac_name_combo.current(0)
    vac_name_combo.grid(row=6,column=3,padx=3,pady=5,sticky=W) 
    #vaccine_date = DateEntry(widget_box_frame,setmode="day",date_pattern="dd/mm/yyyy",state='readonly',width=11)
    #vaccine_date.grid(row=6,column=3,padx=3,pady=5,sticky=W)
    
    lbl_info = Label(widget_box_frame,text="Notice:\nPet's are linked to pet owners (client).\nplease register the client details first.\nthis can be found in the ribbon menu\nNew Client Registration Form.",fg="brown")
    lbl_info.grid(row=4,column=4,columnspan=2,rowspan=3,padx=10,pady=2)#,sticky=N)
    
    clear_button=HoverButton(button_frame,text="CLEAR",font=LARGE_FONT,cursor="hand2",activebackground='#e2f723',bg="systembuttonface",fg="black",command=clear_pet)#lambda: popupmsg('Not supported just yet!'))
    clear_button.grid(row=0,column=0,padx=3,pady=6)#,sticky="E")
    save_button=HoverButton(button_frame,text="SAVE",font=LARGE_FONT,cursor="hand2",activebackground='#e2f723',bg="systembuttonface",fg="black",command=add_pet)#add_pet)popupmsg('Not supported just yet!'))
    save_button.grid(row=0,column=1,padx=3,pady=6)#,sticky="E")
    
    exit_button=HoverButton(button_frame,text="EXIT FORM",font=LARGE_FONT,cursor="hand2",activebackground='orange',bg="#e2f723",fg="black",command=pet_window.destroy)
    exit_button.grid(row=0,column=2,padx=3,pady=6)#,sticky="E")
        
        
class LangtonAndRoberts(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.iconbitmap(self,default='home.ico')
        Tk.wm_title(self, 'Langton_and_Roberts')
        
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #,Status bar,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        title_text=StringVar()
        title_text.set("Kennel Managenent System")
        status_bar=Label(self,textvariable=title_text,height=2,relief=FLAT,anchor=CENTER,bg="#e2f723",fg="brown")
        status_bar.pack(fill=X,side=BOTTOM,ipady=2,padx=0)#,expand=True)
        
        #,,Time in status bar,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        def start():
            text=time.strftime("%H:%M:%S %p")#("%A  %d/%m/%Y  %H:%M:%S %p")
            label.config(text=text)
            label.after(200,start)
        label=Label(status_bar,font=("ds-digital",9),bg="#e2f723",fg="brown")
        label.place(y=6,x=40)
        start()
        
        #,,menu pages(left),,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight, PageNine):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
             
class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)
        #,,Buttons Frame(left),,Center Frame(left),Ribbon Frame(Top),,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        #,,,Ribbon (menu) frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_4=Frame(self,relief=FLAT,bd=0,bg="white",height=6)
        can_4.pack(side='top',anchor=W,fill='x')#,expand=True)
        #,,Frame for Notebook,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_3=Frame(self,relief=FLAT,bg="white")
        can_3.pack(side='left',anchor=W,fill='both',expand=True)  
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")#,background="yellow")
        label.pack()
        
        #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,    
        #,,,Home Tab Main Side (Home Page Frame),,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        #,,,list of greetings on home page on start up.
        frase_list=["O.M.G!!,,, I can't believe\n",
                    "Shit,,,, I can't believe\n",
                    "Unbelievable,, I can't believe\n"]
        fraze=random.choice(frase_list)#https://youtu.be/XKHEtdqhLK8
        today= date.today()
        f_today=today.strftime('%A \n%B %d \n%Y ')
        day_name=today.strftime('%A')
        #print(day_name)
        if day_name =="Friday":
            today_label=Label(can_3,text=f"Shake your TIT'S,,,\nIt's \n{f_today}",font="helvetica, 70",bg="white",fg="orange",justify=LEFT)
            today_label.grid(row=0,column=0,padx=80,pady=30,sticky=W)#pack(pady=20)
        elif day_name =="Thursday":
            today_label=Label(can_3,text=f"One more sleep,,\nIt's \n{f_today}",font="helvetica, 70",bg="white",fg="orange",justify=LEFT)
            today_label.grid(row=0,column=0,padx=80,pady=30,sticky=W)#pack(pady=20)
        else:
            today_label=Label(can_3,text=f"{fraze}It's \n{f_today}",font="helvetica, 70",bg="white",fg="orange",justify=LEFT)
            today_label.grid(row=0,column=0,padx=80,pady=30,sticky=W)#pack(pady=20)
            
        
            
        #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        #,,,,Left side Buttons linked to Class Button,,,,,,,,,,,,,,,,,,,,,,,,,,,
        button1 = HoverButton(can_2, text="PAGE\nONE",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageOne))
        button1.pack(fill=X,pady=2)#grid(row=2,column=2)#pack()
        button2 = HoverButton(can_2, text="PAGE\nTWO",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'orange',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageTwo))
        button2.pack(fill=X,pady=2)#grid(row=3,column=1)#pack()
        button3 = HoverButton(can_2, text="PAGE\nTHREE",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageThree))
        button3.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button4 = HoverButton(can_2, text="PAGE\nFOUR",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'orange',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageFour))
        button4.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button5 = HoverButton(can_2, text="PAGE\nFIVE",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageFive))
        button5.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button6 = HoverButton(can_2, text="PAGE\nSIX",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'orange',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageSix))
        button6.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button7 = HoverButton(can_2, text="PAGE\nSEVER",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageSeven))
        button7.pack(fill=X,pady=2)#grid(row=3,column=1)#pack()
        button8 = HoverButton(can_2, text="PAGE\nEIGHT",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'orange',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageEight))
        button8.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        button9 = HoverButton(can_2, text="PAGE\nNINE",height=3,relief=FLAT,cursor="hand2",bd=0,activebackground= 'white',bg="#e2f723",fg="black",command=lambda: controller.show_frame(PageNine))
        button9.pack(fill=X,pady=2)#grid(row=4,column=0)#pack()
        
        def close_app():
            response = messagebox.askquestion("CLOSE", "Do you really want to Exit?\nthis will close the program!.")
            #print(response)
            if response == "yes":
                app.quit()
        
        #,,, ribbon buttons,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        ribbon_label = Label(can_4, text=" RIBBON \nMENU",font=LARGE_FONT,bg="white",fg="black")
        ribbon_label.grid(row=0,rowspan=3,column=0,ipadx=15)#pack(pady=5,padx=10)
        new_client_button = HoverButton(can_4, text="New Client\n  Registration  \nForm",relief=FLAT,activebackground="white",cursor="hand2",bg="#e2f723",bd=0,fg="black",height=5,command=client_reg_window)
        new_client_button.grid(row=0,rowspan=3,column=1,pady=0,padx=2,ipadx=15)#pack()
        new_pet_button = HoverButton(can_4, text="New Pet\n  Registration  \nForm",relief=FLAT,activebackground="orange",cursor="hand2",bg="#e2f723",bd=0,fg="black",height=5,command=pet_window)
        new_pet_button.grid(row=0,rowspan=3,column=2,pady=0,padx=2,ipadx=15)#pack()
        quick_booking_button = HoverButton(can_4, text="Quick\n  Booking  \nForm",relief=FLAT,activebackground="white",cursor="hand2",bg="#e2f723",bd=0,fg="black",height=5)
        quick_booking_button.grid(row=0,rowspan=3,column=3,pady=0,padx=2,ipadx=15)#pack()
        new_supplier_button = HoverButton(can_4, text="  New Supplier  \nForm",relief=FLAT,activebackground="orange",cursor="hand2",bg="#e2f723",bd=0,fg="black",height=5)
        new_supplier_button.grid(row=0,rowspan=3,column=4,pady=0,padx=2)#pack()
        new_product_button = HoverButton(can_4, text="New\nProduct\nForm",relief=FLAT,cursor="hand2",bd=0,activebackground="white",bg="#e2f723",fg="black",height=5)
        new_product_button.grid(row=0,rowspan=3,column=6,padx=2,pady=0,ipadx=15)#pack()
        new_service_button = HoverButton(can_4, text="New\nService",relief=FLAT,cursor="hand2",bd=0,activebackground="orange",bg="#e2f723",fg="black",height=5)
        new_service_button.grid(row=0,rowspan=3,column=7,padx=2,pady=0,ipadx=15)#pack()
        help_button = HoverButton(can_4, text="  HELP  ",relief=FLAT,activebackground="white",cursor="hand2",bg="#e2f723",bd=0,fg="black",height=5)
        help_button.grid(row=0,rowspan=3,column=8,pady=0,padx=2,ipadx=15)#pack()
        exit_program_button = HoverButton(can_4, text="  CLOSE  ",relief=FLAT,activebackground="light green",cursor="hand2",bg="#e2f723",bd=0,fg="black",height=5, command = close_app)
        exit_program_button.grid(row=0,rowspan=3,column=9,pady=0,padx=2,ipadx=15)#pack()

   
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        
        #,,, frames left Page One System Info,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        #,,main frame Right side,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        canvas_3=Frame(self,relief=RAISED,bd=0)
        canvas_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")#,background="yellow")
        label.pack()
        return_home_button = HoverButton(can_2, text="Back to Home Page",font="helvetica 12",activebackground = 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)
        #,,,Frames
        top_label_frame=Frame(canvas_3,bd=1)  
        top_label_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        heading=Label(top_label_frame,text="PAGE ONE",font="bold 30",fg="#347083")
        heading.grid(row=0,column=0,columnspan=3,padx=30,pady=25)
        button_label_frame=Frame(canvas_3,bg="light blue",bd=1)  
        button_label_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        
        #,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        #,,place everything in this frame,,,,,,,,,,,,,,,,,,,
        page_frame=Frame(canvas_3,bg="red",bd=1)  
        page_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        
        
        
        #,,,Buttons
        button1=HoverButton(button_label_frame,text="BUTTON ONE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button1.grid(row=0,column=0,padx=0,pady=0,ipady=10,ipadx=30)
        button2=HoverButton(button_label_frame,text="BUTTON TWO",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button2.grid(row=0,column=1,padx=0,pady=0,ipady=10,ipadx=30)
        button3=HoverButton(button_label_frame,text="BUTTON THREE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button3.grid(row=0,column=2,padx=0,pady=0,ipady=10,ipadx=30)
        button4=HoverButton(button_label_frame,text="BUTTON FOUR",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button4.grid(row=0,column=3,padx=0,pady=0,ipady=10,ipadx=30)
        button5=HoverButton(button_label_frame,text="BUTTON FIVE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button5.grid(row=0,column=4,padx=0,pady=0,ipady=10,ipadx=30)
        button6=HoverButton(button_label_frame,text="BUTTON SIX",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button6.grid(row=0,column=5,padx=0,pady=0,ipady=10,ipadx=30)


class PageTwo(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left and right frames,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        canvas_3=Frame(self,relief=FLAT,bd=0)
        canvas_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        #network_label.grid(row=0,column=0)
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")#,background="yellow")
        label.pack()
        return_home_button = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)
        #,,,Frames
        top_label_frame=Frame(canvas_3,bd=1)  
        top_label_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        heading=Label(top_label_frame,text="PAGE TWO",font="bold 30",fg="#347083")
        heading.grid(row=0,column=0,columnspan=3,padx=30,pady=25)
        button_label_frame=Frame(canvas_3,bg="light blue",bd=1)  
        button_label_frame.pack(pady=0,padx=0,anchor=W,fill=X)
        #,,,Buttons
        button1=HoverButton(button_label_frame,text="BUTTON ONE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button1.grid(row=0,column=0,padx=0,pady=0,ipady=10,ipadx=30)
        button2=HoverButton(button_label_frame,text="BUTTON TWO",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button2.grid(row=0,column=1,padx=0,pady=0,ipady=10,ipadx=30)
        button3=HoverButton(button_label_frame,text="BUTTON THREE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button3.grid(row=0,column=2,padx=0,pady=0,ipady=10,ipadx=30)
        button4=HoverButton(button_label_frame,text="BUTTON FOUR",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button4.grid(row=0,column=3,padx=0,pady=0,ipady=10,ipadx=30)
        button5=HoverButton(button_label_frame,text="BUTTON FIVE",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button5.grid(row=0,column=4,padx=0,pady=0,ipady=10,ipadx=30)
        button6=HoverButton(button_label_frame,text="BUTTON SIX",font=LARGE_FONT,activebackground = 'white',cursor="hand2",bg="light blue",fg="black",relief=FLAT)
        button6.grid(row=0,column=5,padx=0,pady=0,ipady=10,ipadx=30)


class PageThree(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        return_home_button = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)


class PageFour(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        return_home_button = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)


class PageFive(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        return_home_button = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)
        
        
class PageSix(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        return_home_button = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)


class PageSeven(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        return_home_button = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)


class PageEight(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        return_home_button = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)


class PageNine(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        #,,,left side frame,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        can_2=Frame(self,relief=FLAT,bd=0,bg="white")
        can_2.pack(side='left',anchor=W,fill='both')#,expand=True)
        can_3=Frame(self,relief=FLAT,bd=0)
        can_3.pack(side='left',anchor=W,fill='both',expand=True)
        #,,,load an Image,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        networkpeople=(Image.open("network.png"))
        networkpeople=networkpeople.resize((180,180))#resizes the image.
        networkpeoplePH=ImageTk.PhotoImage(networkpeople)
        network_label=tk.Label(can_2,image=networkpeoplePH)
        network_label.image=networkpeoplePH#this must be put to show the image.
        label = Label(can_2, image=networkpeoplePH, font=LARGE_FONT,bg="white")
        label.pack()
        #,,,Left side button widgets,,,,,,,,,,,,,,,,,,,,,,,,
        return_home_button = HoverButton(can_2, text="Back to Home Page",cursor="hand2",font="helvetica 12",activebackground= 'orange',bg="#e2f723",height=3,relief=FLAT,bd=0,fg="black",command=lambda: controller.show_frame(StartPage))
        return_home_button.pack(anchor=W,fill=X)


app = LangtonAndRoberts()

# ,,, make start up screen fit any monitor ,,,,,,,
width_value=app.winfo_screenwidth()
height_value=app.winfo_screenheight()
app.geometry(f"{width_value}x{height_value}+0+0")


app.mainloop()
