from optparse import Values
from tkinter import *
#from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
from turtle import bgcolor
import csv

#global f_name_editor
#global l_name_editor

root=Tk()
root.title("Year End Solutions")
#root.geometry("360x370")


# ,,,,,,,, database ,,,,,,,,,,,,
# ,,, create a database or connect to one ,,,
conn=sqlite3.connect("address_book.db")
c=conn.cursor() # ,,, create cursor ,,,

# ,,, create a table ,,,,create only once,,,,,,,,,
c.execute("""CREATE TABLE IF NOT EXISTS addresses(
          first_name text,
          last_name text
          )""")

def update():
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor() # ,,, create cursor ,,,
    record_id=delete_box.get()
    c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last WHERE oid=:oid""",
          
          {"first":f_name_editor.get(),
           "last":l_name_editor.get(),
           "oid":record_id
           })   
    
    conn.commit() # ,,, commit changers ,,,,,
    #conn.close() # ,,, commit changers ,,,,,
    editor.destroy()#,,, close window after click ,,,,
    delete_box.delete(0,END)
  
        

# update a record
def edit():
    global editor
    editor=Tk()
    editor.title("Update a record")
    # ,,, create query function ,,,
    conn=sqlite3.connect("address_book.db") # ,,, connect to Database ,,,
    c=conn.cursor() # ,,, create cursor ,,,
    record_id=delete_box.get()
    # ,,, query the database
    c.execute("SELECT* FROM addresses WHERE oid= "+ record_id)
    records=c.fetchall()
    
    global f_name_editor
    global l_name_editor
    
    # ,,, create text boxes for data entry,,,,,,
    f_name_editor = Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    l_name_editor = Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1,padx=20)

    # ,,, create text box labels ,,,,,
    f_name_label = Label(editor,text="First Name")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    l_name_label = Label(editor,text="Last Name")
    l_name_label.grid(row=1,column=0)
     
     #,,, insert info into label and clear Entry box.
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        #delete_box.delete(0, END) # clear the entry boxes after button pres
    
    edit_btn=Button(editor,text="Save record",command=update)
    edit_btn.grid(row=3,column=0,columnspan=2,pady=10,padx=10,ipadx=124)
    
    #conn.commit() # ,,, commit changers ,,,,,
    #conn.close() # ,,, commit changers ,,,,,
    

#,,,,, create a function to delete a record ,,,,,,
def delete():
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor() # ,,, create cursor ,,,
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())
    conn.commit() # ,,, commit changers ,,,,,
    conn.close() # ,,, commit changers ,,,,,
    delete_box.delete(0,END)
    
        
# ,,, create submit function for database
def submit():
    # ,,, create a database or connect to one ,,,
    conn=sqlite3.connect("address_book.db")
    c=conn.cursor() # ,,, create cursor ,,,
    # ,,. insert into table ,,,
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name)",
              {
                'f_name': f_name.get(), 
                'l_name': l_name.get()
              })
    
    
    
    conn.commit() # ,,, commit changers ,,,,,
    conn.close() # ,,, close connection ,,,,
    
    f_name.delete(0, END) # clear the entry boxes after button press
    l_name.delete(0, END) # clear the entry boxes after button press




# ,,, create query function ,,,
def query():
    conn=sqlite3.connect("address_book.db") # ,,, connect to Database ,,,
    c=conn.cursor() # ,,, create cursor ,,,
    # ,,, query the database
    c.execute("SELECT *, oid FROM addresses")
    records=c.fetchall()
    #print(records)#print test in terminal
    # ,,,loop thru results
    print_records=""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" +str(record[2]) + "\n"
        
    print(print_records)
    
    query_label=Label(root,text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)
    conn.commit() # ,,, commit changers ,,,,,
    conn.close() # ,,, close connection ,,,,
    delete_box.delete(0, END) # clear the entry boxes after button press


# ,,, create text boxes for data entry,,,,,,
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)

delete_box=Entry(root,width=30)
delete_box.grid(row=10,column=1)

# ,,, create text box labels ,,,,,
f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label = Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

delete_box_label=Label(root,text="Select ID")
delete_box_label.grid(row=10,column=0)

# ,,, Bind button to hovern,,,,,
def button_hover(e):
    submit_btn["bg"]="white"
def button_hover_leave(e):
    submit_btn["bg"]="systemButtonFace"
    
# ,,, create and place button's
submit_btn = Button(root,text="Add record to Database",command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)
submit_btn.bind("<Leave>",button_hover_leave)
submit_btn.bind("<Enter>",button_hover)

query_btn=Button(root,text="Show Records",command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=124)

delete_btn=Button(root,text="Delete record",command=delete)
delete_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=124)

edit_btn=Button(root,text="Edit record",command=edit)
edit_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=124)

# ,,, commit changers ,,,,,
conn.commit()

# ,,, close connection ,,,,
conn.close()



root.mainloop()
