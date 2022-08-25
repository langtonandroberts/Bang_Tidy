from distutils.command.config import config
from select import select
from string import capwords
from tkinter import ttk
from tkinter import*
import sqlite3
from audioop import reverse
from itertools import count
from tkinter import messagebox
from sqlite3 import Row
from tkinter import colorchooser
  
root=Tk()#,,,main window
root.title("CRM,,, TreeBase")#,,,Title
root.geometry("1230x550")#,,,size of window
#root.config(bg="light blue")

def query_database():
    #,,,clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    #,,, Create a database or connect to one.
    conn=sqlite3.connect("tree_crm.db")
    #,,,create a cursor.
    c=conn.cursor()
    #,,,get row using ID,,,,,,,
    c.execute("SELECT rowid, * FROM customers")
    records=c.fetchall()
    #,,,Add Record Entry Boxes,,,
    global count
    count = 0 #,,,start of ID
     
    for record in records:
        if count % 2==0:
            my_tree.insert(parent="",index="end",iid=count,text="",values=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=("evenrow",))
        else:
            my_tree.insert(parent="",index="end",iid=count,text="",values=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=("oddrow",))
        #,,,increment counter adds 1 to each record entered (ID number),,,,
        count +=1   
        #,,,commit the changes
    conn.commit()
        #,,,close the connection
    conn.close()

def search_records():
    lookup_record=search_entry.get()
    #,,,close the search box
    search.destroy()
    #,,,clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    #,,, Create a database or connect to one.
    conn=sqlite3.connect("tree_crm.db")
    #,,,create a cursor.
    c=conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers WHERE last_name like ?",(lookup_record,))
    records=c.fetchall()
    #,,,Add Record Entry Boxes,,,
    global count
    count = 0
            
    for record in records:
        if count % 2==0:
            my_tree.insert(parent="",index="end",iid=count,text="",values=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=("evenrow",))
        else:
            my_tree.insert(parent="",index="end",iid=count,text="",values=(record[1],record[2],record[0],record[4],record[5],record[6],record[7]), tags=("oddrow",))
        #,,,increment counter,,,,
        count +=1   
        #,,,commit the changes
    conn.commit()
        #,,,close the connection
    conn.close()

def lookup_records():
    global search_entry, search
    search=Toplevel(root)
    search.title("Search Records")
    search.geometry("400x200")
    
    #,,,create lable frame
    search_frame=LabelFrame(search,text="Last Name")
    search_frame.pack(padx=10,pady=10)
    
    #,,,add entry box
    search_entry=Entry(search_frame,font=("Helvetica",18))
    search_entry.pack(padx=20,pady=20,)
    #,,,focus cursor on start.
    search_entry.focus()
    #,,,add a button
    search_button1=Button(search,text="Search Records",command=search_records)
    search_button1.pack(padx=20,pady=20)

def primary_colour():
    #,,,pick colour
    primary_colour=colorchooser.askcolor()[1]
    #,,,update treeview colour
    if primary_colour:
        #,,, create striped rows in treeview,,,
        my_tree.tag_configure("evenrow",background=primary_colour)

def secondary_colour():
    #,,,pick colour
    secondary_colour=colorchooser.askcolor()[1]
    #,,,update treeview colour
    if secondary_colour:
        #,,, create striped rows in treeview,,,
        my_tree.tag_configure("oddrow",background=secondary_colour)
    
def highlight_colour():
    highlight_colour=colorchooser.askcolor()[1]
    #,,,update treeview colour
    #,,,Change selected colour,,,
    if highlight_colour:
        style.map("Treeview",
            background=[("selected",highlight_colour)])


def button_hover3(e):
    money_in["bg"]="white"

def button_leave3(e):
    money_in["bg"]="light blue"#,,,"SystemButtonFace",,normal colour.

def button_hover4(e):
    money_out["bg"]="white"

def button_leave4(e):
    money_out["bg"]="light blue"#,,,"SystemButtonFace",,normal colour.

#,,, add menu options to main window,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
my_menu=Menu(root)
root.config(menu=my_menu)
#,,,configure menu
option_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Options",menu=option_menu)
#,,,drop down menu,,,
option_menu.add_command(label="Primary Colour",command=primary_colour)
option_menu.add_command(label="Secondary Colour",command=secondary_colour)
option_menu.add_command(label="Highlight Colour",command=highlight_colour)
option_menu.add_separator()
option_menu.add_command(label="Exit Options",command="root.quit")

#,,,search menu
#,,,configure menu
search_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Search Records",menu=search_menu)
#,,,drop down menu,,,
search_menu.add_command(label="Search Customers",command=lookup_records)
search_menu.add_separator()
search_menu.add_command(label="Show All",command=query_database)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

#,,,do some stuff,,,
#,,, Create a database or connect to one.
conn=sqlite3.connect("tree_crm.db")
#,,,create a cursor.
c=conn.cursor()
#,,,create a table.
c.execute("""CREATE TABLE if not exists customers(
    first_name text,
    last_name text,
    id integer,
    address text,
    town text,
    city text,
    postcode text)
    """)

#,,,commit the changes
conn.commit()
#,,,close the connection
conn.close()

#,,,add some style,,,
style=ttk.Style() 
#,,,pick a theme,,,
style.theme_use("default")
#,,,configure the Treevew Colour,,,
style.configure("Treeview",
    background="#D3D3D3",
    foreground="black",
    rowheight=25,
    fielbackground="#D3D3D3")

#,,,Change selected colour,,,
global background
style.map("Treeview",
    background=[("selected","#347083")]) 

top_frame=Frame(root,width=180,height=500,bg="lightblue")
top_frame.pack(side="left",fill="both",expand="no")#(padx=20,pady=20)#fill="x",expand="yes"

left_frame=LabelFrame(top_frame,text="Left Frame",bg="light blue",fg="black")
left_frame.pack(padx=10,pady=20)#fill="x",expand="yes"

wid=Label(left_frame,text="CUSTOMER DATABASE",bg="light blue")
wid.pack()#grid(row=0,columnspan=2,padx=10,pady=10)

money_in=Button(left_frame,text="MONEY IN",bg="light blue",width=20,relief="flat",command=button_hover3)#,anchor="w"
money_in.pack(pady=10)#grid(row=1,column=0,padx=2,pady=2)
money_in.bind("<Enter>",button_hover3)
money_in.bind("<Leave>",button_leave3)

money_out=Button(left_frame,text="MONEY OUT",bg="light blue",width=20,relief="flat",command=button_hover4)#,anchor="w"
money_out.pack()#grid(row=1,column=2,padx=2,pady=2)
money_out.bind("<Enter>",button_hover4)
money_out.bind("<Leave>",button_leave4)


first_label_frame=LabelFrame(root,text="Customer Data Frame",fg="black",font=20)
first_label_frame.pack(side="left",padx=10,pady=20)#fill="x",expand="yes"
#,,,create Treeview frame,,,
tree_frame=Frame(first_label_frame)  
tree_frame.pack(pady=10,padx=10)
#,,,Create Treeview Scroll,,,
tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)
#,,,Create the Treeview,,,,
my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended")
my_tree.pack()
#,,,Configure the scrollbar,,,
tree_scroll.config(command=my_tree.yview)
#,,,Define the Columns,,,
my_tree["columns"]=("First Name","Last Name","ID","Address","Town","City","Postcode")
#,,,Format the Columns,,,
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("First Name",anchor=W,width=140)
my_tree.column("Last Name",anchor=W,width=140)
my_tree.column("ID",anchor=CENTER,width=100)
my_tree.column("Address",anchor=CENTER,width=140)
my_tree.column("Town",anchor=CENTER,width=140)
my_tree.column("City",anchor=CENTER,width=140)
my_tree.column("Postcode",anchor=CENTER,width=140)
#,,,Create Headings,,,
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("First Name",text="First Name",anchor=W)
my_tree.heading("Last Name",text="Last Name",anchor=CENTER)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Address",text="Address",anchor=CENTER)
my_tree.heading("Town",text="Town",anchor=CENTER)
my_tree.heading("City",text="City",anchor=CENTER)
my_tree.heading("Postcode",text="Post code",anchor=CENTER)

#,,, create striped rows in treeview,,,
my_tree.tag_configure("oddrow",background="white")
my_tree.tag_configure("evenrow",background="lightblue")

#,,,add record Entry frame and Boxes,,,,,
data_frame=LabelFrame(first_label_frame,text="Customer Information")
data_frame.pack(padx=10)#fill="x",expand="yes"

fn_label=Label(data_frame,text="First Name")
fn_label.grid(row=0,column=0,padx=30,pady=10)
fn_entry=Entry(data_frame)
fn_entry.grid(row=0,column=1,padx=10,pady=10)
  
ln_label=Label(data_frame,text="Last Name")
ln_label.grid(row=0,column=2,padx=10,pady=10)
ln_entry=Entry(data_frame)
ln_entry.grid(row=0,column=3,padx=10,pady=10)  
 
id_label=Label(data_frame,text="ID Name")
id_label.grid(row=0,column=4,padx=10,pady=10)
id_entry=Entry(data_frame,state="normal")
id_entry.grid(row=0,column=5,padx=10,pady=10)

address_label=Label(data_frame,text="Address")
address_label.grid(row=1,column=0,padx=10,pady=10)
address_entry=Entry(data_frame)
address_entry.grid(row=1,column=1,padx=10,pady=10)

town_label=Label(data_frame,text="Town")
town_label.grid(row=1,column=2,padx=10,pady=10)
town_entry=Entry(data_frame)
town_entry.grid(row=1,column=3,padx=10,pady=10)  
  
city_label=Label(data_frame,text="City")
city_label.grid(row=1,column=4,padx=10,pady=10)
city_entry=Entry(data_frame)
city_entry.grid(row=1,column=5,padx=10,pady=10)  
  
postcode_label=Label(data_frame,text="Postcode")
postcode_label.grid(row=1,column=6,padx=10,pady=10)
postcode_entry=Entry(data_frame)
postcode_entry.grid(row=1,column=7,padx=10,pady=10) 

#,,,Move Row up.
def up():
    rows=my_tree.selection()
    for row in rows:
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)-1)

#,,,Move Row Down
def down():
    rows=my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)+1)

#,,, Remove one record.
def remove_one():
    response = messagebox.askyesno("WARNING!!", "This will DELETE Selected from the table\nAre You Sure?!.")
    #,,,add logic for message box(YES=1, NO=0)
    if response==1:
        x=my_tree.selection()[0]
        my_tree.delete(x)
        
        #,,, Create a database or connect to one that executes the remove.
        conn=sqlite3.connect("tree_crm.db")
        #,,,create a cursor.
        c=conn.cursor()
        #,,,Delete from database.
        c.execute("DELETE from customers WHERE oid = " + id_entry.get())
        #,,,commit the changes
        conn.commit()
        #,,,close the connection
        conn.close()
        #,,,clear entry boxes.
        clear_entries()
        #,, 'add a little pop up message after delete.
        messagebox.showinfo("Removed", "Your Record Has Been Deleted")
    
#,,, Remove many records.
def remove_many():
    response = messagebox.askyesno("WARNING!!", "This will DELETE Selection from the table\nAre You Sure?!.")
    #,,,add logic for message box.
    if response==1:
        #,,,desegnate selections
        x=my_tree.selection()
        
        #,,,create list of ID's.
        ids_to_delete=[]
        
        #,,,add selections to ids_to_delete list.
        for record in x:
            ids_to_delete.append(my_tree.item(record,"values")[2])
        #,,,Delete from treeview.
        for record in x:
            my_tree.delete(record)
        #,,,create database.    
        conn=sqlite3.connect("tree_crm.db")
        #,,,create a cursor.
        c=conn.cursor()
        #,,,delete everything from table
        c.executemany("DELETE FROM customers WHERE oid = ?",[(a,)for a in ids_to_delete])
        #,,,commit the changes
        conn.commit()
            #,,,close the connection
        conn.close()
            #,,,clear entries from boxes if filled.
        clear_entries()
        messagebox.showinfo("SELECTION DELETED", "SELECTION Has Been Deleted")


#,,,Clear entry boxes
def clear_entries():
    my_tree.forget
    #,,,re activates the add button.
    add_button["state"]="active"
    #,,,Clear entry boxes.
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    town_entry.delete(0,END)
    city_entry.delete(0,END)
    postcode_entry.delete(0,END)
    my_tree.delete(*my_tree.get_children())
    query_database()
    #fn_entry.focus() #forget
    

#,,, Select Record
def select_record(e):
    add_button["state"]="disabled"
    #,,,Clear entry boxes.
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    town_entry.delete(0,END)
    city_entry.delete(0,END)
    postcode_entry.delete(0,END)
    #,,,Grabe entry
    selected=my_tree.focus()
    #,,,Grab record values.
    values=my_tree.item(selected,"values")
    #,,,output to boxes.
    fn_entry.insert(0,values[0])
    ln_entry.insert(0,values[1])
    id_entry.insert(0,values[2])
    address_entry.insert(0,values[3])
    town_entry.insert(0,values[4])
    city_entry.insert(0,values[5])
    postcode_entry.insert(0,values[6])
    #fn_entry.focus()
    
#,,, Update record,,,
def update_record():
        #,,,grab record number
        select=my_tree.focus()
        #,,,update record
        my_tree.item(select,text="",
                    values=(fn_entry.get(),
                    ln_entry.get(),
                    id_entry.get(),
                    address_entry.get(),
                    town_entry.get(),
                    city_entry.get(),
                    postcode_entry.get(),))
        #,, add our data to the screen.
        #,,, Create a database or connect to one that executes.
        conn=sqlite3.connect("tree_crm.db")
        #,,,create a cursor.
        c=conn.cursor()
        c.execute("""UPDATE customers SET
            first_name=:first,
            last_name=:last,
            address=:address,
            town=:town,
            city=:city,
            postcode=:postcode
            
            WHERE oid=:oid""",
            {
            "first":fn_entry.get(),
            "last":ln_entry.get(),
            "address":address_entry.get(),
            "town":town_entry.get(),
            "city":city_entry.get(),
            "postcode":postcode_entry.get(),
            "oid":id_entry.get(),
            
            })
        #,,,commit the changes
        conn.commit()
        #,,,close the connection
        conn.close()
        messagebox.showinfo("UPDATED", "Record has been UPDATED!")
        
    #,,,Clear entry boxes.
        fn_entry.delete(0,END)
        ln_entry.delete(0,END)
        id_entry.delete(0,END)
        address_entry.delete(0,END)
        town_entry.delete(0,END)
        city_entry.delete(0,END)
        postcode_entry.delete(0,END)
        my_tree.delete(*my_tree.get_children())
        query_database()
    
#,,,add new record to database.
def add_record():
    #,,, Create a database or connect to one that executes.
    conn=sqlite3.connect("tree_crm.db")
    #,,,create a cursor.
    c=conn.cursor()
    #,,,add new record.
    c.execute("INSERT INTO customers VALUES(:first,:last,:id,:address,:town,:city,:postcode)",
        {
            "first":fn_entry.get(),
            "last":ln_entry.get(),
            "id":id_entry.get(),
            "address":address_entry.get(),
            "town":town_entry.get(),
            "city":city_entry.get(),
            "postcode":postcode_entry.get(),
        })
    
    #,,,commit the changes
    conn.commit()
    #,,,close the connection
    conn.close()
    
    #,,,Clear entry boxes.
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    town_entry.delete(0,END)
    city_entry.delete(0,END)
    postcode_entry.delete(0,END)
    #,,,cleare treeview table.
    my_tree.delete(*my_tree.get_children())
    query_database()
    
    
    


    
def button_hover(e):
    add_button["fg"]="green"
    
def button_hover_2(e):
    search_button1["fg"]="red"

def button_leave(e):
    add_button["fg"]="black"#,,,"SystemButtonFace",,normal colour.
    
def button_leave_2(e):
    search_button1["fg"]="black"#,,,"SystemButtonFace",,normal colour.
    

    

#,,, add Buttons to database frame
button_frame=LabelFrame(first_label_frame,text="Command Buttons")
button_frame.pack(padx=0,pady=10)#fill="x",expand="yes"

update_button=Button(button_frame,text="Update Record",command=update_record)
update_button.grid(row=0,column=0,padx=10,pady=10)

add_button=Button(button_frame,text="Add Record",command=add_record)
add_button.grid(row=0,column=1,padx=10,pady=10)
add_button.bind("<Enter>",button_hover)
add_button.bind("<Leave>",button_leave)

search_button1=Button(button_frame,text="Search For Customer",command=lookup_records)
search_button1.grid(row=0,column=2,padx=10,pady=10)
#,,,cursor hover over button
search_button1.bind("<Enter>",button_hover_2)
search_button1.bind("<Leave>",button_leave_2)

remove_one_button=Button(button_frame,text="Remove One Selected",command=remove_one)
remove_one_button.grid(row=0,column=3,padx=10,pady=10)

remove_many_button=Button(button_frame,text="Remove Many Selected",command=remove_many)
remove_many_button.grid(row=0,column=4,padx=10,pady=10)

move_up_button=Button(button_frame,text="Move Up",command=up)
move_up_button.grid(row=0,column=5,padx=10,pady=10)

move_down_button=Button(button_frame,text="Move Down",command=down)
move_down_button.grid(row=0,column=6,padx=10,pady=10)

select_button=Button(button_frame,text="Clear Entry Boxes",command=clear_entries)
select_button.grid(row=0,column=7,padx=10,pady=10)

#,,, Bind the tree.
my_tree.bind("<ButtonRelease-1>",select_record)




#fn_entry.focus()


#,,,run to pull data from database on start.  
query_database()  
  
root.mainloop()  
  