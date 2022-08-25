
#https://youtu.be/nujhZ4MM41Q

#find the total of sales from the date picker.

import tkinter as tk 
from tkinter import ttk 
from tkcalendar import DateEntry 
import sqlite3 


my_w=tk.Tk()
my_w.geometry('900x650')
my_w.title('Finance reports')

conn=sqlite3.connect("tree_crm.db")
#,,,create a cursor.
c=conn.cursor()
#,,,create department table and headings.,,,,,,,,,,,,,,,,,,,,,,,
c.execute('''CREATE TABLE if not exists reports_example(
    p_id int,
    price float NOT NULL,
    quantity integar NOT NULL,
    bill_number int NOT NULL,
    bill_date date
    )''')

#c.execute("INSERT into reports_example (p_id,price,quantity,bill_number,bill_date) VALUES (1,2.99,2,222,'2022-09-30')")
#,,,commit the changes
conn.commit()
#,,,close the connection
conn.close()




sel=tk.StringVar()
cal=DateEntry(my_w,selectmode='day',textvariable=sel)

cal.grid(row=0,column=0,padx=20,pady=30)

def my_update(*args):
    if (len(sel.get())>4):
        dt=cal.get_date()
        dt1=dt.strftime('%y/%m/%d')#format in data base
        dt2=dt.strftime("%d %B %Y")#format displayed in label
        l1.config(text='Date selected: ' +dt2)
        #,,, Create a database or connect to one.
        conn=sqlite3.connect("tree_crm.db")
        #,,,create a cursor.
        c=conn.cursor()
        # getting data from MySQL student table 
        print("DONE, DATE SELECTED: "+ dt2)
        query="SELECT * FROM reports_example WHERE bill_date = '2022-09-30'"
        data=c.execute(query,)
        #remove old data from treeview (fresh data)
        for item in trv.get_children():
            trv.delete(item)
        total=0
        for dt in data:
            trv.insert("", 'end',iid=dt[0], text=dt[0],
                    values =(dt[0],dt[1],dt[2],dt[3],dt[4]))
            a=float(dt[1])
            b=float(dt[2])
            total=total+ (a* b)#quantity x price 2 decimal places
        l2.config(text=f"Total sales\nfor that day\n £ " + format((total),'.2f'))
        #format(float(values[4]),'.2f'))


#creat Treeview.
trv = ttk.Treeview(my_w, selectmode ='browse')  
trv.grid(row=1,column=1,padx=20,pady=20)
# number of columns
trv["columns"] = ("1", "2", "3","4","5")
  
# Defining heading
trv['show'] = 'headings'
  
# width of columns and alignment 
trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 80, anchor ='c')
trv.column("3", width = 80, anchor ='c')
trv.column("4", width = 80, anchor ='c')
trv.column("5", width = 80, anchor ='c')
  
# Headings  
# respective columns
trv.heading("1", text ="p_id")
trv.heading("2", text ="Price")
trv.heading("3", text ="Quantity")
trv.heading("4", text ="Bill_no")  
trv.heading("5", text ="Bill_date")

sel.trace('w',my_update)
l1=tk.Label(my_w,font=('Times',22,'bold'),fg='blue')
l1.grid(row=0,column=1)


l2=tk.Label(my_w,font=('Times',22,'bold'),fg='red')
l2.grid(row=1,column=2)


my_w.mainloop()
